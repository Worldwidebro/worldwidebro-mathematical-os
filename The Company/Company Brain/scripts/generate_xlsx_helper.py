#!/usr/bin/env python3
"""
Pure-Python zero-dependency OpenXML (.xlsx) generator.
Creates valid Excel workbooks using only the Python standard library (zipfile, xml).
"""

import os
import zipfile
import html

def escape_xml(s):
    return html.escape(str(s), quote=True)

def col_letter(col_idx):
    """1-indexed col index to Excel letter: 1 -> A, 27 -> AA"""
    result = ""
    while col_idx > 0:
        col_idx, remainder = divmod(col_idx - 1, 26)
        result = chr(65 + remainder) + result
    return result

def create_simple_xlsx(filepath, sheets_data):
    """
    sheets_data is a dict where:
    key: sheet_name
    value: list of rows (each row is a list of cell values)
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Pre-generate sheets XML
    sheet_entries = []
    sheet_rels = []
    content_types_sheets = []
    
    for idx, (sname, rows) in enumerate(sheets_data.items(), 1):
        r_id = f"rId{idx}"
        sheet_entries.append((sname, idx, r_id))
        sheet_rels.append(f'<Relationship Id="{r_id}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{idx}.xml"/>')
        content_types_sheets.append(f'<Override PartName="/xl/worksheets/sheet{idx}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')

    # [Content_Types].xml
    content_types = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
  {''.join(content_types_sheets)}
</Types>"""

    # _rels/.rels
    root_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""

    # xl/_rels/workbook.xml.rels
    workbook_rels = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  {''.join(sheet_rels)}
  <Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

    # xl/workbook.xml
    sheets_xml = "".join([f'<sheet name="{escape_xml(name)}" sheetId="{idx}" r:id="{rid}"/>' for name, idx, rid in sheet_entries])
    workbook_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    {sheets_xml}
  </sheets>
</workbook>"""

    # xl/styles.xml (Simple institutional styles: Normal, Header, Currency, Bold)
    styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <numFmts count="1">
    <numFmt numFmtId="164" formatCode="$#,##0;($#,##0);&quot;-&quot;"/>
  </numFmts>
  <fonts count="3">
    <font><sz val="10"/><name val="Calibri"/></font>
    <font><b val="1"/><sz val="10"/><name val="Calibri"/><color rgb="FFFFFFFF"/></font>
    <font><b val="1"/><sz val="10"/><name val="Calibri"/><color rgb="FF0F172A"/></font>
  </fonts>
  <fills count="4">
    <fill><patternFill patternType="none"/></fill>
    <fill><patternFill patternType="gray125"/></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF0F172A"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFF1F5F9"/></patternFill></fill>
  </fills>
  <borders count="2">
    <border><left/><right/><top/><bottom/></border>
    <border>
      <left style="thin"><color rgb="FFE2E8F0"/></left>
      <right style="thin"><color rgb="FFE2E8F0"/></right>
      <top style="thin"><color rgb="FFE2E8F0"/></top>
      <bottom style="thin"><color rgb="FFE2E8F0"/></bottom>
    </border>
  </borders>
  <cellStyleXfs count="1">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0"/>
  </cellStyleXfs>
  <cellXfs count="4">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1"/>
    <xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="center"/></xf>
    <xf numFmtId="0" fontId="2" fillId="3" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="164" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1"/>
  </cellXfs>
</styleSheet>"""

    with zipfile.ZipFile(filepath, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", root_rels)
        zf.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
        zf.writestr("xl/workbook.xml", workbook_xml)
        zf.writestr("xl/styles.xml", styles_xml)

        for sidx, (sname, rows) in enumerate(sheets_data.items(), 1):
            sheet_rows_xml = []
            max_col = 1
            for r_num, row in enumerate(rows, 1):
                cells_xml = []
                for c_num, val in enumerate(row, 1):
                    if c_num > max_col:
                        max_col = c_num
                    c_ref = f"{col_letter(c_num)}{r_num}"
                    
                    if r_num == 1:
                        style_id = 's="1"'
                    elif any(k in str(row[0]).upper() for k in ["TOTAL", "NET", "EBITDA"]):
                        style_id = 's="2"'
                    else:
                        style_id = 's="0"'

                    if val is None or val == "":
                        cells_xml.append(f'<c r="{c_ref}" {style_id}/>')
                    elif isinstance(val, (int, float)):
                        cells_xml.append(f'<c r="{c_ref}" {style_id}><v>{val}</v></c>')
                    elif isinstance(val, str) and val.startswith("="):
                        formula_body = escape_xml(val[1:])
                        cells_xml.append(f'<c r="{c_ref}" {style_id}><f>{formula_body}</f></c>')
                    else:
                        sval = str(val).strip()
                        if sval.startswith("$") and sval[1:].replace(",", "").replace(".", "").replace("-", "").isdigit():
                            clean_num = sval.replace("$", "").replace(",", "")
                            cstyle = 's="3"' if r_num > 1 and style_id != 's="2"' else style_id
                            cells_xml.append(f'<c r="{c_ref}" {cstyle}><v>{clean_num}</v></c>')
                        else:
                            clean_str = escape_xml(sval)
                            cells_xml.append(f'<c r="{c_ref}" t="inlineStr" {style_id}><is><t>{clean_str}</t></is></c>')

                sheet_rows_xml.append(f'<row r="{r_num}">{"".join(cells_xml)}</row>')

            cols_xml = "".join([f'<col min="{c}" max="{c}" width="22" customWidth="1"/>' for c in range(1, max_col + 1)])

            ws_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <cols>{cols_xml}</cols>
  <sheetData>
    {''.join(sheet_rows_xml)}
  </sheetData>
</worksheet>"""
            zf.writestr(f"xl/worksheets/sheet{sidx}.xml", ws_xml)

    return filepath
