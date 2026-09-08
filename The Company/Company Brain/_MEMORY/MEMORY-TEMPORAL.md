# MEMORY-TEMPORAL — Time-Awareness and Validity Windows

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-LIFECYCLE|MEMORY-LIFECYCLE]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-TEM-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. The Temporal Fallacy

Agents frequently make catastrophic errors by treating memory as timeless:
> *"The port is 8000 because I read that in a sprint note from 8 months ago."*

To prevent this, every memory atom in Company Brain is bound by **strict temporal metadata**.

---

## 2. Temporal Fields

Every memory node contains:
- `created_at`: Exact UTC ISO 8601 timestamp of record creation.
- `observed_at`: When the physical or runtime state was observed.
- `last_verified_at`: When an empirical test confirmed the state.
- `validity_ttl_seconds`: Time-to-live before transitioning to `STALE`.
- `superseded_at`: Timestamp when a newer record rendered this record historical.
- `historical_interval`: Valid start and end dates (`[t_start, t_end]`).

---

## 3. The Temporal Query Filter

Before acting on any retrieved memory, the agent must evaluate:
1. **Is this fact currently within its validity window?**
2. **Has any event occurred since `last_verified_at` that would invalidate this fact?**
3. **If `current_time - last_verified_at > validity_ttl`, trigger an immediate live verification probe before proceeding.**
