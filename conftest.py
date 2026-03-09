import io

import allure
import pytest
from PIL import ImageGrab
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright

from LBUI.tools.Global_Tools import get_page_by_url


@pytest.fixture(scope="session")
def playwright_instance():
    """Playwright 全局实例"""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    """浏览器（CDP 连接已打开 Chrome）"""
    browser = playwright_instance.chromium.connect_over_cdp(
        "http://localhost:9222"
    )
    yield browser

@pytest.fixture(scope="function")
def context(browser):
    """context"""
    context = browser.contexts[0]
    yield context

@pytest.fixture(scope="function")
def page(context):
    """主页"""
    page = get_page_by_url(context, "/app/a6bc5827/#/home")
    assert page is not None, "未找到主页 Page"
    page.bring_to_front()
    yield page


print("🔥🔥🔥 红红火火恍恍惚惚 🔥🔥🔥")
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 让 pytest 先正常执行
    outcome = yield
    report = outcome.get_result()

    # 只在“用例执行阶段失败”时截图
    if report.when == "call" and report.failed:
        print("🔥 断言失败，准备截图")  # ← 用来验证 hook 是否进来了
        try:
            img = ImageGrab.grab()  # 截全屏
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")  # 转成 PNG 字节

            allure.attach(
                buffer.getvalue(),
                name="失败截图",
                attachment_type=AttachmentType.PNG
            )
        except Exception as e:
            print("❌ 截图失败：", e)