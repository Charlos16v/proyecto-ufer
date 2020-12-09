from src.services.config.ufer_conf import UFER_KEYS, UFER_TYPE
import pytest


@pytest.mark.ufer_conf
def test_ufer_conf():
    assert len(UFER_TYPE) == len(UFER_KEYS)

