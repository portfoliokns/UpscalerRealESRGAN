import os
import torch
from PIL import Image
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from datetime import datetime
import argparse
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

# 演算処理デバイスの初期化
device = 'cuda' if torch.cuda.is_available() else 'cpu'
if device=='cuda':
    print('使用される演算処理デバイスは' + device + 'です')
elif device=='cpu':
    print('使用される演算処理デバイスは' + device + 'です。処理に時間を要します。このプログラムを実行する場合、NVIDIAなどのGPUの使用を推奨しています。')

# コマンドライン引数設定
parser = argparse.ArgumentParser(description="画像のアップスケール処理")
parser.add_argument('--tile', type=int, default=256, help='タイルのサイズ（例: 256）')
args = parser.parse_args()

# 学習済みモデルの初期化
model_path = './RealESRGAN_x4plus.pth'
model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)

upscaler = RealESRGANer(
    scale=4,
    model_path=model_path,
    dni_weight=None,
    model=model,
    tile=args.tile,
    tile_pad=10,
    pre_pad=0,
    half=True if device == 'cuda' else False,
    device=device
)

# 画像ファイルを選択
root = Tk()
root.withdraw()
file_path = askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")])
if not file_path:
    print('処理を中止します。')
    exit()
input_image = Image.open(file_path).convert('RGB')
input_image_array = np.array(input_image)

# アップスケール画像の
output_folder = './upscale'
os.makedirs(output_folder, exist_ok=True)
filename = os.path.basename(file_path)
base_name, ext = os.path.splitext(filename)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_path = os.path.join(output_folder, f"{base_name}_{timestamp}{ext}")

# 高解像度化処理
try:
    print('処理を開始します。しばらくお待ちください。画像は4倍のサイズにアップスケールされます。')
    output_image_array, _ = upscaler.enhance(input_image_array)
    output_image = Image.fromarray(output_image_array)
    output_image.save(output_path)
    print("画像のアップスケールが完了しました。upscaleフォルダをご確認ください。")
except Exception as e:
    print(f"エラーが発生しました: {e}")