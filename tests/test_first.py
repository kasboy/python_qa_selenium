import time


def test_first_test(browser, url):
    # time.sleep(5)
    browser.get(url)
    # browser.save_screenshot("example.png")
    # Aditional Arguments example: --browser chrome/firefox --maximized --headless --url=https://yandex.ru
    assert browser.title == "Your Store"
