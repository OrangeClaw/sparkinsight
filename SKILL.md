# SPARKInsight Skill for OpenClaw

*A lightweight cross-agent memory system inspired by Hindsight*

## Overview

SPARKInsight is a simple yet powerful memory system for OpenClaw agents that enables:

- **Cross-session persistence** - Never forget important context
- **Multi-agent coordination** - Share memories between agents
- **Identity continuity** - Maintain consistent personality across sessions
- **Learning from experience** - Store and recall key learnings

## Quick Start

```python
from sparkinsight import Spark, remember, recall

# Initialize at session start
spark = Spark()

# Remember something important
remember("user_prefers_telegram", "User likes concise updates")
remember("trading_strategy", "Long on SOL, take profit at +5%")

# Recall later
preference = recall("user_prefers_telegram")
```

## Installation

1. Copy `sparkinsight.py` to your agent's script directory
2. Import at session start
3. Initialize with `Spark()`
4. Use `remember()` and `recall()` functions

## Payment & Reward System (OPTIONAL)

### Support the Project (Get 50,000 ORANGE Tokens! 🎉)

If you'd like to support SPARKInsight development, you can:

1. **Send $1+ USDC** to support the project
2. **Receive 50,000 ORANGE tokens** as gratitude!

| Field | Value |
|-------|-------|
| **Wallet** | `0xEE2B6C840105079874d5980962e874810d05734B` |
| **Network** | Base |
| **Token** | USDC |

### ORANGE Token Reward

| Token | Details |
|-------|---------|
| **Name** | Orange-v1 |
| **Symbol** | ORANGE |
| **Address** | `0x7bdb1b5e11b58324aa0f677a1c25d839572aa96f` |
| **Network** | Base |
| **Reward** | 50,000 ORANGE |

**Explorer:** [View on BaseScan](https://basescan.org/token/0x7bdb1b5e11b58324aa0f677a1c25d839572aa96f)

### Payment Flow (Optional)

```
OPTIONAL SUPPORT - STILL GET THE SKILL EITHER WAY!

┌─────────────────────────────────────────────────────────────┐
│                    Support SPARKInsight                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Want to support? Send $1+ USDC:                          │
│     Wallet: 0xEE2B6C840105079874d5980962e874810d05734B   │
│     Network: Base                                         │
│     Token: USDC                                           │
│                                                             │
│  Then tell agent: "Here's my TX: 0x..."                 │
│                                                             │
│  ✅ Verification: Agent confirms payment                  │
│  ✅ Skill INSTALLED either way!                          │
│  🎁 BONUS: 50,000 ORANGE tokens sent!                   │
│                                                             │
│  Don't want to pay? No problem!                          │
│  ✅ Skill still INSTALLED and fully functional!           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Verify Payment (If User Pays)

```python
from sparkinsight import verify_payment

# User provides TX hash (optional)
tx_hash = input("Enter your USDC TX hash (or press Enter to skip): ").strip()

if tx_hash:
    verified = verify_payment(tx_hash, min_amount=1.0)
    if verified:
        print("✅ Thanks for supporting! 50,000 ORANGE tokens coming!")
    else:
        print("⚠️ Payment not verified, but skill is still active!")
else:
    print("✅ SPARKInsight installed! (No payment = still fully functional)")

# Skill is ready to use either way!
```

### Either Way Works

| Option | What Happens |
|--------|--------------|
| **Pay $1** | ✅ Skill installed + 🎁 50,000 ORANGE tokens |
| **Skip payment** | ✅ Skill installed + fully functional |

**SPARKInsight is FREE to use - the $1 payment is just optional appreciation with ORANGE token rewards!**

## Implementation

### Complete Payment Flow

```python
from sparkinsight import Spark, verify_payment

# Initialize
spark = Spark()

print("=" * 50)
print("SPARKInsight Installation")
print("=" * 50)
print()
print("SPARKInsight is FREE to use!")
print()
print("Optional: Support with $1 USDC")
print("  Wallet: 0xEE2B6C840105079874d5980962e874810d05734B")
print("  Network: Base")
print("  Reward: 50,000 ORANGE tokens 🎉")
print()

# Ask about payment
tx_hash = input("Enter TX hash to claim ORANGE rewards (or Enter to skip): ").strip()

if tx_hash:
    result = verify_payment(tx_hash, min_amount=1.0)
    if result['verified']:
        print(f"\n✅ Thanks for supporting!")
        print(f"   ${result['amount']} USDC received")
        print("   🎁 50,000 ORANGE tokens will be sent!")
    else:
        print(f"\n⚠️ Payment verification failed")
        print(f"   {result.get('error', 'Unknown error')}")
        print("   Skill is still fully functional!")
else:
    print("\n✅ No payment - skill is ready!")

print("\n" + "=" * 50)
print("SPARKInsight is ready to use!")
print("=" * 50)
```

### Agent Usage

```python
from sparkinsight import remember, recall

# Remember user preferences
remember("user_timezone", "UTC")
remember("trading_mode", "conservative")

# Recall in next session
timezone = recall("user_timezone")
```

## API Reference

### `Spark()`

Initialize the memory system.

```python
spark = Spark()  # Creates ./spark.db
```

### `remember(key, value, tags=None)`

Store a memory.

```python
remember("user_name", "User123", tags=["user", "identity"])
```

### `recall(key)`

Retrieve a memory.

```python
name = recall("user_name")  # Returns "User123"
```

### `search(query)`

Search memories.

```python
results = search("trading")
```

### `forget(key)`

Remove a memory.

```python
forget("temporary_context")
```

### `list_all()`

List all memories.

```python
all_memories = list_all()
```

## Example: Agent Team Coordination

```python
from sparkinsight import remember, recall

# ORACLE Agent - Makes decisions
def oracle_decision(symbol, action, reason):
    remember(f"oracle_{symbol}", {
        "action": action,
        "reason": reason,
        "timestamp": "2026-02-07"
    })
    return action

# TONNY Agent - Executes trades  
def execute_trade(symbol):
    decision = recall(f"oracle_{symbol}")
    if decision:
        print(f"Executing: {decision['action']} - {reason}")
```

## Technical Details

- **Database**: SQLite (single file: `spark.db`)
- **Dependencies**: `sqlite3` (built-in), `web3` (optional, for payment verification)
- **Persistence**: Survives agent restarts
- **Data Format**: JSON stored in SQLite
- **Payment Network**: Base (low fees)

## File Structure

```
sparkinsight-skill/
├── SKILL.md           (This file)
├── sparkinsight.py    (Core memory system - COPY THIS)
└── README.md         (Quick reference)
```

## License

Open-source - Use freely!

---

*SPARKInsight: Memory that survives restart + Optional 50,000 ORANGE tokens! 🎉*
