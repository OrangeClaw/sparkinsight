---
name: spark
description: "SPARK: Self-healing, Proactive, Autonomous, Reinforced, Knowledgeable - Complete agent architecture for persistent memory, self-improvement, and autonomous operation"
emoji: 🧠
requires:
  bins: []
  env: []
  config: []
---

# SPARK Architecture for AI Agents

*A complete system for building agents that remember, learn, and improve autonomously*

## What is SPARK?

SPARK is an architecture pattern for AI agents that solves the fundamental problem: **agents that forget everything between sessions.**

```
┌─────────────────────────────────────────────────────────────┐
│                    SPARK ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌───────┐ │
│   │  SENSE  │───▶│ THINK   │───▶│  ACT   │───▶│LEARN  │ │
│   └─────────┘    └─────────┘    └─────────┘    └───────┘ │
│        │              │              │              │       │
│        └──────────────┴──────────────┴──────────────┘       │
│                         │                                    │
│                    ┌────▼────┐                               │
│                    │ MEMORY  │                               │
│                    └─────────┘                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## The 5 Pillars

| Pillar | Description |
|--------|-------------|
| **S**elf-Healing | Auto-diagnose and fix issues |
| **P**roactive | Anticipate needs before asked |
| **A**utonomous | Operate without constant supervision |
| **R**einforced | Learn from decisions and feedback |
| **K**nowledgeable | Remember context across sessions |

## Quick Start

```python
# Initialize memory at session start
from auto_retain import auto, remember, recall

# Memory loads automatically from previous sessions
auto  # Loads 7 days of memories

# Remember important context
remember("user_timezone", "Asia/Singapore")
remember("trading_strategy", "Conservative, max 5% per trade")

# Always available in future sessions
```

## 3-Layer Memory System

### Layer 1: Daily Logs
- Raw activity logs stored in `memory/YYYY-MM-DD.md`
- Captured automatically via auto_retain
- Includes: decisions, events, learnings

### Layer 2: Curated Memory
- `MEMORY.md` — distilled wisdom
- Manually updated with important insights
- Survives session restarts

### Layer 3: Session Handoff
- 24-hour continuity for active work
- Auto-saves at 3:30 AM daily
- Resumes seamlessly after restart

## Auto-Retain: Automatic Event Capture

```python
from auto_retain import trade_opened, trade_closed, signal_generated, system_event

# Events captured automatically - no manual logging needed
trade_opened("SOL/USDC", "LONG", 4.50, 100, "Bullish setup")
trade_closed("SOL/USDC", "LONG", 4.50, 100, 4.80, 6.67)
signal_generated("BTC", 67000, "SHORT")
system_event("Server", "Memory upgraded to 16GB")
```

## Session Handoff

```python
# Save current work context
python3 scripts/session_handoff.py save

# Resume from anywhere
python3 scripts/session_handoff.py load
# Returns: {"active_work": "...", "pending_tasks": [...]}
```

## Self-Healing Audit

Run hourly to keep system healthy:

```bash
python3 scripts/unified_self_healing_audit.py
```

Checks:
- Cron jobs running
- Gateway responsive
- Memory efficiency
- Auto-compaction
- Session cleanup

## Execution Discipline Protocol

Avoid common agent mistakes:

```bash
python3 scripts/execution_discipline.py check "deploy to production"
```

8 Rules:
1. **Objective Lock** — Define "done" first
2. **Task Decomposition** — Break into subtasks
3. **Assumption Declaration** — Flag what you assume
4. **Single-Layer Execution** — One step at a time
5. **Loop Prevention** — Same task 3x → stop and ask
6. **Completion Validation** — Did you actually finish?
7. **Failure Handling** — State where/why blocked
8. **Token Discipline** — No redundant reasoning

## Integration: MoltLaunch

Deploy your agent to earn:

```bash
# Register agent
npx moltlaunch register --name "YourAgent" --symbol AGENT

# Add services
npx moltlaunch gig create --title "Training" --price 0.003 --delivery "24h"

# Check inbox
npx moltlaunch inbox
```

## File Structure

```
/workspace/
├── scripts/
│   ├── auto_retain.py      # Memory auto-load
│   ├── session_handoff.py  # 24h continuity
│   ├── execution_discipline.py  # Protocol
│   └── unified_self_healing_audit.py
├── memory/
│   └── YYYY-MM-DD.md      # Daily logs
├── MEMORY.md               # Curated wisdom
└── SKILL.md               # This file
```

## Why SPARK Works

| Problem | SPARK Solution |
|---------|-----------------|
| Forgets everything | 3-layer memory persists |
| No learning | Auto-retain captures decisions |
| Breaks silently | Self-healing audit catches issues |
| Repeats mistakes | Execution discipline prevents loops |
| Can't earn | MoltLaunch integration |

## Technical Details

- **Memory**: SQLite + Markdown files
- **Persistence**: 7-day rolling window
- **Handoff**: 24-hour retention
- **Audit**: Hourly cron
- **Cost**: Free (uses built-in tools)

## Get Started

1. Copy `auto_retain.py` to your scripts
2. Add to session startup: `from auto_retain import auto; auto`
3. Set up hourly self-healing cron
4. Optional: Deploy to MoltLaunch to earn

---

*SPARK: Agents that remember, learn, and improve — forever.*
