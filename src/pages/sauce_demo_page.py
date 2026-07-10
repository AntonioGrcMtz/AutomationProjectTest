try:
    from playwright.async_api import Page
except Exception:  # pragma: no cover - fallback for environments without playwright
    from typing import Any as Page
from src.base_page import BasePage


class SauceDemoPage(BasePage):
    """Page object for Sauce Demo home page."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        super().__init__(page)

    async def open(self) -> None:
        """Open the Sauce Demo home page."""
        await self.navigate(self.URL)

    async def get_heading_text(self) -> str:
        """Get the main heading text from the page."""
        heading = await self.get_text("h1")
        return heading or ""

    async def is_login_button_visible(self) -> bool:
        """Check if login button is visible."""
        return await self.page.is_visible("#login-button")
