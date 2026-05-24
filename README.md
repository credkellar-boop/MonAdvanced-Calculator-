# MonAdvanced-Calculator-

🔍 **An advanced, modular calculator engine built with Python.**

---

<p align="left">
  <img src="https://img.shields.io/github/actions/workflow/status/credkellar-boop/MonAdvanced-Calculator-/python-package.yml?branch=main&style=flat-square&logo=github" alt="Build Status">
  <img src="https://img.shields.io/github/languages/top/credkellar-boop/MonAdvanced-Calculator-?style=flat-square&color=blue&logo=python" alt="Top Language">
  <img src="https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue?style=flat-square&logo=python" alt="Python Versions">
  <img src="https://img.shields.io/badge/code%20style-flake8-black?style=flat-square" alt="Code Style">
  <img src="https://img.shields.io/github/license/credkellar-boop/MonAdvanced-Calculator-?style=flat-square&color=green" alt="License">
</p>

---

## 📂 Project Structure

This project follows a professional Python package layout, separating your application logic from your configuration and test suite.

```text
MonAdvanced-Calculator-/
│
├── .github/
│   └── workflows/
│       └── python-package.yml   # CI/CD automated pipeline
│
├── calculator/                  # Main source package
│   ├── __init__.py              # Makes the folder an importable module
│   ├── core.py                  # Basic arithmetic operations
│   └── advanced.py              # Advanced calculations (scientific, matrices, etc.)
│
├── tests/                       # Automated test suite
│   ├── __init__.py
│   ├── test_core.py             # Unit tests for core calculator functionality
│   └── test_advanced.py         # Unit tests for advanced functionality
│
├── .gitignore                   # Files to ignore in Git (venv, __pycache__)
├── LICENSE                      # Project license terms
├── README.md                    # Project documentation
└── requirements.txt             # Project project dependencies
