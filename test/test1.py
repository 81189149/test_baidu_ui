from time import sleep
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # context = browser.new_context(java_script_enabled=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://game.bilibili.com/platform/#/")


    text = page.inner_text("body")
    text_len=len(text)
    print("内容长度",text_len)
    print("body:",text)

    assert text_len==0,"java_script被关掉了"