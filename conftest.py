import io
import allure
import pytest
from PIL import ImageGrab
from allure_commons.types import AttachmentType


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