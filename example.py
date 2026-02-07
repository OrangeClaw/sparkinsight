#!/usr/bin/env python3
"""
SPARKInsight Usage Examples
============================
Copy `sparkinsight.py` to your agent's directory.
"""

import sys
sys.path.insert(0, '.')
from sparkinsight import remember, recall, search, list_all, Spark

# =============================================================================
# PATTERN 1: Session Startup
# =============================================================================

def session_startup():
    """Initialize memory and load user preferences"""
    spark = Spark()
    
    user_name = recall("user_name")
    trading_mode = recall("trading_mode") or "conservative"
    risk_tolerance = recall("risk_tolerance") or "medium"
    
    print(f"Session started!")
    print(f"User: {user_name or 'Unknown'}")
    print(f"Trading mode: {trading_mode}")
    print(f"Risk tolerance: {risk_tolerance}")

# =============================================================================
# PATTERN 2: Trading Decisions
# =============================================================================

def oracle_decision(symbol, action, reason, confidence):
    """Store trading decision"""
    remember(f"oracle_{symbol}", {
        "action": action,
        "reason": reason,
        "confidence": confidence
    })

def tonny_execution(symbol):
    """Recall trading decision"""
    decision = recall(f"oracle_{symbol}")
    if decision:
        print(f"Executing: {decision['action']} - {decision['reason']}")

# =============================================================================
# PATTERN 3: Payment Processing with ORANGE Rewards
# =============================================================================

import os

def setup_wallet():
    """Create agent wallet for receiving payments"""
    from sparkinsight import create_wallet
    
    wallet = create_wallet()
    if wallet:
        print("=" * 50)
        print("Wallet Created!")
        print("=" * 50)
        print(f"Address: {wallet['address']}")
        print("Configure:")
        print(f"export SPARKINSIGHT_AGENT_WALLET=\"{wallet['address']}\"")
        print(f"export SPARKINSIGHT_AGENT_PRIVATE_KEY=\"{wallet['private_key']}\"")

def request_payment_and_reward():
    """Request payment and send ORANGE reward"""
    from sparkinsight import process_payment
    
    agent_wallet = os.environ.get('SPARKINSIGHT_AGENT_WALLET', '')
    
    if not agent_wallet:
        print("⚠️ Run setup_wallet() first!")
        return
    
    print("=" * 50)
    print("SPARKInsight Payment + ORANGE Token Reward")
    print("=" * 50)
    print(f"Your wallet: {agent_wallet}")
    print("Send $1+ USDC, then enter:")
    tx_hash = input("TX Hash: ")
    payer_address = input("Your wallet: ")
    
    result = process_payment(tx_hash, payer_address)
    
    if result['success']:
        print(f"\n✅ Complete!")
        print(f"   USDC TX: {result['usdc_tx']}")
        if result.get('orange_tx'):
            print(f"   🎉 ORANGE TX: {result['orange_tx']}")
            print(f"   🎉 {result['orange_amount']:,} ORANGE sent!")

# =============================================================================
# PATTERN 4: Team Memory
# =============================================================================

class TeamMember:
    """Base class for team agents with shared memory"""
    
    def __init__(self, name):
        self.name = name
    
    def remember_team(self, key, value):
        remember(f"team_{key}", {"from": self.name, "value": value})
    
    def recall_team(self, key):
        return recall(f"team_{key}")

# =============================================================================
# PATTERN 5: Session Summary
# =============================================================================

def session_summary():
    """Generate session summary"""
    all_mem = list_all()
    print("=" * 50)
    print("SESSION SUMMARY")
    print("=" * 50)
    print(f"Total memories: {len(all_mem)}")
    for mem in all_mem[:5]:
        print(f"  - {mem['key']}")
    print("=" * 50)

# =============================================================================
# RUN DEMO
# =============================================================================

if __name__ == "__main__":
    print("SPARKInsight Examples")
    print("=" * 50)
    
    print("\n1. Session Startup:")
    session_startup()
    
    print("\n2. Trading Decision:")
    oracle_decision("SOL", "LONG", "Bullish", 75)
    tonny_execution("SOL")
    
    print("\n3. Wallet Setup (run first!):")
    print("   setup_wallet()")
    
    print("\n4. Payment with ORANGE Rewards:")
    print("   request_payment_and_reward()")
    
    print("\n5. Team Memory:")
    print("   TeamMember('AgentA')")
    
    print("\n6. Session Summary:")
    session_summary()
    
    print("\n" + "=" * 50)
    print("Copy sparkinsight.py to your agent!")
    print("🎉 Get 50,000 ORANGE tokens when you pay!")
    print("=" * 50)
