from playwright.sync_api import sync_playwright
import logging

logging.basicConfig(level=logging.INFO)

def run_o(url):
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(str(url), timeout=120000)
            page.screenshot(path='screenshot.png', full_page=True)

            footer = page.locator('#footer')
            if footer.count() == 0:
                footer = page.locator('body')  # Fallback
            link_elements = footer.locator('a')
            links = [
                {
                    'text': (link.text_content() or 'No text').strip(),
                    'href': link.get_attribute('href') or '#'
                }
                for i in range(link_elements.count())
                for link in [link_elements.nth(i)]
            ]

            main_content = page.locator('#main-content')
            text_content = main_content.inner_text(timeout=5000) if main_content.count() > 0 else page.inner_text('body')
            
            yield [{"RAW_TEXT_CONTENT": text_content.strip(), "LINKS": links}]
            browser.close()
    except Exception as e:
        logging.error(f"Error in run_o: {e}")
        yield [{"RAW_TEXT_CONTENT": f"Error: {str(e)}", "LINKS": []}]

def web_search(url):  # Simplified for Gradio
    if url and url.strip():
        yield from run_o(url)
    else:
        yield [{"RAW_TEXT_CONTENT": "Error: No URL provided", "LINKS": []}]
