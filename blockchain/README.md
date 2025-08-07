# Proof of Work Blockchain Implementation

A complete and functional Proof of Work (PoW) blockchain implementation in Python. This implementation includes all the core features of a blockchain system with a focus on educational clarity and practical usability.

## Features

### Core Blockchain Features
- **Proof of Work Consensus**: Mining blocks with configurable difficulty
- **Block Structure**: Complete block implementation with hash linking
- **Transaction System**: Support for multiple transactions per block
- **Chain Validation**: Comprehensive validation of blockchain integrity
- **Balance Tracking**: Calculate balances for any address
- **Transaction History**: Retrieve complete transaction history for addresses

### Advanced Features
- **Persistence**: Save and load blockchain to/from JSON files
- **Serialization**: Full serialization/deserialization support
- **Tampering Detection**: Automatic detection of blockchain tampering
- **Mining Rewards**: Built-in mining reward system
- **Configurable Difficulty**: Adjustable mining difficulty levels

## Architecture

### Block Structure
Each block contains:
- **Index**: Position in the blockchain
- **Timestamp**: When the block was created
- **Transactions**: List of transaction data
- **Previous Hash**: Hash of the previous block
- **Nonce**: Number used in proof of work
- **Hash**: SHA-256 hash of the block

### Transaction Structure
Each transaction contains:
- **Sender**: Address of the sender
- **Recipient**: Address of the recipient
- **Amount**: Transaction amount
- **Data**: Optional transaction data
- **Timestamp**: When the transaction was created

## Installation

No external dependencies required! This implementation uses only Python standard library modules.

```bash
# Clone or download the blockchain directory
cd blockchain

# Run the demo
python demo.py
```

## Usage

### Basic Usage

```python
from blockchain import Blockchain

# Create a new blockchain
blockchain = Blockchain(difficulty=4)

# Add transactions
blockchain.add_transaction("Alice", "Bob", 50.0, "Payment for services")
blockchain.add_transaction("Bob", "Charlie", 25.0, "Split payment")

# Mine a block
blockchain.mine_pending_transactions("miner1")

# Check balances
alice_balance = blockchain.get_balance("Alice")
bob_balance = blockchain.get_balance("Bob")

# Validate the chain
is_valid = blockchain.is_chain_valid()
```

### Advanced Usage

```python
# Save blockchain to file
blockchain.save_to_file("my_blockchain.json")

# Load blockchain from file
loaded_blockchain = Blockchain.load_from_file("my_blockchain.json")

# Get transaction history
alice_history = blockchain.get_transaction_history("Alice")

# Get specific block
block = blockchain.get_block_by_index(1)
```

## Demo Script

The included `demo.py` script demonstrates all features:

```bash
python demo.py
```

The demo covers:
1. **Basic Mining**: Creating and mining blocks
2. **Transactions**: Adding and processing transactions
3. **Chain Validation**: Validating blockchain integrity
4. **Difficulty Comparison**: Testing different difficulty levels
5. **Persistence**: Saving and loading blockchain data
6. **Transaction History**: Retrieving transaction history

## API Reference

### Blockchain Class

#### Constructor
```python
Blockchain(difficulty: int = 4)
```

#### Methods
- `add_transaction(sender, recipient, amount, data="")`: Add a transaction
- `mine_pending_transactions(miner_address)`: Mine a new block
- `is_chain_valid()`: Validate the entire blockchain
- `get_balance(address)`: Get balance for an address
- `get_transaction_history(address)`: Get transaction history
- `get_block_by_index(index)`: Get block by index
- `save_to_file(filename)`: Save blockchain to file
- `load_from_file(filename)`: Load blockchain from file

### Block Class

#### Constructor
```python
Block(index, transactions, timestamp=None, previous_hash="0", nonce=0)
```

#### Methods
- `calculate_hash()`: Calculate block hash
- `mine_block(difficulty)`: Mine the block
- `to_dict()`: Convert to dictionary
- `from_dict(data)`: Create from dictionary

## Proof of Work Algorithm

The implementation uses a simple but effective PoW algorithm:

1. **Target Calculation**: Creates a target string of leading zeros
2. **Nonce Increment**: Incrementally tries different nonce values
3. **Hash Verification**: Checks if the resulting hash meets the target
4. **Difficulty Adjustment**: Configurable difficulty (number of leading zeros)

Example with difficulty 4:
- Target: "0000"
- Valid hash: "0000a1b2c3d4e5f6..."
- Invalid hash: "0001a2b3c4d5e6f7..."

## Security Features

### Tampering Detection
The blockchain automatically detects tampering by:
- Verifying block hashes match their content
- Checking previous hash references
- Validating proof of work requirements

### Immutability
- Each block's hash depends on all previous blocks
- Changing any block invalidates all subsequent blocks
- Previous hash linking prevents insertion of fake blocks

## Performance Considerations

### Mining Performance
- Higher difficulty = longer mining time
- Exponential relationship between difficulty and time
- Recommended difficulty: 2-4 for testing, 4-6 for production

### Memory Usage
- All blocks stored in memory
- Consider database storage for large chains
- Transaction history can be memory-intensive

## Extending the Implementation

### Possible Enhancements
1. **Network Layer**: Add P2P networking
2. **Web API**: Create REST API interface
3. **Database Storage**: Use SQLite/PostgreSQL for persistence
4. **Enhanced Cryptography**: Add digital signatures
5. **Smart Contracts**: Implement basic smart contract functionality
6. **Wallet Integration**: Add wallet creation and management

### Adding New Features
The modular design makes it easy to extend:
- Add new transaction types
- Implement different consensus mechanisms
- Add block rewards or fees
- Create custom validation rules

## Testing

Run the demo script to test all functionality:

```bash
python demo.py
```

The demo will test:
- Block creation and mining
- Transaction processing
- Chain validation
- Persistence
- Error handling

## License

This implementation is provided for educational purposes. Feel free to use, modify, and extend as needed.

## Contributing

Contributions are welcome! Areas for improvement:
- Performance optimizations
- Additional security features
- Network layer implementation
- Web interface
- Documentation improvements

## Troubleshooting

### Common Issues

1. **Slow Mining**: Reduce difficulty for testing
2. **Memory Issues**: Consider limiting chain size for large demos
3. **File Permissions**: Ensure write permissions for persistence features

### Performance Tips

- Use difficulty 2-3 for quick testing
- Limit transaction count per block for large demos
- Consider clearing old blocks for long-running systems

## Educational Value

This implementation is designed to be:
- **Readable**: Clear, well-documented code
- **Educational**: Demonstrates blockchain concepts
- **Practical**: Actually functional and usable
- **Extensible**: Easy to modify and extend

Perfect for learning blockchain concepts, prototyping ideas, or as a foundation for more complex systems.