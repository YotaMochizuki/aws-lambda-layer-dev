import pytest


@pytest.fixture(autouse=True)
def set_default_env(monkeypatch):
    """各テスト実行前に共通の環境変数 HELLO_TEMPLATE をセットする.テスト関数内で個別に上書きも可能."""
    monkeypatch.setenv("HELLO_TEMPLATE", "Hello, {name} from layer!")
