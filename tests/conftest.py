"""Pytest configuration and fixtures."""
import pytest_asyncio
from collections.abc import AsyncGenerator
from playwright.async_api import Browser, Page, async_playwright


@pytest_asyncio.fixture(scope="session")
async def browser() -> AsyncGenerator[Browser, None]:
    """Create a browser instance for the test session."""
    async with async_playwright() as p:
        browser_instance = await p.chromium.launch()
        try:
            yield browser_instance
        finally:
            await browser_instance.close()


@pytest_asyncio.fixture
async def page(browser: Browser) -> AsyncGenerator[Page, None]:
    """Create a new page for each test."""
    page_instance = await browser.new_page()
    try:
        yield page_instance
    finally:
        await page_instance.close()
