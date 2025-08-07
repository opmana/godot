#!/usr/bin/env python3
"""
Setup script for Proof of Work Blockchain Implementation
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pow-blockchain",
    version="1.0.0",
    author="Blockchain Developer",
    author_email="developer@example.com",
    description="A complete Proof of Work blockchain implementation in Python",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pow-blockchain",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/pow-blockchain/issues",
        "Source": "https://github.com/yourusername/pow-blockchain",
        "Documentation": "https://github.com/yourusername/pow-blockchain#readme",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Distributed Computing",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.10.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "blockchain-demo=examples.demo:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="blockchain, proof-of-work, cryptocurrency, distributed-ledger",
)