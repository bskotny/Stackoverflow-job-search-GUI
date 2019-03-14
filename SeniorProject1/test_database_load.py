from database_load import*


# tests for function get_location
def test_get_location():
    test_location = get_location(feedparser.parse('https://stackoverflow.com/jobs/feed'), 1)
    assert isinstance(test_location, str)
    assert get_location(feedparser.parse('https://stackoverflow.com/jobs/feed'), 1.0)
    assert get_location(1, 1)


# tests for function get_company
def test_get_company():
    test_company = get_company(feedparser.parse('https://stackoverflow.com/jobs/feed'), 1)
    assert isinstance(test_company, str)
    assert get_company(feedparser.parse('https://stackoverflow.com/jobs/feed'), 1.0)
    assert get_company(1, 1)


# tests for function get_title
def test_get_title():
    test_title = get_title(feedparser.parse('https://stackoverflow.com/jobs/feed'), 1)
    assert isinstance(test_title, str)
    assert get_title(feedparser.parse('https://stackoverflow.com/jobs/feed'), 1)
    assert get_title(feedparser.parse('https://stackoverflow.com/jobs/feed'), 1.0)


if __name__ == "__main__":
    test_get_location()
    test_get_company()
    test_get_title()