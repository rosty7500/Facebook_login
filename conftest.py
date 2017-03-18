import pytest

@pytest.fixture(scope="module")
def base_url():
    url = 'https://www.facebook.com/'
    return url

