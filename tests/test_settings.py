import pytest
from tei_iiif.utils.settings import settings

@pytest.fixture(scope="module")
def get_settings():
    return settings

def test_settings_pass(get_settings):
    settings_dict = get_settings()
    assert settings_dict["temp_dir"] == "./temp/"