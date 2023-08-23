import pytest
from tei_iiif.utils.settings import settings
from tei_iiif.getfile import fileName, getFile

@pytest.fixture(scope="module")
def get_settings():
    return settings

def test_get_remote_file_pass(requests_mock):
    requests_mock.get("http://www.test.com", text="test")
    actual_result = getFile("http://www.test.com").text
    expected_result = "test"
    assert actual_result == expected_result

def test_get_local_file_pass():
    file = "tests/testdoc.xml"
    expected_result = open(file, "r").read()
    actual_result = getFile(file)
    assert actual_result == expected_result