import allure


@allure.feature("示例功能")
@allure.story("打开网站")
@allure.title("验证 example.com 页面标题")
def test_example(page):

    with allure.step("打开网站"):
        page.goto("https://example.com")

    with allure.step("获取标题"):
        title = page.title()

    with allure.step("断言标题"):
        assert "Example" in title