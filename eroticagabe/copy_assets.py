import os
import shutil

src_root = "/Users/acebless/Documents/vex-hero-site"
dest_root = "/Users/acebless/Documents/eroticagabe"

# Files/folders to remove from next.js boilerplate
to_remove = [
    "src",
    "public",
    "next.config.ts",
    "eslint.config.mjs",
    "postcss.config.mjs"
]

print("Cleaning up old Next.js boilerplate files...")
for item in to_remove:
    path = os.path.join(dest_root, item)
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        print(f"Removed: {item}")

# Files/folders to copy from vex-hero-site
to_copy = [
    ("src", True),
    ("public", True),
    ("package.json", False),
    ("tsconfig.json", False),
    ("tsconfig.app.json", False),
    ("tsconfig.node.json", False),
    ("vite.config.ts", False),
    ("index.html", False),
    ("tailwind.config.js", False),
    ("postcss.config.js", False)
]

print("Copying Vite+React+Tailwind frontend from vex-hero-site...")
for item, is_dir in to_copy:
    src_path = os.path.join(src_root, item)
    dest_path = os.path.join(dest_root, item)
    
    if os.path.exists(src_path):
        if is_dir:
            shutil.copytree(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)
        print(f"Copied: {item}")
    else:
        print(f"Warning: {item} not found in source")

print("Done!")
