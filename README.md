# Web Automation Project

A Python-based web automation project using Playwright and pytest for browser automation and testing.

## 📋 Project Structure

```
├── src/                    # Source code
│   ├── base_page.py       # Base page object class
│   └── __init__.py
├── tests/                  # Test files
│   ├── conftest.py        # Pytest configuration and fixtures
│   ├── test_sample.py     # Sample tests
│   └── __init__.py
├── config/                 # Configuration files
│   ├── settings.py        # Application settings
│   └── __init__.py
├── requirements.txt        # Python dependencies
├── pytest.ini             # Pytest configuration
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore patterns
└── README.md             # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or create the project directory**
   ```bash
   cd AutomationProjectTest
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Playwright browsers**
   ```bash
   playwright install
   ```

6. **Create `.env` file**
   ```bash
   copy .env.example .env  # On Windows
   cp .env.example .env    # On macOS/Linux
   ```

## 🧪 Running Tests

### Run all tests
```bash
pytest
```

### Run tests with verbose output
```bash
pytest -v
```

### Run specific test file
```bash
pytest tests/test_sample.py
```

### Run tests with coverage
```bash
pip install pytest-cov
pytest --cov=src tests/
```

## 📝 Writing Tests

### Basic Test Structure
```python
import pytest
from playwright.async_api import Page

@pytest.mark.asyncio
async def test_example(page: Page):
    await page.goto("https://example.com")
    title = await page.title()
    assert "Example" in title
```

### Using Page Objects
```python
from src.base_page import BasePage

class MyPage(BasePage):
    async def perform_action(self):
        await self.click_element(".button-selector")
```

## ⚙️ Configuration

### Environment Variables
Edit `.env` file to configure:
- `HEADLESS` - Run browser in headless mode (true/false)
- `BROWSER_TYPE` - Browser type (chromium, firefox, webkit)
- `TIMEOUT` - Default timeout in milliseconds
- `BASE_URL` - Base URL for tests

### Pytest Configuration
Configure pytest in `pytest.ini`:
- Test discovery patterns
- Async mode settings
- Output verbosity

## 📚 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Async/Await in Python](https://docs.python.org/3/library/asyncio.html)

## 🤝 Best Practices

1. **Use Page Objects** - Create page classes inheriting from `BasePage`
2. **Async/Await** - Use async functions for Playwright operations
3. **Fixtures** - Leverage pytest fixtures for setup/teardown
4. **Waits** - Use implicit/explicit waits instead of sleep
5. **Error Handling** - Handle timeouts and element not found errors gracefully

## ✨ Next Steps

1. Create page objects for your target websites
2. Write test cases for your automation scenarios
3. Configure CI/CD to run tests automatically
4. Add reporting and screenshots for failed tests
5. Extend the `conftest.py` with custom fixtures

---

Happy automating! 🎉
