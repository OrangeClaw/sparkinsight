# SPARK Architecture

Lightweight cross-agent memory system for OpenClaw

## Overview

SPARK = Self-Healing, Proactive, Autonomous, Reinforced, Knowledgeable

A complete architecture for building AI agents that:
- Remember context across sessions
- Learn from decisions
- Self-heal when issues arise
- Operate autonomously
- Earn via integrations

## Quick Start

```python
from auto_retain import auto, remember, recall

auto  # Load memories from previous sessions
remember("key", "value")  # Store important context
value = recall("key")  # Retrieve later
```

## 5 Pillars

| Pillar | Function |
|--------|----------|
| Self-Healing | Auto-diagnose & fix |
| Proactive | Anticipate needs |
| Autonomous | Run without supervision |
| Reinforced | Learn from feedback |
| Knowledgeable | Persistent memory |

## Memory Layers

1. **Daily Logs** — `memory/YYYY-MM-DD.md`
2. **Curated** — `MEMORY.md`  
3. **Session Handoff** — 24h continuity

## Scripts

- `auto_retain.py` — Memory system
- `session_handoff.py` — Continuity
- `execution_discipline.py` — Protocol
- `unified_self_healing_audit.py` — Health checks

## License

Open-source

---

🧠 Memory that survives restart
