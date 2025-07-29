from mylib.util import hello


def test_hello_uses_default_env_template():
    """conftest.py で設定されたデフォルトテンプレートが使われるかを検証."""
    assert hello("Alice") == "Hello, Alice from layer!"


def test_hello_uses_overridden_env_template(monkeypatch):
    """テスト関数内でテンプレートを上書きした場合、それが使用されるかを検証."""
    monkeypatch.setenv("HELLO_TEMPLATE", "Hi, {name}!")
    assert hello("Bob") == "Hi, Bob!"
