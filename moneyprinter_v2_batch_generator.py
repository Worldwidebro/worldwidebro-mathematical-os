#!/usr/bin/env python3
"""
MoneyPrinter V2 Batch Video Generator for Construction Ventures

Generates short-form videos for construction/trade ventures using:
- Venture-repo linkage data (WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv)
- Construction sector ventures (con-001 through con-015)
- MoneyPrinter V2's video generation pipeline

Output: videos/{venture_id}_{venture_name}_{timestamp}.mp4
"""

import sys
import os
import csv
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Add MoneyPrinterV2 to path
MONEYPRINTER_PATH = Path("/Users/acebless/MoneyPrinterV2")
sys.path.insert(0, str(MONEYPRINTER_PATH))

class ConstructionVideoGenerator:
    def __init__(self):
        self.docs_dir = Path("/Users/acebless/Documents")
        self.linkage_file = self.docs_dir / "WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data/WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv"
        self.output_dir = self.docs_dir / "moneyprinter-output"
        self.moneyprinter_dir = MONEYPRINTER_PATH

        self.output_dir.mkdir(exist_ok=True, parents=True)

        # Construction sector venture IDs (con-001 through con-015)
        self.construction_ventures = self._load_construction_ventures()

    def _load_construction_ventures(self) -> Dict[str, Dict]:
        """Load construction ventures from linkage CSV"""
        ventures = {}

        if not self.linkage_file.exists():
            print(f"❌ Linkage file not found: {self.linkage_file}")
            return ventures

        with open(self.linkage_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                venture_id = row.get('venture_id', '').strip()
                venture_name = row.get('venture_name', '').strip()
                sector = row.get('sector', '').strip()

                # Filter for construction-related ventures (sector = 'con')
                if sector.lower() == 'con' and venture_name:
                    ventures[venture_id] = {
                        'venture_id': venture_id,
                        'venture_name': venture_name,
                        'sector': sector,
                        'tier': row.get('tier', ''),
                        'required_capabilities': row.get('required_capabilities', ''),
                        'top_repo_1': row.get('top_repo_1', ''),
                        'top_repo_1_match': row.get('top_repo_1_match_pct', ''),
                    }

        return ventures

    def _generate_video_script(self, venture: Dict) -> str:
        """Generate a promotional script for the venture"""
        name = venture['venture_name']
        sector = venture['sector']

        scripts = {
            "Home Renovation Services": f"Transform Your Home with {name}. Expert renovations. Professional results. Click link to learn more.",
            "Roofing Company": f"Protect Your Home with {name}. Quality roofing services. Free inspections. Contact us today.",
            "Plumbing Services": f"Urgent plumbing issues? {name} is here 24/7. Fast response. Expert technicians. Your trusted plumber.",
            "Electrical Services": f"Need electrical work? {name} specializes in safe, code-compliant installations. Licensed & insured.",
            "HVAC Services": f"Stay comfortable year-round with {name}. Heating, cooling, maintenance. Professional service guaranteed.",
            "Painting Services": f"Transform any space with {name}. Interior & exterior painting. Expert craftsmanship. Free estimates.",
            "Flooring Services": f"Beautiful floors start with {name}. Hardwood, tile, laminate. Professional installation. Quality guaranteed.",
            "Landscaping Services": f"Create your dream outdoor space with {name}. Design, installation, maintenance. Trusted local expert.",
        }

        return scripts.get(name, f"Discover {name}. Premium {sector} services. Your satisfaction guaranteed.")

    def _generate_video_metadata(self, venture: Dict) -> Dict:
        """Create metadata for MoneyPrinter V2 video generation"""
        return {
            "venture_id": venture['venture_id'],
            "title": venture['venture_name'],
            "description": f"Professional {venture['sector']} services by {venture['venture_name']}",
            "script": self._generate_video_script(venture),
            "duration": "30-60",
            "music_type": "professional",
            "subtitle_style": "modern",
            "video_type": "promotional",
            "target_platform": "youtube_shorts",
            "quality": "1080p",
            "created_at": datetime.now().isoformat(),
        }

    def generate_batch(self, limit: Optional[int] = None) -> List[str]:
        """Generate videos for construction ventures"""
        generated_videos = []

        if not self.construction_ventures:
            print("⚠️  No construction ventures found in linkage file")
            return generated_videos

        ventures_to_process = list(self.construction_ventures.values())
        if limit:
            ventures_to_process = ventures_to_process[:limit]

        print(f"📹 Generating videos for {len(ventures_to_process)} construction ventures...")
        print("")

        for i, venture in enumerate(ventures_to_process, 1):
            print(f"[{i}/{len(ventures_to_process)}] {venture['venture_name']}")

            # Generate metadata
            metadata = self._generate_video_metadata(venture)

            # Create venture-specific output directory
            venture_output_dir = self.output_dir / venture['venture_id']
            venture_output_dir.mkdir(exist_ok=True, parents=True)

            # Save metadata
            metadata_file = venture_output_dir / "metadata.json"
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)

            # Log entry
            log_entry = {
                "venture_id": venture['venture_id'],
                "venture_name": venture['venture_name'],
                "status": "queued",
                "metadata_file": str(metadata_file),
                "timestamp": datetime.now().isoformat(),
            }

            # Save log
            log_file = venture_output_dir / "generation_log.json"
            with open(log_file, 'w') as f:
                json.dump(log_entry, f, indent=2)

            print(f"   ✅ Metadata saved: {metadata_file}")
            print(f"   📋 Log saved: {log_file}")
            print(f"   📝 Script: {metadata['script'][:60]}...")
            print("")

            generated_videos.append(str(venture_output_dir))

        return generated_videos

    def create_execution_script(self):
        """Create shell script to run MoneyPrinter V2 for generated metadata"""
        script_content = f'''#!/bin/bash
# Execute MoneyPrinter V2 video generation for prepared ventures

OUTPUT_DIR="{self.output_dir}"
MONEYPRINTER_DIR="{self.moneyprinter_dir}"

echo "🎬 Starting MoneyPrinter V2 batch video generation..."
echo ""

# Count preparation files
VENTURE_COUNT=$(find "$OUTPUT_DIR" -name "metadata.json" | wc -l)
echo "📹 Found $VENTURE_COUNT ventures ready for video generation"
echo ""

# Run MoneyPrinter V2 main.py with batch mode
cd "$MONEYPRINTER_DIR"

# Create batch config file
cat > /tmp/mp_batch_config.json <<'EOF'
{{
  "batch_mode": true,
  "input_dir": "$OUTPUT_DIR",
  "output_format": "mp4",
  "quality": "1080p",
  "target_platform": "youtube_shorts",
  "parallel_jobs": 2
}}
EOF

# Execute MoneyPrinter V2
python3 src/main.py --config /tmp/mp_batch_config.json

echo ""
echo "✅ Video generation complete!"
echo "📂 Check output: $OUTPUT_DIR"
'''

        script_file = self.docs_dir / "execute_moneyprinter_batch.sh"
        with open(script_file, 'w') as f:
            f.write(script_content)

        os.chmod(script_file, 0o755)
        print(f"✅ Execution script created: {script_file}")
        return script_file

def main():
    generator = ConstructionVideoGenerator()

    print("=" * 60)
    print("MoneyPrinter V2 Batch Video Generator")
    print("=" * 60)
    print("")

    # Load and display construction ventures
    if generator.construction_ventures:
        print(f"🏗️  Found {len(generator.construction_ventures)} construction ventures:")
        for vid, v in list(generator.construction_ventures.items())[:5]:
            print(f"   • {v['venture_name']} (Tier {v['tier']})")
        if len(generator.construction_ventures) > 5:
            print(f"   ... and {len(generator.construction_ventures) - 5} more")
        print("")
    else:
        print("⚠️  No construction ventures found")
        return

    # Generate batch
    generated = generator.generate_batch(limit=5)

    print(f"📊 Summary:")
    print(f"   ✅ Metadata prepared: {len(generated)}")
    print(f"   📂 Output dir: {generator.output_dir}")
    print("")

    # Create execution script
    exec_script = generator.create_execution_script()

    print(f"🚀 Next step:")
    print(f"   bash {exec_script}")
    print("")

if __name__ == "__main__":
    main()
