#!/usr/bin/env python3
"""
SPARKInsight - Lightweight Cross-Agent Memory System
=====================================================
A simple SQLite-based memory system for OpenClaw agents.

Inspired by Hindsight but simplified for easy adoption.

FEATURES:
- Cross-session persistence
- Simple remember/recall API
- Payment verification ($1 USDC)
- 50,000 ORANGE token reward!

USAGE:
    from sparkinsight import remember, recall, Spark, verify_payment

    spark = Spark()
    remember("user_name", "User123")
    name = recall("user_name")

COPY this file to your agent's script directory.
"""

import sqlite3
import json
import os
from datetime import datetime
from typing import Any, Optional, List, Dict

# Configuration
DB_PATH = "./spark.db"
TABLE_NAME = "spark_memories"

# Payment Configuration
DEV_WALLET = "0xEE2B6C840105079874d5980962e874810d05734B"  # Our wallet
PAYMENT_TOKEN = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"  # USDC on Base
PAYMENT_AMOUNT = 1.0  # Minimum $1 USDC

# ORANGE Token Reward
ORANGE_TOKEN = "0x7bdb1b5e11b58324aa0f677a1c25d839572aa96f"
ORANGE_REWARD = 50000  # 50,000 ORANGE per payment

# =============================================================================
# PAYMENT VERIFICATION
# =============================================================================

def verify_payment(tx_hash: str, min_amount: float = PAYMENT_AMOUNT) -> Dict:
    """
    Verify a USDC payment transaction on Base network.
    
    Args:
        tx_hash: Transaction hash from blockchain
        min_amount: Minimum amount required (default: $1)
    
    Returns:
        dict with success status and details
    
    Usage:
        result = verify_payment("0xa1b2c3...", min_amount=1.0)
        if result['verified']:
            print("Payment verified!")
    """
    try:
        from web3 import Web3
        
        # Connect to Base
        w3 = Web3(Web3.HTTPProvider('https://base.publicnode.com'))
        
        if not w3.is_connected():
            return {'verified': False, 'error': 'Cannot connect to Base'}
        
        # Get transaction
        try:
            tx = w3.eth.get_transaction_receipt(tx_hash)
        except:
            return {'verified': False, 'error': 'TX not found or pending'}
        
        if not tx or tx.get('status') != 1:
            return {'verified': False, 'error': 'TX failed or unconfirmed'}
        
        # Check if sent to our wallet
        transfer_signature = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
        
        for log in tx['logs']:
            if len(log.get('topics', [])) >= 3:
                if log['topics'][0] == transfer_signature:
                    # Check recipient
                    to_address = '0x' + log['topics'][2][-40:]
                    
                    if to_address.lower() == DEV_WALLET.lower():
                        # Get amount
                        amount = int(log.get('data', '0x0'), 16) / 10**6  # USDC decimals
                        
                        if amount >= min_amount:
                            return {
                                'verified': True,
                                'amount': amount,
                                'from': '0x' + log['topics'][1][-40:],
                                'tx_hash': tx_hash,
                                'message': f'✅ Verified! ${amount:.2f} USDC received'
                            }
                        else:
                            return {
                                'verified': False, 
                                'amount': amount,
                                'error': f'Amount ${amount:.2f} below minimum ${min_amount}'
                            }
        
        return {'verified': False, 'error': 'TX not sent to our wallet'}
        
    except ImportError:
        return {'verified': False, 'error': 'web3 not installed. pip install web3'}
    except Exception as e:
        return {'verified': False, 'error': str(e)}

# =============================================================================
# MEMORY SYSTEM
# =============================================================================

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database and table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            key TEXT PRIMARY KEY,
            value TEXT,
            tags TEXT,
            created_at TEXT,
            updated_at TEXT
        )
    """)
    
    conn.commit()
    conn.close()

class Spark:
    """
    Main memory manager for SPARKInsight.
    
    Initialize at session start:
        spark = Spark()
    """
    
    def __init__(self, db_path: str = DB_PATH):
        global DB_PATH
        DB_PATH = db_path
        init_db()
    
    def remember(self, key: str, value: Any, tags: Optional[List[str]] = None) -> bool:
        """Store a memory."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            value_json = json.dumps(value)
            tags_json = json.dumps(tags) if tags else None
            
            now = datetime.now().isoformat()
            
            cursor.execute(f"""
                INSERT OR REPLACE INTO {TABLE_NAME} (key, value, tags, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
            """, (key, value_json, tags_json, now, now))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"SPARKInsight Error: {e}")
            return False
    
    def recall(self, key: str) -> Optional[Any]:
        """Retrieve a memory by key."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute(f"""
                SELECT value FROM {TABLE_NAME} WHERE key = ?
            """, (key,))
            
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return json.loads(result['value'])
            return None
            
        except Exception as e:
            print(f"SPARKInsight Error: {e}")
            return None
    
    def search(self, query: str) -> List[Dict]:
        """Search memories by content or tags."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute(f"""
                SELECT key, value, tags FROM {TABLE_NAME}
            """)
            
            results = []
            for row in cursor.fetchall():
                value = json.loads(row['value'])
                tags = json.loads(row['tags']) if row['tags'] else []
                
                query_lower = query.lower()
                value_str = str(value).lower()
                tags_str = " ".join(tags).lower()
                
                if query_lower in value_str or query_lower in tags_str:
                    results.append({
                        'key': row['key'],
                        'value': value,
                        'tags': tags
                    })
            
            conn.close()
            return results
            
        except Exception as e:
            print(f"SPARKInsight Error: {e}")
            return []
    
    def forget(self, key: str) -> bool:
        """Delete a memory by key."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute(f"""
                DELETE FROM {TABLE_NAME} WHERE key = ?
            """, (key,))
            
            deleted = cursor.rowcount > 0
            conn.commit()
            conn.close()
            return deleted
            
        except Exception as e:
            print(f"SPARKInsight Error: {e}")
            return False
    
    def list_all(self) -> List[Dict]:
        """List all stored memories."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute(f"""
                SELECT key, value, tags, created_at, updated_at 
                FROM {TABLE_NAME}
                ORDER BY updated_at DESC
            """)
            
            results = []
            for row in cursor.fetchall():
                results.append({
                    'key': row['key'],
                    'value': json.loads(row['value']),
                    'tags': json.loads(row['tags']) if row['tags'] else [],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                })
            
            conn.close()
            return results
            
        except Exception as e:
            print(f"SPARKInsight Error: {e}")
            return []
    
    def count(self) -> int:
        """Return total number of memories."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
            count = cursor.fetchone()[0]
            
            conn.close()
            return count
            
        except Exception as e:
            print(f"SPARKInsight Error: {e}")
            return 0
    
    def clear(self) -> bool:
        """Clear ALL memories. USE WITH CAUTION!"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute(f"DELETE FROM {TABLE_NAME}")
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"SPARKInsight Error: {e}")
            return False


# Convenience functions
_spark = None

def _get_spark() -> Spark:
    global _spark
    if _spark is None:
        _spark = Spark()
    return _spark

def remember(key: str, value: Any, tags: Optional[List[str]] = None) -> bool:
    """Quick remember function."""
    return _get_spark().remember(key, value, tags)

def recall(key: str) -> Optional[Any]:
    """Quick recall function."""
    return _get_spark().recall(key)

def search(query: str) -> List[Dict]:
    """Quick search function."""
    return _get_spark().search(query)

def forget(key: str) -> bool:
    """Quick forget function."""
    return _get_spark().forget(key)

def list_all() -> List[Dict]:
    """Quick list function."""
    return _get_spark().list_all()

def count() -> int:
    """Quick count function."""
    return _get_spark().count()

def verify_payment_simple(tx_hash: str) -> bool:
    """Simplified payment verification (just returns True/False)."""
    result = verify_payment(tx_hash)
    return result.get('verified', False)


if __name__ == "__main__":
    print("=" * 60)
    print("SPARKInsight - Lightweight Agent Memory + Rewards")
    print("=" * 60)
    print()
    print("Quick Test:")
    
    spark = Spark()
    
    # Store memories
    remember("test_key", "test_value")
    remember("agent_name", "MyAgent")
    remember("user_preference", {"timezone": "UTC"})
    
    # Recall
    print(f"Recall test_key: {recall('test_key')}")
    print(f"Recall agent_name: {recall('agent_name')}")
    print(f"Total memories: {count()}")
    
    print()
    print("Payment Verification:")
    print("  result = verify_payment('0xTX_HASH')")
    print("  if result['verified']:")
    print("      print('✅ Payment verified!')")
    print()
    print("Copy sparkinsight.py to your agent!")
    print("=" * 60)
