import json
import os
import shutil
import subprocess
import urllib.request
from pathlib import Path

# 環境変数からパスを取得
LAYERS_JSON = Path(os.getenv("LAYERS_JSON"))
LAYERS_DIR = Path(os.getenv("LAYERS_DIR"))
TMP_ZIP = Path(os.getenv("TMP_ZIP"))
TMP_DIR = TMP_ZIP.parent  # 例: layers/tmp

# 一時ディレクトリ作成
TMP_DIR.mkdir(parents=True, exist_ok=True)

# JSON 読み込み
with open(LAYERS_JSON) as f:
    layers = json.load(f)

# 各レイヤーをダウンロードして展開
for layer in layers:
    if not layer.get("enabled", True):
        continue

    name = layer["name"]
    arn = layer["arn"]
    print(f"▶️ Downloading {name} from {arn}")

    # レイヤーのダウンロードURL取得
    url = subprocess.check_output(
        ["aws", "lambda", "get-layer-version-by-arn", "--arn", arn, "--query", "Content.Location", "--output", "text"],
        text=True,
    ).strip()

    # ZIPファイルをダウンロード
    urllib.request.urlretrieve(url, TMP_ZIP)

    # 展開先ディレクトリ作成
    dest_dir = LAYERS_DIR / name
    dest_dir.mkdir(parents=True, exist_ok=True)

    # ZIP 解凍
    subprocess.run(["unzip", "-oq", str(TMP_ZIP), "-d", str(dest_dir)], check=True)
    print(f"✅ Extracted to: {dest_dir}")

# 一時ディレクトリを削除
print(f"🧹 Cleaning up: {TMP_DIR}")
shutil.rmtree(TMP_DIR, ignore_errors=True)
