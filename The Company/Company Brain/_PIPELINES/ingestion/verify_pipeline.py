#!/usr/bin/env python3
"""
Pipeline Verification & Testing Script
Tests Phase 2.1-2.2 without requiring GitHub authentication.
"""

import os
import sys
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

# Color output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def print_check(msg, passed):
    status = f"{Colors.GREEN}✓{Colors.RESET}" if passed else f"{Colors.RED}✗{Colors.RESET}"
    print(f"{status} {msg}")

def print_info(msg):
    print(f"ℹ {msg}")

def print_section(title):
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print(f"{'=' * 60}\n")

class PipelineVerifier:
    """Verify Phase 2 pipeline structure and functionality."""

    def __init__(self):
        self.base_dir = '/tmp/company-brain-repos'
        self.passed = 0
        self.failed = 0
        self.warnings = 0

    def check_directory_structure(self) -> bool:
        """Verify required directories exist."""
        print_section("1. DIRECTORY STRUCTURE")

        required_dirs = [
            'raw',
            'normalized',
            'logs'
        ]

        for dir_name in required_dirs:
            dir_path = os.path.join(self.base_dir, dir_name)
            exists = os.path.isdir(dir_path)
            print_check(f"Directory: {dir_name}/", exists)
            if exists:
                self.passed += 1
            else:
                self.failed += 1

        return self.failed == 0

    def check_script_files(self) -> bool:
        """Verify required scripts exist and are valid."""
        print_section("2. SCRIPT FILES")

        required_scripts = [
            ('github_ingest.py', 'Phase 2.1 ingestion'),
            ('normalize_repos.py', 'Phase 2.2 normalization'),
            ('verify_pipeline.py', 'Pipeline verification'),
            ('run_phases.sh', 'Orchestration'),
        ]

        for script, desc in required_scripts:
            path = os.path.join(self.base_dir, script)
            exists = os.path.isfile(path)
            executable = os.access(path, os.X_OK) if exists else False

            print_check(f"{script} exists", exists)
            if exists:
                self.passed += 1
            else:
                self.failed += 1

            if exists:
                print_check(f"  → {desc}", True)
                self.passed += 1

        return self.failed == 0

    def check_python_syntax(self) -> bool:
        """Check Python scripts for syntax errors."""
        print_section("3. PYTHON SYNTAX VALIDATION")

        import py_compile

        python_files = [
            'github_ingest.py',
            'normalize_repos.py',
        ]

        all_valid = True
        for filename in python_files:
            path = os.path.join(self.base_dir, filename)
            try:
                py_compile.compile(path, doraise=True)
                print_check(f"Syntax: {filename}", True)
                self.passed += 1
            except py_compile.PyCompileError as e:
                print_check(f"Syntax: {filename}", False)
                print(f"  → Error: {e}")
                self.failed += 1
                all_valid = False

        return all_valid

    def check_dependencies(self) -> bool:
        """Check required Python dependencies."""
        print_section("4. PYTHON DEPENDENCIES")

        required = ['requests', 'json', 'logging', 'datetime']
        all_available = True

        for module in required:
            if module == 'json' or module == 'logging' or module == 'datetime':
                # Built-in modules
                available = True
            else:
                try:
                    __import__(module)
                    available = True
                except ImportError:
                    available = False
                    all_available = False

            status = "built-in" if module in ['json', 'logging', 'datetime'] else "available"
            print_check(f"Module: {module} ({status})", available)
            if available:
                self.passed += 1
            else:
                self.failed += 1

        if not all_available:
            print_info("Install missing dependencies: pip install requests")

        return all_available

    def generate_test_data(self, count: int = 100) -> str:
        """Generate mock GitHub repository data for testing."""
        print_section(f"5. TEST DATA GENERATION ({count} repos)")

        languages = ['Python', 'TypeScript', 'Go', 'Rust', 'JavaScript', 'Java', 'C++', None]
        licenses = ['MIT', 'Apache-2.0', 'GPL-3.0', 'BSD-3-Clause', None]

        repos = []
        now = datetime.now()

        for i in range(count):
            created = now - timedelta(days=random.randint(365, 3650))
            pushed = now - timedelta(days=random.randint(0, 300))
            updated = now - timedelta(days=random.randint(0, 180))

            repo = {
                'id': 100000000 + i,
                'name': f'repo-{i:04d}',
                'full_name': f'user{i%10}/repo-{i:04d}',
                'url': f'https://github.com/user{i%10}/repo-{i:04d}',
                'api_url': f'https://api.github.com/repos/user{i%10}/repo-{i:04d}',
                'description': f'Test repository {i}' if random.random() > 0.3 else None,
                'stars': random.randint(0, 10000),
                'forks': random.randint(0, 1000),
                'open_issues': random.randint(0, 100),
                'language': random.choice(languages),
                'license': random.choice(licenses),
                'topics': random.sample(['ai', 'ml', 'python', 'testing', 'devops'], k=random.randint(0, 3)),
                'is_private': False,
                'is_archived': random.random() < 0.1,
                'is_fork': random.random() < 0.2,
                'created_at': created.isoformat() + 'Z',
                'updated_at': updated.isoformat() + 'Z',
                'pushed_at': pushed.isoformat() + 'Z',
                'homepage': f'https://example{i}.com' if random.random() > 0.8 else None,
                'default_branch': 'main',
            }
            repos.append(repo)

        # Add intentional duplicates for testing
        if len(repos) > 10:
            repos.append(repos[0])  # Exact duplicate
            repos.append(repos[5])  # Exact duplicate

        output_data = {
            'metadata': {
                'ingestion_timestamp': datetime.now().isoformat(),
                'total_repos': len(repos),
                'version': '1.0',
                'test_data': True
            },
            'repositories': repos
        }

        output_path = os.path.join(self.base_dir, 'raw', 'test-github-starred.json')

        try:
            with open(output_path, 'w') as f:
                json.dump(output_data, f, indent=2, default=str)

            file_size = os.path.getsize(output_path) / 1024  # KB
            print_check(f"Generated test data: {count} repos", True)
            print_info(f"Saved to: {output_path} ({file_size:.1f} KB)")
            self.passed += 1

            return output_path
        except Exception as e:
            print_check(f"Generate test data", False)
            print(f"  → Error: {e}")
            self.failed += 1
            return None

    def test_normalization(self, input_path: str) -> bool:
        """Test normalization logic on test data."""
        print_section("6. NORMALIZATION TEST")

        try:
            # Import normalizer
            sys.path.insert(0, self.base_dir)
            from normalize_repos import RepositoryNormalizer

            normalizer = RepositoryNormalizer(input_path)

            # Load and normalize
            if not normalizer.load_raw_data():
                print_check("Load test data", False)
                self.failed += 1
                return False

            print_check("Load test data", True)
            self.passed += 1

            # Run normalization
            if not normalizer.normalize():
                print_check("Run normalization", False)
                self.failed += 1
                return False

            print_check("Run normalization", True)
            self.passed += 1

            # Verify output
            print_info(f"Input repos: {normalizer.dedup_stats['total_input']}")
            print_info(f"Duplicates removed: {normalizer.dedup_stats['duplicates_removed']}")
            print_info(f"Archived flagged: {normalizer.dedup_stats['archived_flagged']}")
            print_info(f"Final output: {normalizer.dedup_stats['final_count']}")

            # Save test output
            output_path = os.path.join(self.base_dir, 'normalized', 'test-deduplicated.json')
            if normalizer.save_normalized(output_path):
                print_check("Save normalized output", True)
                self.passed += 1
            else:
                print_check("Save normalized output", False)
                self.failed += 1

            return True

        except Exception as e:
            print_check("Normalization test", False)
            print(f"  → Error: {e}")
            self.failed += 1
            return False

    def check_output_format(self) -> bool:
        """Verify output JSON format."""
        print_section("7. OUTPUT FORMAT VALIDATION")

        test_normalized = os.path.join(self.base_dir, 'normalized', 'test-deduplicated.json')

        if not os.path.exists(test_normalized):
            print_check("Test output exists", False)
            self.failed += 1
            return False

        try:
            with open(test_normalized, 'r') as f:
                data = json.load(f)

            # Verify structure
            has_metadata = 'metadata' in data
            has_repos = 'repositories' in data

            print_check("Has 'metadata' key", has_metadata)
            if has_metadata:
                self.passed += 1
            else:
                self.failed += 1

            print_check("Has 'repositories' key", has_repos)
            if has_repos:
                self.passed += 1
            else:
                self.failed += 1

            if has_metadata:
                meta = data['metadata']
                print_check("Metadata has 'total_repositories'", 'total_repositories' in meta)
                if 'total_repositories' in meta:
                    self.passed += 1
                else:
                    self.failed += 1

            if has_repos:
                print_check(f"Repositories list is valid", isinstance(data['repositories'], list))
                if isinstance(data['repositories'], list):
                    self.passed += 1
                else:
                    self.failed += 1

                if len(data['repositories']) > 0:
                    first_repo = data['repositories'][0]
                    has_flags = '_flags' in first_repo
                    print_check("Repository entries have '_flags'", has_flags)
                    if has_flags:
                        self.passed += 1
                    else:
                        self.failed += 1

            return True

        except Exception as e:
            print_check("Output format validation", False)
            print(f"  → Error: {e}")
            self.failed += 1
            return False

    def run_verification(self, generate_test=True):
        """Run complete verification suite."""
        print(f"\n{Colors.GREEN}PHASE 2 PIPELINE VERIFICATION{Colors.RESET}\n")

        # Core checks
        self.check_directory_structure()
        self.check_script_files()
        self.check_python_syntax()
        self.check_dependencies()

        # Test data and normalization (optional)
        if generate_test:
            test_data_path = self.generate_test_data(count=100)
            if test_data_path:
                self.test_normalization(test_data_path)
                self.check_output_format()

        # Summary
        self.print_summary()

    def print_summary(self):
        """Print verification summary."""
        print_section("VERIFICATION SUMMARY")

        total = self.passed + self.failed

        if self.failed == 0:
            status = f"{Colors.GREEN}PASSED{Colors.RESET}"
        else:
            status = f"{Colors.YELLOW}PARTIAL{Colors.RESET}" if self.failed < 5 else f"{Colors.RED}FAILED{Colors.RESET}"

        print(f"Status: {status}")
        print(f"Checks: {self.passed} passed, {self.failed} failed (total: {total})")

        if self.failed == 0:
            print(f"\n{Colors.GREEN}Pipeline is ready for Phase 2.1 execution{Colors.RESET}")
            print("\nNext steps:")
            print("1. Set GitHub token: export GITHUB_TOKEN=ghp_xxx")
            print("2. Run ingestion: python3 github_ingest.py")
            print("3. Run normalization: python3 normalize_repos.py")
            print("4. Or use orchestration: ./run_phases.sh")
        else:
            print(f"\n{Colors.RED}Fix the errors above before running Phase 2{Colors.RESET}")

        print()


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Verify Phase 2 Pipeline')
    parser.add_argument('--generate-test-data', action='store_true',
                       help='Generate and test on mock data')
    parser.add_argument('--test-count', type=int, default=100,
                       help='Number of mock repos to generate')

    args = parser.parse_args()

    verifier = PipelineVerifier()
    verifier.run_verification(generate_test=args.generate_test_data)

    return 0 if verifier.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
