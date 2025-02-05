from playwright.async_api import async_playwright
import doitall.addons.chat_style as cs
import tempfile
import markdown
import datetime
import asyncio
import os

async def load_html_string(html_string, timename):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode='w', encoding='utf-8') as f:
            f.write(html_string)
            temp_file_path = f.name

        await page.goto(f"file://{temp_file_path}")
        #await page.set_viewport_size({"width": 800, "height": 5000})  # Set a suitable viewport size
        await page.screenshot(path=f'{os.getcwd()}/{timename}_html_to_screenshot.png', 
            
            omit_background=True, 
            full_page=True
            )
        await browser.close()

    return f'./{timename}_html_to_screenshot.png'

def markdowntext(text):
    return markdown.markdown(text)

def sort_chat(chat):
    chat_out=""
    for ea in chat:
        if ea['role'] == 'user':
            chat_out+=f"<div style='{cs.user};'>{ea['content']}</div>"
        elif ea['role'] == 'assistant':
            ass_out = markdowntext(ea['content'])
            print(ass_out)
            chat_out+=f"<div style='{cs.bot};'>{ass_out}</div>"
    return chat_out


async def html_s(html_string):
    timename = str(datetime.datetime.now()).replace(" ", "__").replace(":", "_").split('.')[0]
    print(html_string)
    mark_out = sort_chat(html_string)
    #print('######################################')
    #print(mark_out)
    #print('######################################')

    screenshot_path = await load_html_string(mark_out, f'{timename}_html_to_screenshot.png')
    return screenshot_path

def html_ss(html_content):
    screenshot_path = asyncio.run(html_s(html_content))
    print(f"Screenshot saved at: {screenshot_path}")
    return screenshot_path
