"""Sample test to verify setup."""
import pytest
from playwright.async_api import Page


@pytest.mark.asyncio
async def test_example_website(page: Page):
    """Test navigation to a website."""
    # Navigate to a website
    await page.goto("https://www.saucedemo.com/")
    
    # Get the heading text
    heading = await page.text_content("h1")
    
    # Verify the heading
    assert heading is not None
    assert "Example Domain" in heading


@pytest.mark.asyncio
async def test_page_title(page: Page):
    """Test page title verification."""
    # Navigate to a website
    await page.goto("https://www.saucedemo.com/")
    
    # Get the page title
    title = await page.title()
    
    # Verify the title
    assert "Example" in title
