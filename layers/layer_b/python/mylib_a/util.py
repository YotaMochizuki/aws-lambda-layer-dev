import os


def hello(name: str) -> str:
    """名前付きで挨拶メッセージを返す関数.

    Parameters:
        name (str): 挨拶対象の名前

    Returns:
        str: 挨拶テンプレートに基づく文字列（例: "Hello, Alice from layer!"）
    """
    # メッセージテンプレートを環境変数から取得（なければデフォルト）
    template = os.getenv("HELLO_TEMPLATE", "Hello, {name} from layer!")
    return template.format(name=name)
