from setuptools import find_packages, setup, Command

NAME = "NudeNet"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "2.0.9"

REQUIRED = [
    "pillow",
    "opencv-python-headless>=4.5.1.48",
    "pydload",
    "scikit-image",
    "onnxruntime",
    "flask",
]

EXTRAS = {}

setup(
    name=NAME,
    version=VERSION,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
)
