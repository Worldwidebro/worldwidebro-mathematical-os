#!/usr/bin/env python3
"""
Document Preprocessor (RAG-Anything alternative)
Handles diverse document formats for Week 0 ingestion
Converts: PDF, DOCX, CSV, JSON, markdown → plain text → LightRAG
"""

import csv
import json
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProcessedDocument:
    """Preprocessed document ready for LightRAG"""
    doc_id: str
    filename: str
    format: str
    text: str
    metadata: Dict
    chunks: List[str] = None
    chunk_size: int = 512


class DocumentPreprocessor:
    """Process documents from multiple formats into clean text"""

    SUPPORTED_FORMATS = ["txt", "md", "csv", "json"]

    def __init__(self, chunk_size: int = 512):
        self.chunk_size = chunk_size
        self.processed: List[ProcessedDocument] = []

    def process_markdown(self, filepath: str) -> ProcessedDocument:
        """Process markdown file: extract headings + content"""
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract structured info from markdown
        lines = content.split("\n")
        text_content = "\n".join(lines)

        # Extract metadata from frontmatter if present
        metadata = {}
        if text_content.startswith("---"):
            parts = text_content.split("---", 3)
            if len(parts) > 2:
                try:
                    metadata = json.loads("{" + parts[1].strip() + "}")
                except:
                    pass
                text_content = parts[2]

        return ProcessedDocument(
            doc_id=f"md_{Path(filepath).stem}",
            filename=Path(filepath).name,
            format="markdown",
            text=text_content,
            metadata=metadata or {"source": "markdown"},
            chunks=self._chunk_text(text_content)
        )

    def process_csv(self, filepath: str) -> ProcessedDocument:
        """Process CSV file: convert rows to text blocks"""
        rows = []
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

        # Convert CSV rows to natural language
        text_blocks = []
        for row in rows:
            block = " | ".join([f"{k}: {v}" for k, v in row.items()])
            text_blocks.append(block)

        text_content = "\n".join(text_blocks)

        return ProcessedDocument(
            doc_id=f"csv_{Path(filepath).stem}",
            filename=Path(filepath).name,
            format="csv",
            text=text_content,
            metadata={"rows": len(rows), "columns": len(rows[0]) if rows else 0},
            chunks=self._chunk_text(text_content)
        )

    def process_json(self, filepath: str) -> ProcessedDocument:
        """Process JSON file: flatten structure to text"""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Flatten JSON to text
        text_content = self._flatten_json(data)

        return ProcessedDocument(
            doc_id=f"json_{Path(filepath).stem}",
            filename=Path(filepath).name,
            format="json",
            text=text_content,
            metadata={"keys": len(data) if isinstance(data, dict) else len(data)},
            chunks=self._chunk_text(text_content)
        )

    def process_text(self, filepath: str) -> ProcessedDocument:
        """Process plain text file"""
        with open(filepath, "r", encoding="utf-8") as f:
            text_content = f.read()

        return ProcessedDocument(
            doc_id=f"txt_{Path(filepath).stem}",
            filename=Path(filepath).name,
            format="text",
            text=text_content,
            metadata={"lines": len(text_content.split("\n"))},
            chunks=self._chunk_text(text_content)
        )

    def process_file(self, filepath: str) -> Optional[ProcessedDocument]:
        """Auto-detect format and process"""
        path = Path(filepath)
        suffix = path.suffix.lower().lstrip(".")

        if suffix == "md":
            return self.process_markdown(filepath)
        elif suffix == "csv":
            return self.process_csv(filepath)
        elif suffix == "json":
            return self.process_json(filepath)
        elif suffix == "txt":
            return self.process_text(filepath)
        else:
            print(f"⚠️  Unsupported format: {suffix}")
            return None

    def process_bulk(self, directory: str, pattern: str = "*") -> List[ProcessedDocument]:
        """Process all matching files in directory"""
        docs = []
        path = Path(directory)

        for filepath in path.glob(pattern):
            if filepath.is_file():
                doc = self.process_file(str(filepath))
                if doc:
                    docs.append(doc)
                    self.processed.append(doc)

        return docs

    def _chunk_text(self, text: str, chunk_size: int = None) -> List[str]:
        """Split text into overlapping chunks"""
        if chunk_size is None:
            chunk_size = self.chunk_size

        chunks = []
        sentences = re.split(r"(?<=[.!?])\s+", text)
        current_chunk = ""

        for sentence in sentences:
            if len(current_chunk) + len(sentence) < chunk_size:
                current_chunk += sentence + " "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + " "

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def _flatten_json(self, obj, prefix="") -> str:
        """Recursively flatten JSON to text"""
        lines = []

        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    lines.append(self._flatten_json(v, f"{prefix}{k}."))
                else:
                    lines.append(f"{prefix}{k}: {v}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                if isinstance(item, (dict, list)):
                    lines.append(self._flatten_json(item, f"{prefix}[{i}]."))
                else:
                    lines.append(f"{prefix}[{i}]: {item}")

        return "\n".join(lines)

    def get_text(self, doc_id: str) -> Optional[str]:
        """Get processed text for a document"""
        for doc in self.processed:
            if doc.doc_id == doc_id:
                return doc.text
        return None

    def get_chunks(self, doc_id: str) -> Optional[List[str]]:
        """Get chunked text for a document"""
        for doc in self.processed:
            if doc.doc_id == doc_id:
                return doc.chunks
        return None

    def stats(self) -> Dict:
        """Get preprocessing statistics"""
        total_docs = len(self.processed)
        total_text = sum(len(d.text) for d in self.processed)
        total_chunks = sum(len(d.chunks) if d.chunks else 0 for d in self.processed)
        by_format = {}

        for doc in self.processed:
            if doc.format not in by_format:
                by_format[doc.format] = 0
            by_format[doc.format] += 1

        return {
            "total_documents": total_docs,
            "total_text_chars": total_text,
            "total_chunks": total_chunks,
            "by_format": by_format,
            "avg_doc_size": total_text // total_docs if total_docs > 0 else 0
        }


def demo_preprocessor():
    """Demo: Process sample documents"""
    preprocessor = DocumentPreprocessor(chunk_size=512)

    print(f"\n📄 Document Preprocessor Demo (RAG-Anything alternative)")
    print(f"{'='*70}\n")

    # Create sample documents
    sample_docs = {
        "sample_venture.txt": """
        HRMS Payroll Platform Venture
        ================================

        Owner: Worldwidebro Holdings
        Status: ACTIVE
        Metrics:
        - CAC: $120
        - LTV: $500
        - ROI: 75%
        - Survival Metric: 72
        - Churn Rate: 8%

        Latest Decision: SCALE
        Capital Allocated: $50,000
        Execution: Lead search + SMS campaigns
        """,
        "venture_metrics.csv": """venture_id,metric_name,value,date
venture_hrms_001,survival_metric,72,2026-05-14
venture_hrms_001,roi,75,2026-05-14
venture_ai_002,survival_metric,65,2026-05-14
venture_ai_002,roi,85,2026-05-14
venture_marketplace_003,survival_metric,28,2026-05-14
venture_marketplace_003,roi,-15,2026-05-14""",
        "decisions.json": """{
  "decisions": [
    {
      "venture_id": "venture_hrms_001",
      "decision": "SCALE",
      "capital": 50000,
      "date": "2026-05-14"
    },
    {
      "venture_id": "venture_ai_002",
      "decision": "COMPOUND",
      "capital": 100000,
      "date": "2026-05-14"
    },
    {
      "venture_id": "venture_marketplace_003",
      "decision": "OPTIMIZE",
      "capital": 25000,
      "date": "2026-05-14"
    }
  ]
}"""
    }

    # Write samples to temp dir
    import tempfile
    import os

    tmpdir = tempfile.mkdtemp()
    for filename, content in sample_docs.items():
        filepath = os.path.join(tmpdir, filename)
        with open(filepath, "w") as f:
            f.write(content)

    # Process documents
    print(f"Processing {len(sample_docs)} sample documents...\n")

    for filename in sample_docs.keys():
        filepath = os.path.join(tmpdir, filename)
        doc = preprocessor.process_file(filepath)
        if doc:
            print(f"✓ {doc.filename}")
            print(f"   Format: {doc.format}")
            print(f"   Size: {len(doc.text)} chars")
            print(f"   Chunks: {len(doc.chunks) if doc.chunks else 0}")

    # Show statistics
    stats = preprocessor.stats()
    print(f"\n{'='*70}")
    print(f"📊 Preprocessing Statistics:")
    print(f"   Total Documents: {stats['total_documents']}")
    print(f"   Total Text: {stats['total_text_chars']} chars")
    print(f"   Total Chunks: {stats['total_chunks']}")
    print(f"   By Format: {stats['by_format']}")
    print(f"   Avg Doc Size: {stats['avg_doc_size']} chars")

    # Show sample chunks
    print(f"\n{'='*70}")
    print(f"📋 Sample Text (first document):")
    if preprocessor.processed:
        first_doc = preprocessor.processed[0]
        print(f"\nDocument: {first_doc.filename}")
        print(f"Preview:\n{first_doc.text[:300]}...")

    print(f"\n✅ Preprocessor ready for LightRAG ingestion")
    print(f"   Output format: Clean text + chunks")
    print(f"   Next: Feed to LightRAG for entity extraction")

    # Cleanup
    import shutil
    shutil.rmtree(tmpdir)

    return preprocessor


if __name__ == "__main__":
    preprocessor = demo_preprocessor()
