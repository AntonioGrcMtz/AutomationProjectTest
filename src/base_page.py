"""Base page object for all pages."""
from playwright.async_api import Page, expect


class BasePage:
    """Base page class with common methods for all pages."""

    def __init__(self, page: Page):
        """Initialize the page."""
        self.page = page

    async def navigate(self, url: str) -> None:
        """Navigate to a URL."""
        await self.page.goto(url)

    async def click_element(self, selector: str) -> None:
        """Click an element."""
        await self.page.click(selector)

    async def fill_text(self, selector: str, text: str) -> None:
        """Fill text in an input field."""
        await self.page.fill(selector, text)

    async def get_text(self, selector: str) -> str:
        """Get text from an element."""
        return await self.page.text_content(selector)

    async def wait_for_selector(self, selector: str) -> None:
        """Wait for an element to be visible."""
        await self.page.wait_for_selector(selector)

    async def take_screenshot(self, path: str) -> None:
        """Take a screenshot."""
        await self.page.screenshot(path=path)
