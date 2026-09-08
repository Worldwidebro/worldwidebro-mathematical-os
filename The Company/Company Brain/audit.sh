#!/bin/bash

echo "=== AUDIT: Company Brain Completeness ==="
echo ""

# Check which domains have no README
echo "📋 DOMAINS WITHOUT README.md:"
for domain in 0{0..9}-* {1,2,3,4}{0..9}-*; do
  if [ -d "$domain" ] && [ ! -f "$domain/README.md" ]; then
    echo "  ❌ $domain"
  fi
done

echo ""
echo "📋 DOMAINS WITH README.md:"
ls -1d */README.md 2>/dev/null | sed 's|/README.md||' | wc -l | xargs echo "  ✅ Count:"

echo ""
echo "🔗 BROKEN WIKI LINKS IN INDEX.md:"
grep -o '\[\[[^]]*\]\]' INDEX.md | sed 's/\[\[//;s/\]\]//' | sort | uniq > /tmp/index_links.txt

for link in $(cat /tmp/index_links.txt); do
  # Skip infrastructure/registries/pipelines/docs (they exist)
  if [[ "$link" =~ ^_ ]]; then
    [ -d "$link" ] && echo "  ✅ $link" || echo "  ❌ $link (missing)"
  else
    # Check domain folders
    if [ ! -d "$link" ]; then
      echo "  ❌ $link (domain missing)"
    fi
  fi
done | grep "❌"

echo ""
echo "📁 EMPTY DOMAINS (only .keep files):"
for domain in 0{0..9}-* {1,2,3,4}{0..9}-*; do
  if [ -d "$domain" ]; then
    count=$(find "$domain" -type f ! -name ".keep" | wc -l)
    if [ $count -eq 0 ]; then
      echo "  ⚠️  $domain (empty)"
    fi
  fi
done | head -20

echo ""
echo "🔧 INFRASTRUCTURE COMPLETENESS:"
for dir in _INFRASTRUCTURE/*; do
  if [ -d "$dir" ]; then
    count=$(find "$dir" -type f ! -name ".keep" | wc -l)
    echo "  $(basename $dir): $count files"
  fi
done

echo ""
echo "📊 REGISTRIES COMPLETENESS:"
for dir in _REGISTRIES/*; do
  if [ -d "$dir" ]; then
    count=$(find "$dir" -type f ! -name ".keep" | wc -l)
    echo "  $(basename $dir): $count files"
  fi
done

