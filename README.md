# このアプリケーションについて
これはpython環境で実行する画像の高画質化アプリです。機能は以下の通りです。
- アップスケール
  - 選択した画像をアップスケールすることができます。

# 事前準備
## pythonインストール
python 3.10.11をインストールしてください。

## ファイルをダウンロード
GitHub上からファイルをダウンロードしてください。
もしくは以下のコマンドを実行し、UpscalerRealESRGANをクローンしてください。
```
git clone https://github.com/portfoliokns/UpscalerRealESRGAN.git
```
## 仮想環境を設定
以下のコマンドから、仮想環境を構築してください。
```
python -m venv venv
```

以下のコマンドから、仮想環境に入ってください。
```
source venv/bin/activate 
```

## 各種ライブラリのインストール
以下のコマンドから、requirements.txtを実行して、各種ライブラリをインストールしてください。
```
pip install -r requirements.txt
```

## 学習済みモデルのダウンロード & 配置
以下のモデルを検索して、ダウンロードして、"UpscalerRealESRGAN"フォルダに配置してください。

- RealESRGAN_x2plus.pth
- RealESRGAN_x4plus.pth
- RealESRGAN_x4plus_anime_6B.pth

# 使い方
アップスケールしたい画像を準備し、ターミナル上から仮想環境に入っておいてください。

## アップスケール
- 以下のコマンドからアップスケールを実行してください。
```:実行コマンドの例①
python RealESRGAN_x2plus.py
```
```:実行コマンドの例②
python RealESRGAN_x4plus.py --tile 512
```
- 選択画面からアップスケールしたい画像を選択してください。
- 選択後、アップスケール処理が開始され、"upscale"フォルダにアップスケール済みの画像が保存されます。
- アップスケールには時間を要するので、CUDA搭載のPCで実行することを推奨します。

# CUDAを使用する場合の補足事項
Windows11の環境(CUDA)で実行した際に遭遇した問題についての対処法を記載しています。ここに記載している内容は鵜呑みにせず、まずは内容を読んで調べてから実行してください。

## CUDA(GPU)ではなく、CPUで処理されていて遅い
CUDA版のPyTorchが必要となります。以下のコマンドを実行し、状況を確認してください。
```
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

```:実行結果の例
1.12.1+cpu
False
```
"False"が出力されたなら、PyTorchがCPU版となっているため、CUDA版をインストールしないといけない。

以下のコマンドを実行し、CUDA版のPyTorchをインストールする。
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## 互換性によるエラー
プログラムを実行した際に"ModuleNotFoundError: No module named 'torchvision.transforms.functional_tensor'"といったエラーが出た場合、互換性に問題あります。以下のコマンドを実行し、0.16.1のバージョンにしましょう。
```
pip install torchvision==0.16.1 --index-url https://download.pytorch.org/whl/cu118
```

# 開発/検証環境の情報
## macOS
- CPU:Apple M1チップ
- メモリ:16GB
- macOS:Sonoma 14.6.1
- python 3.10.11

## Windows11
- CPU:AMD Ryzen 5 4500 6-Core Processor 36.0GHz
- メモリ:32GB
- GPU:NVIDIA GeForce RTX-4060
- Windows11
- python 3.10.6

# 参考
- [https://github.com/xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)

# 免責事項
- この拡張機能はGitHub上で公開されています。この拡張機能を使用したことにより発生した被害や損害について、このアプリの開発者は一切関与致しません。
- 使用するライブラリの互換性や非推奨性など、開発者が開発時点で意図しないライブラリが存在する可能性があります。
- ReadMeに記載しているプロンプトなどは全てmacOSのTerminal上で実行することを前提に記載しています。
