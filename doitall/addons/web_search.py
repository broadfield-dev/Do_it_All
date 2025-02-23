from playwright.sync_api import sync_playwright
import gradio as gr
from playwright.async_api import async_playwright
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.example.com")
        text_content = await page.inner_text("body")  # Get text content of the <body> element
        print(text_content)
        await browser.close()

def run_o(url):
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(str(url), timeout=120000)  # Increased timeout
            page.screenshot(path='screenshot.png', full_page=True)

            # More robust locator strategy
            footer = page.locator('#footer')
            link_elements = footer.locator('a')
            links = []
            for i in range(link_elements.count()):
                link = link_elements.nth(i)
                href = link.get_attribute('href')
                text = link.text_content()
                links.append({'text': text, 'href': href})

            # Targeted extraction of page content
            text_content = page.inner_text('#main-content')
            out = [{"RAW_TEXT_CONTENT": text_content, "LINKS": links}]
            yield out
            browser.close()
    except Exception as e:
        logging.error(f"Error occurred: {e}")

def web_search(prompt, history, url, mod, tok, seed, data):
    try:
        if url != "" and url != None:
            yield from run_o(url)
        else:
            history.extend([{'role': 'system', 'content': "observation: An Error occured\nI need to trigger a search using the following syntax:\naction: INTERNET_SEARCH action_input=URL"}])
            return history
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        history.extend([{'role': 'system', 'content': "observation: An Error occured\nI need to trigger a search using the following syntax:\naction: INTERNET_SEARCH action_input=URL"}])
        return history
