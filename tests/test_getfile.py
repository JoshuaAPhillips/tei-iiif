import pytest
import sys
from tei_iiif.utils.settings import settings
from tei_iiif.getfile import fileName, getFile

@pytest.fixture(scope="module")
def get_settings():
    return settings

def test_filename_pass(get_settings, monkeypatch):
    settings = get_settings()
    monkeypatch.setattr(sys, "argv", ["fileName", "file.xml"])
    file = fileName()
    assert file == "https://raw.githubusercontent.com/JoshuaAPhillips/digital-anon/main/transcriptions/file.xml"

def test_filename_fail(get_settings, monkeypatch):
    settings = get_settings()
    monkeypatch.setattr(sys, "argv", ["fileName", "file.xml"])
    file = fileName()
    assert file is None