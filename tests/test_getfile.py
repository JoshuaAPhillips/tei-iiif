import pytest
import sys
import requests
from tei_iiif.utils.settings import settings
from tei_iiif.getfile import fileName, getFile

@pytest.fixture(scope="module")
def get_settings():
    return settings

def test_filename_pass(get_settings, monkeypatch):
    settings = get_settings()
    monkeypatch.setitem(settings, "base_path", "https://raw.githubusercontent.com/JoshuaAPhillips/tei-iiif/main/tests")
    monkeypatch.setattr(sys, "argv", ["fileName", "testdoc.xml"])
    file = fileName()
    assert file == "https://raw.githubusercontent.com/JoshuaAPhillips/digital-anon/main/transcriptions/testdoc.xml"

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