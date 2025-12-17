# WhatsApp Biz - Developer Guide

This guide is intended for developers who want to contribute to the `waclient` package or understand its internal structure.

## Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/surenthars/waclient.git
   cd waclient
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the package in editable mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Running Tests

We use `pytest` for testing.

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=waclient
```

## Project Structure

```
waclient/
├── examples/           # Example scripts
├── tests/              # Unit and integration tests
├── waclient/       # Source code
│   ├── __init__.py     # Package initialization
│   ├── client.py       # Main WhatsAppClient
│   ├── messages.py     # Message sending logic
│   ├── media.py        # Media upload/download
│   ├── models.py       # Data models (Button, Row, etc.)
│   └── exceptions.py   # Custom exceptions
├── setup.py            # Package installation setup
├── pyproject.toml      # Build system configuration
├── README.md           # Main documentation
├── USER_MANUAL.md      # Detailed usage guide
└── DEVELOPER_GUIDE.md  # This file
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

## Coding Standards

- Follow PEP 8 style guide.
- Use `black` and `flake8` for linting.
- Ensure all new features have accompanying tests.

## Release Process

1. Bump version in `setup.py` and `waclient/__init__.py`.
2. Build the package:
   ```bash
   python -m build
   ```
3. Upload to PyPI (requires credentials):
   ```bash
   twine upload dist/*
   ```
