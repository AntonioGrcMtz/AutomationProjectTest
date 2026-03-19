"""Pytest configuration and fixtures."""
import pytest
from playwright.async_api import async_playwright, Browser, Page


@pytest.fixture(scope="session")
async def browser() -> Browser:
    """Create a browser instance."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        yield browser
        await browser.close()


@pytest.fixture
async def page(browser: Browser) -> Page:
    """Create a new page for each test."""
    page = await browser.new_page()
    yield page
    await page.close()
