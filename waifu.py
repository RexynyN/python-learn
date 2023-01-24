import sys
from argparse import Namespace
from pathlib import Path

from PIL import Image

# THISDIR = str(Path(__file__).resolve().parent)
# sys.path.insert(0, str(Path(THISDIR).parent))

from waifu2x import load_models, upscale_image

args = Namespace(
	color="rgb",
	model_dir=None,
	arch="ResNet10",
	method="scale",
	scale_level=1,
	gpu=-1,
	scale_ratio=2.0,
	tta=False,
	block_size=128,
	batch_size=16,
)

models = load_models(args)


def test_background_png():
	"""test_background_png"""
	src = Image.open(f"fb1.jpg")
	dst = src.copy()
	dst = upscale_image(args, dst, models["scale"])
	dst.convert(src.mode).save(f"newfb1.jpg")


def test_foreground_png():
	"""test_foreground_png"""
	src = Image.open(f"{THISDIR}/data/foreground.png")
	dst = src.copy()
	dst = upscale_image(args, dst, models["scale"])
	dst.convert(src.mode).save(f"{THISDIR}/data/foreground_resnet10_expected.png")


test_background_png()