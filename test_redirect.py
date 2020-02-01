import importlib


def test_that_redirect_can_be_imported() -> None:
    importlib.import_module("redirect")
