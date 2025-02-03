from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.example.com")
        text_content = await page.inner_text("body") # Get text content of the <body> element
        print(text_content)
        await browser.close()

def run_o(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(str(url), timeout=60000)  # Replace with your target URL
        page.screenshot(path='screenshot.png', full_page=True)

        footer = page.locator('body')  # Adjust the selector if needed
        link_elements = footer.locator('a')
        links = []
        for i in range(link_elements.count()):
            link = link_elements.nth(i)
            href = link.get_attribute('href')
            text = link.text_content()
            links.append({'text': text, 'href': href})

        b_links2 = page.locator('footer')  # Adjust the selector if needed
        link_elements2 = b_links2.locator('a')
        for ii in range(link_elements2.count()):
            link2 = link_elements2.nth(ii)
            href2 = link2.get_attribute('href')
            text2 = link2.text_content()
            links.append({'text': text2, 'url': href2})
        out = [{"RAW_TEXT_CONTENT":page.inner_text('body'), "LINKS":links}]
        yield out  
        browser.close()

def web_search(prompt,history, url,mod,tok,seed,data):
        return_list=[]
        try:
            if url != "" and url != None:    
                yield from run_o(url)
            else: 
                history.extend([{'role':'system','content':"observation: An Error occured\nI need to trigger a search using the following syntax:\naction: INTERNET_SEARCH action_input=URL\n"}])
                return history
        except Exception as e:
            history.extend([{'role':'system','content':"observation: I need to trigger a search using the following syntax:\naction: INTERNET_SEARCH action_input=URL\n"}])
            return history
