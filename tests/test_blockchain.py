#!/usr/bin/env python3
"""
Tests for the Proof of Work Blockchain Implementation
"""

import pytest
import tempfile
import os
from src.blockchain import Blockchain, Block


class TestBlock:
    """Test cases for the Block class."""
    
    def test_block_creation(self):
        """Test basic block creation."""
        transactions = [{"sender": "Alice", "recipient": "Bob", "amount": 50.0}]
        block = Block(1, transactions, previous_hash="test_hash")
        
        assert block.index == 1
        assert block.transactions == transactions
        assert block.previous_hash == "test_hash"
        assert block.nonce == 0
        assert block.hash is not None
    
    def test_block_hash_calculation(self):
        """Test that block hash is calculated correctly."""
        block1 = Block(1, [], previous_hash="hash1")
        block2 = Block(1, [], previous_hash="hash1")
        
        # Same inputs should produce same hash
        assert block1.hash == block2.hash
    
    def test_block_mining(self):
        """Test block mining with different difficulties."""
        block = Block(1, [], previous_hash="test_hash")
        original_hash = block.hash
        
        # Mine with difficulty 2
        block.mine_block(2)
        
        # Hash should start with "00"
        assert block.hash.startswith("00")
        assert block.hash != original_hash
        assert block.nonce > 0
    
    def test_block_serialization(self):
        """Test block serialization and deserialization."""
        transactions = [{"sender": "Alice", "recipient": "Bob", "amount": 50.0}]
        original_block = Block(1, transactions, previous_hash="test_hash")
        original_block.mine_block(2)
        
        # Serialize
        block_dict = original_block.to_dict()
        
        # Deserialize
        new_block = Block.from_dict(block_dict)
        
        # Should be identical
        assert new_block.index == original_block.index
        assert new_block.transactions == original_block.transactions
        assert new_block.previous_hash == original_block.previous_hash
        assert new_block.nonce == original_block.nonce
        assert new_block.hash == original_block.hash


class TestBlockchain:
    """Test cases for the Blockchain class."""
    
    def test_blockchain_creation(self):
        """Test blockchain creation with genesis block."""
        blockchain = Blockchain(difficulty=3)
        
        assert len(blockchain.chain) == 1
        assert blockchain.chain[0].index == 0
        assert blockchain.difficulty == 3
        assert len(blockchain.pending_transactions) == 0
    
    def test_add_transaction(self):
        """Test adding transactions to the blockchain."""
        blockchain = Blockchain()
        
        # Add a transaction
        block_index = blockchain.add_transaction("Alice", "Bob", 50.0, "Test payment")
        
        assert len(blockchain.pending_transactions) == 1
        assert blockchain.pending_transactions[0]["sender"] == "Alice"
        assert blockchain.pending_transactions[0]["recipient"] == "Bob"
        assert blockchain.pending_transactions[0]["amount"] == 50.0
        assert blockchain.pending_transactions[0]["data"] == "Test payment"
        assert block_index == 1  # Next block index
    
    def test_mine_pending_transactions(self):
        """Test mining a block with pending transactions."""
        blockchain = Blockchain(difficulty=2)
        
        # Add transactions
        blockchain.add_transaction("Alice", "Bob", 50.0)
        blockchain.add_transaction("Bob", "Charlie", 25.0)
        
        # Mine the block
        mined_block = blockchain.mine_pending_transactions("miner1")
        
        assert mined_block.index == 1
        assert len(mined_block.transactions) == 2
        assert mined_block.hash.startswith("00")  # Difficulty 2
        assert len(blockchain.pending_transactions) == 1  # Mining reward transaction
    
    def test_chain_validation(self):
        """Test blockchain validation."""
        blockchain = Blockchain(difficulty=2)
        
        # Add transactions and mine
        blockchain.add_transaction("Alice", "Bob", 50.0)
        blockchain.mine_pending_transactions("miner1")
        
        blockchain.add_transaction("Bob", "Charlie", 25.0)
        blockchain.mine_pending_transactions("miner2")
        
        # Chain should be valid
        assert blockchain.is_chain_valid()
        
        # Tamper with a block
        if len(blockchain.chain) > 1:
            blockchain.chain[1].transactions[0]["amount"] = 999.0
            assert not blockchain.is_chain_valid()
    
    def test_get_balance(self):
        """Test balance calculation."""
        blockchain = Blockchain(difficulty=2)
        
        # Add transactions and mine
        blockchain.add_transaction("Alice", "Bob", 50.0)
        blockchain.mine_pending_transactions("miner1")
        
        blockchain.add_transaction("Bob", "Charlie", 25.0)
        blockchain.mine_pending_transactions("miner2")
        
        # Check balances
        alice_balance = blockchain.get_balance("Alice")
        bob_balance = blockchain.get_balance("Bob")
        charlie_balance = blockchain.get_balance("Charlie")
        miner1_balance = blockchain.get_balance("miner1")
        miner2_balance = blockchain.get_balance("miner2")
        
        assert alice_balance == -50.0
        assert bob_balance == 25.0  # 50 - 25
        assert charlie_balance == 25.0
        assert miner1_balance == 10.0  # Mining reward
        assert miner2_balance == 10.0  # Mining reward
    
    def test_get_transaction_history(self):
        """Test transaction history retrieval."""
        blockchain = Blockchain(difficulty=2)
        
        # Add transactions and mine
        blockchain.add_transaction("Alice", "Bob", 50.0, "Payment 1")
        blockchain.mine_pending_transactions("miner1")
        
        blockchain.add_transaction("Bob", "Charlie", 25.0, "Payment 2")
        blockchain.mine_pending_transactions("miner2")
        
        # Get Alice's transaction history
        alice_history = blockchain.get_transaction_history("Alice")
        
        assert len(alice_history) == 1
        assert alice_history[0]["sender"] == "Alice"
        assert alice_history[0]["recipient"] == "Bob"
        assert alice_history[0]["amount"] == 50.0
        assert alice_history[0]["data"] == "Payment 1"
    
    def test_persistence(self):
        """Test saving and loading blockchain."""
        blockchain = Blockchain(difficulty=2)
        
        # Add some data
        blockchain.add_transaction("Alice", "Bob", 50.0)
        blockchain.mine_pending_transactions("miner1")
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_filename = f.name
        
        try:
            blockchain.save_to_file(temp_filename)
            
            # Load from file
            loaded_blockchain = Blockchain.load_from_file(temp_filename)
            
            # Should be identical
            assert len(loaded_blockchain.chain) == len(blockchain.chain)
            assert loaded_blockchain.difficulty == blockchain.difficulty
            assert loaded_blockchain.is_chain_valid()
            
        finally:
            # Clean up
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
    
    def test_get_block_by_index(self):
        """Test retrieving blocks by index."""
        blockchain = Blockchain(difficulty=2)
        
        # Add transactions and mine
        blockchain.add_transaction("Alice", "Bob", 50.0)
        blockchain.mine_pending_transactions("miner1")
        
        # Get blocks
        genesis_block = blockchain.get_block_by_index(0)
        block_1 = blockchain.get_block_by_index(1)
        invalid_block = blockchain.get_block_by_index(999)
        
        assert genesis_block is not None
        assert genesis_block.index == 0
        assert block_1 is not None
        assert block_1.index == 1
        assert invalid_block is None


def test_integration():
    """Integration test for the complete blockchain workflow."""
    blockchain = Blockchain(difficulty=3)
    
    # Add multiple transactions
    blockchain.add_transaction("Alice", "Bob", 100.0, "Initial payment")
    blockchain.add_transaction("Bob", "Charlie", 50.0, "Split payment")
    blockchain.add_transaction("Charlie", "David", 25.0, "Further split")
    
    # Mine the block
    mined_block = blockchain.mine_pending_transactions("miner1")
    
    # Add more transactions
    blockchain.add_transaction("David", "Alice", 10.0, "Refund")
    blockchain.mine_pending_transactions("miner2")
    
    # Verify the chain
    assert blockchain.is_chain_valid()
    assert len(blockchain.chain) == 3  # Genesis + 2 mined blocks
    
    # Check balances
    assert blockchain.get_balance("Alice") == -90.0  # -100 + 10
    assert blockchain.get_balance("Bob") == 50.0     # 100 - 50
    assert blockchain.get_balance("Charlie") == 25.0  # 50 - 25
    assert blockchain.get_balance("David") == 15.0    # 25 - 10
    assert blockchain.get_balance("miner1") == 10.0   # Mining reward
    assert blockchain.get_balance("miner2") == 10.0   # Mining reward


if __name__ == "__main__":
    pytest.main([__file__])