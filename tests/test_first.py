import pytest


@pytest.mark.parametrize("url,title", [
    ("https://yandex.ru", "Яндекс"),
    ("https://google.ru", "Google")
])
def test_title(browser, url, title):
    browser.get(url)
    current_title = browser.title
    assert current_title == title
