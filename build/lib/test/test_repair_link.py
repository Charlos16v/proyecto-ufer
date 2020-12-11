from src.services.crawler.repair_link import repair_link
from src.services.config.ufer_conf import UFER_DOMAIN
import pytest


@pytest.mark.repair_link
def test_repair_link():
    assert repair_link("test") == UFER_DOMAIN + "test"
    assert repair_link("SDKLJDFJDFdsfkjdfSFDJ") == UFER_DOMAIN + "SDKLJDFJDFdsfkjdfSFDJ"
