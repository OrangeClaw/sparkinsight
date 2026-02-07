# SPARKInsight

*A lightweight cross-agent memory system for OpenClaw*

## Free to Use! Optional Support with ORANGE Rewards

```
┌─────────────────────────────────────────────────────────────────┐
│           SPARKInsight - Optional Payment Flow                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SPARKInsight is FREE to use!                                   │
│                                                                 │
│  OPTIONAL: Support with $1 USDC → Get 50,000 ORANGE tokens!   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │  Wallet: 0xEE2B6C840105079874d5980962e874810d05734B      │ │
│  │  Network: Base                                             │ │
│  │  Reward: 50,000 ORANGE tokens 🎉                         │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│  Either way: ✅ SKILL INSTALLED + FULLY FUNCTIONAL!           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Start

```bash
cp sparkinsight.py /your/agent/

from sparkinsight import remember, recall, verify_payment

spark = Spark()
remember("user_name", "User123")
name = recall("user_name")
```

## Optional Payment

```python
from sparkinsight import verify_payment

# Optional - skip if you don't want to pay
tx_hash = input("Enter TX to claim 50,000 ORANGE (or Enter to skip): ").strip()

if tx_hash:
    result = verify_payment(tx_hash, min_amount=1.0)
    if result['verified']:
        print("✅ Thanks! 50,000 ORANGE tokens coming!")
    else:
        print("⚠️ Verification failed - but skill works anyway!")
else:
    print("✅ No payment - skill is ready!")

# Skill works either way! ✅
```

## ORANGE Token Reward

| Token | Details |
|-------|---------|
| **Name** | Orange-v1 |
| **Symbol** | ORANGE |
| **Address** | `0x7bdb1b5e11b58324aa0f677a1c25d839572aa96f` |
| **Network** | Base |
| **Reward** | 50,000 ORANGE |

**Explorer:** [View on BaseScan](https://basescan.org/token/0x7bdb1b5e11b58324aa0f677a1c25d839572aa96f)

## Files

```
sparkinsight-skill/
├── SKILL.md           # Full documentation
├── sparkinsight.py    # Core system (COPY THIS)
└── README.md         # This file
```

## License

Open-source - Use freely!

---

*Memory + Optional 50,000 ORANGE tokens! 🎉*
