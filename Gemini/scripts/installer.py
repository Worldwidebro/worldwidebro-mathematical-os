#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor

# Define tool details
TOOLS = {
    'claudecode': {
        'name': 'Claude Code',
        'detection': lambda: shutil.which('claude') is not None or os.path.exists(os.path.expanduser('~/.claudecoderc')),
        'destinations': [os.path.expanduser('~/.claudecoderc')],
        'source_file': 'claudecode-instructions.md',
        'install_handler': 'append'
    },
    'copilot': {
        'name': 'GitHub Copilot',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.github')) or os.path.exists(os.path.expanduser('~/.copilot')),
        'destinations': [os.path.expanduser('~/.github/copilot-instructions.md'), '.github/copilot-instructions.md'],
        'source_file': 'copilot-instructions.md',
        'install_handler': 'write'
    },
    'antigravity': {
        'name': 'Antigravity',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.gemini/antigravity')),
        'destinations': [os.path.expanduser('~/.gemini/antigravity/rules/instructions.md'), 'GEMINI.md'],
        'source_file': 'GEMINI.md',
        'install_handler': 'write'
    },
    'gemini-cli': {
        'name': 'Gemini CLI',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.gemini/agents')),
        'destinations': [os.path.expanduser('~/.gemini/agents/instructions.md')],
        'source_file': 'gemini-cli-instructions.md',
        'install_handler': 'write'
    },
    'opencode': {
        'name': 'OpenCode',
        'detection': lambda: shutil.which('opencode') is not None or os.path.exists(os.path.expanduser('~/.opencode')),
        'destinations': [os.path.expanduser('~/.opencode/rules.md')],
        'source_file': 'opencode-instructions.md',
        'install_handler': 'write'
    },
    'openclaw': {
        'name': 'OpenClaw',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.openclaw')),
        'destinations': [os.path.expanduser('~/.openclaw/agency-agents/rules.md')],
        'source_file': 'openclaw-instructions.md',
        'install_handler': 'write'
    },
    'cursor': {
        'name': 'Cursor',
        'detection': lambda: shutil.which('cursor') is not None or os.path.exists(os.path.expanduser('~/.cursor')) or os.path.exists('.cursor'),
        'destinations': ['.cursorrules', '.cursor/rules/ai-boss-os.md'],
        'source_file': 'cursorrules',
        'install_handler': 'write'
    },
    'aider': {
        'name': 'Aider',
        'detection': lambda: shutil.which('aider') is not None,
        'destinations': ['CONVENTIONS.md'],
        'source_file': 'CONVENTIONS.md',
        'install_handler': 'write'
    },
    'windsurf': {
        'name': 'Windsurf',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.windsurf')) or os.path.exists('.windsurfrules'),
        'destinations': ['.windsurfrules'],
        'source_file': 'windsurfrules',
        'install_handler': 'write'
    },
    'qwen-code': {
        'name': 'Qwen Code',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.qwen/agents')),
        'destinations': [os.path.expanduser('~/.qwen/agents/rules.md')],
        'source_file': 'qwen-code-instructions.md',
        'install_handler': 'write'
    },
    'kimi-code': {
        'name': 'Kimi Code',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.config/kimi/agents')),
        'destinations': [os.path.expanduser('~/.config/kimi/agents/rules.md')],
        'source_file': 'kimi-code-instructions.md',
        'install_handler': 'write'
    },
    'codex': {
        'name': 'Codex',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.codex/agents')),
        'destinations': [os.path.expanduser('~/.codex/agents/rules.md')],
        'source_file': 'codex-instructions.md',
        'install_handler': 'write'
    },
    'osaurus': {
        'name': 'Osaurus',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.osaurus/skills')),
        'destinations': [os.path.expanduser('~/.osaurus/skills/rules.md')],
        'source_file': 'osaurus-instructions.md',
        'install_handler': 'write'
    },
    'hermes': {
        'name': 'Hermes',
        'detection': lambda: os.path.exists(os.path.expanduser('~/.hermes/plugins')),
        'destinations': [os.path.expanduser('~/.hermes/plugins/rules.md')],
        'source_file': 'hermes-instructions.md',
        'install_handler': 'write'
    }
}

# Scan system for existing tools
def scan_system():
    detections = {}
    for key, spec in TOOLS.items():
        try:
            detections[key] = spec['detection']()
        except Exception:
            detections[key] = False
    return detections

def install_tool(key, source_dir):
    spec = TOOLS[key]
    src_path = os.path.join(source_dir, spec['source_file'])
    
    if not os.path.exists(src_path):
        print(f"[-] Source file missing: {src_path}. Running converter first...")
        # Try to run converter.py dynamically
        os.system(f"python3 {os.path.join(os.path.dirname(__file__), 'converter.py')} --tool {key}")
        if not os.path.exists(src_path):
            print(f"[!] Error: Could not compile source for {key}")
            return False
            
    with open(src_path, 'r') as f:
        content = f.read()
        
    installed_paths = []
    for dest in spec['destinations']:
        try:
            # Create directories if they do not exist
            dest_dir = os.path.dirname(dest)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir, exist_ok=True)
                
            if spec['install_handler'] == 'append':
                # Avoid appending duplicate blocks
                existing = ""
                if os.path.exists(dest):
                    with open(dest, 'r') as df:
                        existing = df.read()
                if "AI-BOSS-OS" not in existing:
                    with open(dest, 'a') as df:
                        df.write("\n\n# AI-BOSS-OS Rules Integration\n" + content)
                else:
                    # Replace existing integration
                    pass 
            else:
                with open(dest, 'w') as df:
                    df.write(content)
            installed_paths.append(dest)
        except Exception as e:
            print(f"[!] Error writing to {dest}: {e}")
            
    if installed_paths:
        print(f"[+] Installed {spec['name']} integration to: {', '.join(installed_paths)}")
        return True
    return False

# Custom interactive checkbox UI
def run_interactive_ui(detections):
    tool_keys = list(TOOLS.keys())
    selections = {k: detections[k] for k in tool_keys} # Default to detected tools
    
    # Save terminal settings to return to raw mode
    import sys
    import termios
    import tty
    
    def print_menu():
        # Clear screen/lines
        sys.stdout.write("\033[H\033[2J")
        sys.stdout.write("  +------------------------------------------------+\n")
        sys.stdout.write("  |   The Agency -- Tool Installer                 |\n")
        sys.stdout.write("  +------------------------------------------------+\n\n")
        sys.stdout.write("  System scan: [*] = detected on this machine\n\n")
        
        for idx, k in enumerate(tool_keys):
            num = idx + 1
            detect_str = "[*]" if detections[k] else "[ ]"
            select_str = "[x]" if selections[k] else "[ ]"
            sys.stdout.write(f"  {select_str}  {num:2d})  {detect_str}  {TOOLS[k]['name']:<14}\n")
            
        sys.stdout.write("\n  [1-14] toggle   [a] all   [n] none   [d] detected\n")
        sys.stdout.write("  [Enter] install   [q] quit\n")
        sys.stdout.flush()

    fd = sys.stdin.fileno()
    
    buffer = ""
    while True:
        print_menu()
        
        # Read keys
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            
        if ch == '\r' or ch == '\n':
            # Enter: install
            break
        elif ch == 'q' or ch == 'Q':
            print("\nExiting installer.")
            sys.exit(0)
        elif ch == 'a' or ch == 'A':
            for k in tool_keys:
                selections[k] = True
        elif ch == 'n' or ch == 'N':
            for k in tool_keys:
                selections[k] = False
        elif ch == 'd' or ch == 'D':
            for k in tool_keys:
                selections[k] = detections[k]
        elif ch.isdigit():
            buffer += ch
            # If buffer matches option
            val = int(buffer)
            if val >= 1 and val <= len(tool_keys):
                target_key = tool_keys[val - 1]
                selections[target_key] = not selections[target_key]
                buffer = ""
            elif val > len(tool_keys) or len(buffer) >= 2:
                buffer = ""
        else:
            buffer = ""
            
    return [k for k in tool_keys if selections[k]]

def main():
    parser = argparse.ArgumentParser(description="Install tool integration files.")
    parser.add_argument('--no-interactive', action='store_true', help='Run without prompt')
    parser.add_argument('--interactive', action='store_true', help='Force interactive prompt')
    parser.add_argument('--parallel', action='store_true', help='Install files in parallel')
    parser.add_argument('--jobs', type=int, default=4, help='Number of parallel jobs')
    parser.add_argument('--tool', type=str, default='all', help='Target tool name or all')
    args = parser.parse_args()
    
    workspace = '/Users/acebless/Documents/Gemini'
    dist_dir = os.path.join(workspace, 'scripts/dist')
    
    detections = scan_system()
    selected_tools = []
    
    # Decide interactivity
    interactive_mode = not args.no_interactive
    if args.interactive:
        interactive_mode = True
        
    if not sys.stdin.isatty():
        interactive_mode = False
        
    if interactive_mode and args.tool == 'all':
        selected_tools = run_interactive_ui(detections)
    else:
        # Batch installation mode
        if args.tool == 'all':
            selected_tools = [k for k, v in detections.items() if v]
            if not selected_tools:
                # If nothing detected, select all as fallback
                selected_tools = list(TOOLS.keys())
        else:
            if args.tool not in TOOLS:
                print(f"Error: Unknown tool: {args.tool}")
                sys.exit(1)
            selected_tools = [args.tool]
            
    if not selected_tools:
        print("No tools selected for installation.")
        sys.exit(0)
        
    print(f"\nInstalling integration files for: {', '.join([TOOLS[k]['name'] for k in selected_tools])}...")
    
    if args.parallel and len(selected_tools) > 1:
        with ThreadPoolExecutor(max_workers=args.jobs) as executor:
            futures = [executor.submit(install_tool, t, dist_dir) for t in selected_tools]
            for fut in futures:
                fut.result()
    else:
        for t in selected_tools:
            install_tool(t, dist_dir)
            
    print("\nInstallation completed successfully!")

if __name__ == '__main__':
    main()
