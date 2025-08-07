import json
import time
from typing import List, Dict, Any, Optional
from .block import Block


class Blockchain:
    def __init__(self, difficulty: int = 4):
        """
        Initialize a new blockchain.
        
        Args:
            difficulty: Number of leading zeros required for proof of work
        """
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.pending_transactions: List[Dict] = []
        self.mining_reward = 10  # Reward for mining a block
        
        # Create the genesis block
        self.create_genesis_block()
    
    def create_genesis_block(self) -> None:
        """Create the first block in the blockchain (genesis block)."""
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> Block:
        """Get the most recent block in the chain."""
        return self.chain[-1]
    
    def add_transaction(self, sender: str, recipient: str, amount: float, 
                       data: str = "") -> int:
        """
        Add a new transaction to the pending transactions list.
        
        Args:
            sender: Address of the sender
            recipient: Address of the recipient
            amount: Amount to transfer
            data: Additional transaction data
            
        Returns:
            Index of the block that will contain this transaction
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'data': data,
            'timestamp': time.time()
        }
        
        self.pending_transactions.append(transaction)
        return self.get_latest_block().index + 1
    
    def mine_pending_transactions(self, miner_address: str) -> Block:
        """
        Mine a new block with pending transactions.
        
        Args:
            miner_address: Address of the miner who will receive the reward
            
        Returns:
            The newly mined block
        """
        # Create a new block with pending transactions
        block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )
        
        # Mine the block
        start_time = time.time()
        block.mine_block(self.difficulty)
        mining_time = time.time() - start_time
        
        print(f"Block mined! Hash: {block.hash}")
        print(f"Mining time: {mining_time:.2f} seconds")
        
        # Add the block to the chain
        self.chain.append(block)
        
        # Reset pending transactions and add mining reward
        self.pending_transactions = [
            {
                'sender': "BLOCKCHAIN_REWARD",
                'recipient': miner_address,
                'amount': self.mining_reward,
                'data': f"Reward for mining block #{block.index}",
                'timestamp': time.time()
            }
        ]
        
        return block
    
    def is_chain_valid(self) -> bool:
        """
        Validate the entire blockchain.
        
        Returns:
            True if the blockchain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check if the current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash in block {i}")
                return False
            
            # Check if the previous hash reference is correct
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash reference in block {i}")
                return False
            
            # Check if the block has been properly mined
            if current_block.hash[:self.difficulty] != "0" * self.difficulty:
                print(f"Block {i} has not been properly mined")
                return False
        
        return True
    
    def get_balance(self, address: str) -> float:
        """
        Calculate the balance of a given address.
        
        Args:
            address: The address to check balance for
            
        Returns:
            Current balance of the address
        """
        balance = 0.0
        
        for block in self.chain:
            for transaction in block.transactions:
                if transaction['sender'] == address:
                    balance -= transaction['amount']
                if transaction['recipient'] == address:
                    balance += transaction['amount']
        
        return balance
    
    def get_block_by_index(self, index: int) -> Optional[Block]:
        """
        Get a block by its index.
        
        Args:
            index: Index of the block to retrieve
            
        Returns:
            Block at the specified index or None if not found
        """
        if 0 <= index < len(self.chain):
            return self.chain[index]
        return None
    
    def get_transaction_history(self, address: str) -> List[Dict]:
        """
        Get all transactions involving a specific address.
        
        Args:
            address: The address to get transaction history for
            
        Returns:
            List of transactions involving the address
        """
        transactions = []
        
        for block in self.chain:
            for transaction in block.transactions:
                if (transaction['sender'] == address or 
                    transaction['recipient'] == address):
                    transaction_copy = transaction.copy()
                    transaction_copy['block_index'] = block.index
                    transaction_copy['block_hash'] = block.hash
                    transactions.append(transaction_copy)
        
        return transactions
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the blockchain to a dictionary for serialization.
        
        Returns:
            Dictionary representation of the blockchain
        """
        return {
            'chain': [block.to_dict() for block in self.chain],
            'difficulty': self.difficulty,
            'pending_transactions': self.pending_transactions,
            'mining_reward': self.mining_reward
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Blockchain':
        """
        Create a Blockchain instance from a dictionary.
        
        Args:
            data: Dictionary containing blockchain data
            
        Returns:
            Blockchain instance
        """
        blockchain = cls(difficulty=data['difficulty'])
        blockchain.chain = [Block.from_dict(block_data) for block_data in data['chain']]
        blockchain.pending_transactions = data['pending_transactions']
        blockchain.mining_reward = data['mining_reward']
        return blockchain
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the blockchain to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'Blockchain':
        """
        Load a blockchain from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            Blockchain instance
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)
    
    def __str__(self) -> str:
        """String representation of the blockchain."""
        return f"Blockchain with {len(self.chain)} blocks, difficulty: {self.difficulty}"
    
    def __repr__(self) -> str:
        """Detailed string representation of the blockchain."""
        return f"Blockchain(blocks={len(self.chain)}, difficulty={self.difficulty})"