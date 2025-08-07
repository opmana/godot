#!/usr/bin/env python3
"""
Simple Blockchain Example

A basic example showing how to use the Proof of Work blockchain implementation.
"""

import sys
import os

# Add the src directory to the path so we can import the blockchain module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from blockchain import Blockchain


def main():
    """Run a simple blockchain example."""
    print("🚀 Simple Blockchain Example")
    print("=" * 50)
    
    # Create a new blockchain with difficulty 3
    print("Creating blockchain with difficulty 3...")
    blockchain = Blockchain(difficulty=3)
    
    # Add some transactions
    print("\nAdding transactions...")
    blockchain.add_transaction("Alice", "Bob", 100.0, "Payment for services")
    blockchain.add_transaction("Bob", "Charlie", 50.0, "Split payment")
    blockchain.add_transaction("Charlie", "David", 25.0, "Further split")
    
    print(f"Added {len(blockchain.pending_transactions)} transactions")
    
    # Mine the block
    print("\n⛏️  Mining block...")
    mined_block = blockchain.mine_pending_transactions("miner1")
    
    print(f"✅ Block mined! Hash: {mined_block.hash[:20]}...")
    print(f"   Nonce: {mined_block.nonce}")
    print(f"   Transactions: {len(mined_block.transactions)}")
    
    # Add more transactions
    print("\nAdding more transactions...")
    blockchain.add_transaction("David", "Alice", 10.0, "Refund")
    blockchain.add_transaction("Alice", "Eve", 20.0, "New payment")
    
    # Mine another block
    print("\n⛏️  Mining second block...")
    mined_block2 = blockchain.mine_pending_transactions("miner2")
    
    print(f"✅ Second block mined! Hash: {mined_block2.hash[:20]}...")
    print(f"   Nonce: {mined_block2.nonce}")
    
    # Check chain validity
    print(f"\n🔍 Chain valid: {blockchain.is_chain_valid()}")
    print(f"📊 Total blocks: {len(blockchain.chain)}")
    
    # Show balances
    print("\n💰 Balances:")
    addresses = ["Alice", "Bob", "Charlie", "David", "Eve", "miner1", "miner2"]
    for address in addresses:
        balance = blockchain.get_balance(address)
        print(f"   {address}: {balance:>8.2f}")
    
    # Show transaction history for Alice
    print(f"\n📜 Transaction history for Alice:")
    alice_history = blockchain.get_transaction_history("Alice")
    for i, tx in enumerate(alice_history, 1):
        print(f"   {i}. {tx['sender']} -> {tx['recipient']}: {tx['amount']:.2f}")
        if tx.get('data'):
            print(f"      Data: {tx['data']}")
    
    print("\n🎉 Example completed successfully!")


if __name__ == "__main__":
    main()