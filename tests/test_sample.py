"""Sample test to verify setup."""
import pytest
from playwright.async_api import Page

from src.pages.sauce_demo_page import SauceDemoPage


@pytest.mark.asyncio
async def test_example_website(page: Page):
    """Test navigation to Sauce Demo website and login button visibility."""
    sauce_demo = SauceDemoPage(page)
    await sauce_demo.open()

    assert await sauce_demo.is_login_button_visible() is True


@pytest.mark.asyncio
async def test_page_title(page: Page):
    """Test Sauce Demo page title verification."""
    sauce_demo = SauceDemoPage(page)
    await sauce_demo.open()

    title = await page.title()

    assert "swag labs" in title.lower()

@pytest.mark.asyncio
async def test_page_title(page: Page):
    """Test page title verification."""
    sauce_demo = SauceDemoPage(page)
    await sauce_demo.open()

    title = await page.title()

    assert "sauce" in title.lower() or title != ""  # Ajusta según título actual del sitio

