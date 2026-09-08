# Official 2022 NAICS Structure & Labor Market Taxonomy

> **Standard:** North American Industry Classification System (United States, 2022)
> **Authority:** U.S. Economic Classification Policy Committee (ECPC) / Office of Management and Budget (OMB) / U.S. Census Bureau
> **Official Source:** `2022_NAICS_Structure.xlsx` (SHA256: `217c9e0d4d74e751...`)
> **Dataset Totals:** **20 Sectors** | **96 Subsectors** | **308 Industry Groups** | **692 NAICS Industries** | **1,012 U.S. National Industries** (2,125 Total Nodes)

---

## 1. Executive Summary

The North American Industry Classification System (NAICS) is the canonical classification standard used by Federal statistical agencies in classifying business establishments for the purpose of collecting, analyzing, and publishing statistical data related to the U.S. business economy.

In **OPS-001 (Universal Labor Marketplace & Operating System)**, NAICS serves as the **root ontological anchor** for all employer accounts, job orders, and statutory classification models:

```text
NAICS (2-6 Digits) ↓ Employer ↓ Sector/Industry ↓ Occupation (SOC) ↓ Job Order ↓ Tasks ↓ Skills ↓ Credentials ↓ Worker
```

---

## 2. All 20 Official NAICS Sectors

| Sector Code | Sector Title | Subsectors (3-Digit) | Industry Groups (4-Digit) | National Industries (6-Digit) | Trilateral |
| :--- | :--- | :---: | :---: | :---: | :---: |
| `11` | **Agriculture, Forestry, Fishing and Hunting** | 5 | 19 | 64 | ✅ Yes |
| `21` | **Mining, Quarrying, and Oil and Gas Extraction** | 3 | 5 | 21 | ✅ Yes |
| `22` | **Utilities** | 1 | 3 | 14 | ✅ Yes |
| `23` | **Construction** | 3 | 10 | 31 | ✅ Yes |
| `31-33` | **Manufacturing** | 21 | 86 | 346 | ✅ Yes |
| `42` | **Wholesale Trade** | 3 | 19 | 69 | ✅ Yes |
| `44-45` | **Retail Trade** | 9 | 24 | 57 | ✅ Yes |
| `48-49` | **Transportation and Warehousing** | 11 | 29 | 57 | ✅ Yes |
| `51` | **Information** | 6 | 11 | 29 | ✅ Yes |
| `52` | **Finance and Insurance** | 5 | 11 | 35 | ✅ Yes |
| `53` | **Real Estate and Rental and Leasing** | 3 | 8 | 24 | ✅ Yes |
| `54` | **Professional, Scientific, and Technical Services** | 1 | 9 | 49 | ✅ Yes |
| `55` | **Management of Companies and Enterprises** | 1 | 1 | 3 | ✅ Yes |
| `56` | **Administrative and Support and Waste Management and Remediation Services** | 2 | 11 | 44 | ✅ Yes |
| `61` | **Educational Services** | 1 | 7 | 17 | ✅ Yes |
| `62` | **Health Care and Social Assistance** | 4 | 18 | 39 | ✅ Yes |
| `71` | **Arts, Entertainment, and Recreation** | 3 | 9 | 25 | ✅ Yes |
| `72` | **Accommodation and Food Services** | 2 | 6 | 15 | ✅ Yes |
| `81` | **Other Services (except Public Administration)** | 4 | 14 | 44 | ✅ Yes |
| `92` | **Public Administration** | 8 | 8 | 29 | ✅ Yes |

---

## 3. 2022 Revisions & Change Indicators

The 2022 NAICS revision includes major restructuring in **Retail Trade (Sector 44-45)**, **Information (Sector 51)**, and **Manufacturing (Sector 31-33)** to reflect modern digital commerce and technological convergence.

| Indicator | Meaning | Record Count |
| :---: | :--- | :---: |
| `*` | Title change, no content change | 31 |
| `**` | New code for 2022 NAICS | 186 |
| `***` | Re-used code, content change | 7 |
| `****` | Content change at lower level | 5 |
| *(None)* | Unchanged from 2017 | 1896 |

---

## 4. Hierarchy Specification

- **Level 1: Sector (2-digit or 2-digit range)**: 20 sectors representing general economic activities.
- **Level 2: Subsector (3-digit)**: 96 subsectors grouping establishments with similar production processes.
- **Level 3: Industry Group (4-digit)**: 308 industry groups.
- **Level 4: NAICS Industry (5-digit)**: 692 industries comparable across US, Canada, and Mexico.
- **Level 5: National Industry (6-digit)**: 1,012 detailed US-specific industry classifications.
