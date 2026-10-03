import re
with open('FILESYSTEM_AND_DISKMAP_MASTER_ONTOLOGY.md', 'r') as f:
    diskmap = f.read()

diskmap = diskmap.replace(
    '[[MAC_AIR]]\n    ├── [[INTERNAL_SSD]]\n    └── [[T7_SHIELD]]',
    '[[MAC_AIR]] (or [[MAC_STUDIO]])\n    ├── [[INTERNAL_SSD]]\n    └── [[T7_SHIELD]] (Roaming - currently on Mac Studio)'
)
with open('FILESYSTEM_AND_DISKMAP_MASTER_ONTOLOGY.md', 'w') as f:
    f.write(diskmap)
print("Updated diskmap")
