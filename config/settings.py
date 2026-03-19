"""Application settings."""
import os
from dotenv import load_dotenv

load_dotenv()

# Browser settings
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
BROWSER_TYPE = os.getenv("BROWSER_TYPE", "chromium")
TIMEOUT = int(os.getenv("TIMEOUT", 30000))

# Test settings
BASE_URL = os.getenv("BASE_URL", "https://example.com")
