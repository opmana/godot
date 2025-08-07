# Proof of Work Blockchain Implementation

A complete and functional Proof of Work (PoW) blockchain implementation in Python. This implementation includes all the core features of a blockchain system with a focus on educational clarity and practical usability.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🚀 Features

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

## 📦 Installation

### From Source
```bash
# Clone the repository
git clone https://github.com/yourusername/pow-blockchain.git
cd pow-blockchain

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Direct Usage
No external dependencies required! This implementation uses only Python standard library modules.

```bash
# Navigate to the project directory
cd pow-blockchain

# Run the demo
python examples/demo.py
```

## 🏗️ Project Structure

```
pow-blockchain/
├── src/
│   └── blockchain/
│       ├── __init__.py      # Package initialization
│       ├── block.py         # Block class implementation
│       └── blockchain.py    # Main blockchain class
├── examples/
│   └── demo.py             # Comprehensive demo script
├── tests/                  # Test files (to be added)
├── requirements.txt        # Dependencies
├── setup.py              # Package setup
└── README.md             # This file
```

## 🎯 Quick Start

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

## 🎮 Demo Script

The included demo script demonstrates all features:

```bash
python examples/demo.py
```

The demo covers:
1. **Basic Mining**: Creating and mining blocks
2. **Transactions**: Adding and processing transactions
3. **Chain Validation**: Validating blockchain integrity
4. **Difficulty Comparison**: Testing different difficulty levels
5. **Persistence**: Saving and loading blockchain data
6. **Transaction History**: Retrieving transaction history

## 📚 API Reference

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

## 🔧 Proof of Work Algorithm

The implementation uses a simple but effective PoW algorithm:

1. **Target Calculation**: Creates a target string of leading zeros
2. **Nonce Increment**: Incrementally tries different nonce values
3. **Hash Verification**: Checks if the resulting hash meets the target
4. **Difficulty Adjustment**: Configurable difficulty (number of leading zeros)

Example with difficulty 4:
- Target: "0000"
- Valid hash: "0000a1b2c3d4e5f6..."
- Invalid hash: "0001a2b3c4d5e6f7..."

## 🔒 Security Features

### Tampering Detection
The blockchain automatically detects tampering by:
- Verifying block hashes match their content
- Checking previous hash references
- Validating proof of work requirements

### Immutability
- Each block's hash depends on all previous blocks
- Changing any block invalidates all subsequent blocks
- Previous hash linking prevents insertion of fake blocks

## ⚡ Performance Considerations

### Mining Performance
- Higher difficulty = longer mining time
- Exponential relationship between difficulty and time
- Recommended difficulty: 2-4 for testing, 4-6 for production

### Memory Usage
- All blocks stored in memory
- Consider database storage for large chains
- Transaction history can be memory-intensive

## 🧪 Testing

Run the demo script to test all functionality:

```bash
python examples/demo.py
```

The demo will test:
- Block creation and mining
- Transaction processing
- Chain validation
- Persistence
- Error handling

## 🚀 Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/pow-blockchain.git
cd pow-blockchain

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=blockchain

# Run specific test file
pytest tests/test_blockchain.py
```

### Code Quality

```bash
# Format code
black src/ tests/ examples/

# Lint code
flake8 src/ tests/ examples/

# Type checking
mypy src/
```

## 🔮 Extending the Implementation

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

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Areas for Improvement
- Performance optimizations
- Additional security features
- Network layer implementation
- Web interface
- Documentation improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

1. **Slow Mining**: Reduce difficulty for testing
2. **Memory Issues**: Consider limiting chain size for large demos
3. **File Permissions**: Ensure write permissions for persistence features

### Performance Tips

- Use difficulty 2-3 for quick testing
- Limit transaction count per block for large demos
- Consider clearing old blocks for long-running systems

## 📖 Educational Value

This implementation is designed to be:
- **Readable**: Clear, well-documented code
- **Educational**: Demonstrates blockchain concepts
- **Practical**: Actually functional and usable
- **Extensible**: Easy to modify and extend

Perfect for learning blockchain concepts, prototyping ideas, or as a foundation for more complex systems.

## 🙏 Acknowledgments

- Inspired by Bitcoin's Proof of Work consensus mechanism
- Built for educational purposes and learning blockchain technology
- Uses Python standard library for maximum compatibility

---

**Note**: This is an educational implementation. For production use, consider established blockchain frameworks and libraries.
