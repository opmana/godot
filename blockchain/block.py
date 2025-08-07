import hashlib
import json
import time
from typing import List, Dict, Any


class Block:
    def __init__(self, index: int, transactions: List[Dict], timestamp: float = None, 
                 previous_hash: str = "0", nonce: int = 0):
        """
        Initialize a new block in the blockchain.
        
        Args:
            index: Position of the block in the blockchain
            transactions: List of transaction dictionaries
            timestamp: Time when block was created (defaults to current time)
            previous_hash: Hash of the previous block
            nonce: Number used in proof of work
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.
        
        Returns:
            Hexadecimal string representation of the block hash
        """
        block_string = json.dumps({
            'index': self.index,
            'transactions': self.transactions,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True)
        
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty: int) -> None:
        """
        Mine the block by finding a nonce that produces a hash with the required difficulty.
        
        Args:
            difficulty: Number of leading zeros required in the hash
        """
        target = "0" * difficulty
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the block to a dictionary for serialization.
        
        Returns:
            Dictionary representation of the block
        """
        return {
            'index': self.index,
            'transactions': self.transactions,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Block':
        """
        Create a Block instance from a dictionary.
        
        Args:
            data: Dictionary containing block data
            
        Returns:
            Block instance
        """
        block = cls(
            index=data['index'],
            transactions=data['transactions'],
            timestamp=data['timestamp'],
            previous_hash=data['previous_hash'],
            nonce=data['nonce']
        )
        block.hash = data['hash']
        return block
    
    def __str__(self) -> str:
        """String representation of the block."""
        return f"Block #{self.index} - Hash: {self.hash[:10]}... - Nonce: {self.nonce}"
    
    def __repr__(self) -> str:
        """Detailed string representation of the block."""
        return f"Block(index={self.index}, hash='{self.hash[:10]}...', nonce={self.nonce})"