import allure



@allure.feature("示例功能")
@allure.story("打开网站")
@allure.title("验证 baidu.com 页面标题")
def test_example(page):

    with allure.step("打开百度网站"):
        page.goto("https://www.baidu.com")

    with allure.step("获取_标题"):
        title = page.title()

    with allure.step("断言_标题"):
        assert "百度" in title
    with allure.step("关闭页面"):
        page.close()


def test_error(page):

    with allure.step("打开百度网站"):
        page.goto("https://www.baidu.com")

    with allure.step("获取_标题"):
        title = page.title()

    with allure.step("断言_标题"):
        assert "error" in title

    with allure.step("关闭页面"):
        page.close()
