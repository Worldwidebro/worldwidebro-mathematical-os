---
id: DOC-02-COMP-009
aliases: ['MACS']
tags: ['compute', 'macs', 'infrastructure']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]] | [[_REGISTRIES/compute_registry.json]]

# Apple Silicon Architecture & Metal Acceleration

> **Authority:** CP-027 | **Status:** LIVE

## Unified Memory Architecture (UMA)
Both primary nodes utilize Apple Silicon's Unified Memory Architecture, enabling zero-copy memory sharing between CPU, GPU, and the Neural Engine.
- **Mac Studio:** 36GB UMA with ~410 GB/s memory bandwidth. Critical for hosting 35B quantized models in memory with high inference speed.
- **MacBook Air:** 16GB UMA with ~100 GB/s memory bandwidth. Used for lightweight reasoning and code compilation.

## Native Acceleration Frameworks
- **Metal 3 / MPS:** Native GPU tensor evaluation used by `exo` and PyTorch.
- **Apple AMX / Accelerate:** High-speed BLAS operations for vector math.

## Connected Documents & Registries
- Domain Hub: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|COMPUTE]]
- Master Infrastructure: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
- Core Registry: [[_REGISTRIES/compute_registry.json]]
- [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|STORAGE]]
- [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|NETWORK]]
- [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|RUNTIME]]
- [[_REGISTRIES/compute_registry.json|compute_registry.json]]
