#!/usr/bin/env python3
"""
Blockchain Demo Script

This script demonstrates the Proof of Work blockchain implementation
with various features including mining, transactions, and validation.
"""

import time
from blockchain import Blockchain


def print_blockchain_info(blockchain: Blockchain) -> None:
    """Print information about the current state of the blockchain."""
    print("\n" + "="*60)
    print("BLOCKCHAIN STATUS")
    print("="*60)
    print(f"Total blocks: {len(blockchain.chain)}")
    print(f"Current difficulty: {blockchain.difficulty}")
    print(f"Pending transactions: {len(blockchain.pending_transactions)}")
    print(f"Chain valid: {blockchain.is_chain_valid()}")
    print("="*60)


def print_block_details(block: 'Block') -> None:
    """Print detailed information about a specific block."""
    print(f"\nBlock #{block.index}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {time.ctime(block.timestamp)}")
    print(f"Nonce: {block.nonce}")
    print(f"Transactions: {len(block.transactions)}")
    
    if block.transactions:
        print("Transactions:")
        for i, tx in enumerate(block.transactions, 1):
            print(f"  {i}. {tx['sender']} -> {tx['recipient']}: {tx['amount']}")
            if tx.get('data'):
                print(f"     Data: {tx['data']}")


def print_balances(blockchain: Blockchain, addresses: list) -> None:
    """Print the balance of specified addresses."""
    print("\n" + "="*40)
    print("BALANCES")
    print("="*40)
    for address in addresses:
        balance = blockchain.get_balance(address)
        print(f"{address}: {balance:.2f}")


def demo_basic_mining():
    """Demonstrate basic mining functionality."""
    print("\n" + "="*60)
    print("DEMO 1: BASIC MINING")
    print("="*60)
    
    # Create a new blockchain with difficulty 4
    blockchain = Blockchain(difficulty=4)
    
    print("Created new blockchain with difficulty 4")
    print_blockchain_info(blockchain)
    
    # Mine some blocks
    print("\nMining blocks...")
    for i in range(3):
        print(f"\nMining block {i+1}...")
        blockchain.mine_pending_transactions("miner1")
        print_blockchain_info(blockchain)


def demo_transactions():
    """Demonstrate transaction functionality."""
    print("\n" + "="*60)
    print("DEMO 2: TRANSACTIONS")
    print("="*60)
    
    blockchain = Blockchain(difficulty=3)
    
    # Add some transactions
    print("Adding transactions...")
    blockchain.add_transaction("Alice", "Bob", 50.0, "Payment for services")
    blockchain.add_transaction("Bob", "Charlie", 25.0, "Split payment")
    blockchain.add_transaction("Charlie", "Alice", 10.0, "Refund")
    
    print(f"Added {len(blockchain.pending_transactions)} pending transactions")
    
    # Mine the block with transactions
    print("\nMining block with transactions...")
    blockchain.mine_pending_transactions("miner1")
    
    print_blockchain_info(blockchain)
    
    # Print balances
    addresses = ["Alice", "Bob", "Charlie", "miner1"]
    print_balances(blockchain, addresses)


def demo_chain_validation():
    """Demonstrate blockchain validation."""
    print("\n" + "="*60)
    print("DEMO 3: CHAIN VALIDATION")
    print("="*60)
    
    blockchain = Blockchain(difficulty=2)
    
    # Add some transactions and mine
    blockchain.add_transaction("Alice", "Bob", 100.0)
    blockchain.mine_pending_transactions("miner1")
    
    blockchain.add_transaction("Bob", "Charlie", 50.0)
    blockchain.mine_pending_transactions("miner2")
    
    print("Created blockchain with 2 blocks")
    print(f"Chain valid: {blockchain.is_chain_valid()}")
    
    # Demonstrate tampering detection
    print("\nDemonstrating tampering detection...")
    if len(blockchain.chain) > 1:
        # Tamper with a block
        tampered_block = blockchain.chain[1]
        original_hash = tampered_block.hash
        tampered_block.transactions[0]['amount'] = 999.0  # Tamper with amount
        
        print(f"Tampered with block {tampered_block.index}")
        print(f"Chain valid after tampering: {blockchain.is_chain_valid()}")
        
        # Restore the original hash to continue demo
        tampered_block.hash = original_hash


def demo_difficulty_adjustment():
    """Demonstrate mining with different difficulty levels."""
    print("\n" + "="*60)
    print("DEMO 4: DIFFICULTY COMPARISON")
    print("="*60)
    
    difficulties = [2, 3, 4]
    
    for difficulty in difficulties:
        print(f"\nTesting difficulty {difficulty}...")
        blockchain = Blockchain(difficulty=difficulty)
        
        start_time = time.time()
        blockchain.mine_pending_transactions("miner1")
        mining_time = time.time() - start_time
        
        print(f"Difficulty {difficulty}: {mining_time:.2f} seconds")
        print(f"Block hash: {blockchain.get_latest_block().hash}")


def demo_persistence():
    """Demonstrate saving and loading blockchain."""
    print("\n" + "="*60)
    print("DEMO 5: PERSISTENCE")
    print("="*60)
    
    # Create and populate blockchain
    blockchain = Blockchain(difficulty=3)
    blockchain.add_transaction("Alice", "Bob", 100.0)
    blockchain.mine_pending_transactions("miner1")
    
    print("Original blockchain:")
    print_blockchain_info(blockchain)
    
    # Save to file
    filename = "blockchain_demo.json"
    blockchain.save_to_file(filename)
    print(f"\nSaved blockchain to {filename}")
    
    # Load from file
    loaded_blockchain = Blockchain.load_from_file(filename)
    print("\nLoaded blockchain from file:")
    print_blockchain_info(loaded_blockchain)
    
    print(f"Loaded chain valid: {loaded_blockchain.is_chain_valid()}")


def demo_transaction_history():
    """Demonstrate transaction history functionality."""
    print("\n" + "="*60)
    print("DEMO 6: TRANSACTION HISTORY")
    print("="*60)
    
    blockchain = Blockchain(difficulty=2)
    
    # Add various transactions
    blockchain.add_transaction("Alice", "Bob", 50.0, "Payment 1")
    blockchain.mine_pending_transactions("miner1")
    
    blockchain.add_transaction("Bob", "Charlie", 25.0, "Payment 2")
    blockchain.add_transaction("Alice", "David", 30.0, "Payment 3")
    blockchain.mine_pending_transactions("miner2")
    
    # Get transaction history for Alice
    alice_history = blockchain.get_transaction_history("Alice")
    
    print(f"Transaction history for Alice ({len(alice_history)} transactions):")
    for i, tx in enumerate(alice_history, 1):
        print(f"  {i}. Block {tx['block_index']}: {tx['sender']} -> {tx['recipient']}: {tx['amount']}")
        if tx.get('data'):
            print(f"     Data: {tx['data']}")


def main():
    """Run all demos."""
    print("PROOF OF WORK BLOCKCHAIN DEMO")
    print("="*60)
    
    try:
        demo_basic_mining()
        demo_transactions()
        demo_chain_validation()
        demo_difficulty_adjustment()
        demo_persistence()
        demo_transaction_history()
        
        print("\n" + "="*60)
        print("ALL DEMOS COMPLETED SUCCESSFULLY!")
        print("="*60)
        
    except Exception as e:
        print(f"\nError during demo: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()