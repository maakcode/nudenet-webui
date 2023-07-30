# NudeNet WebUI

A browser interface for NudeNet classifier.

![](https://github.com/maakcode/nudenet-web/blob/main/banner.png)

## Features

- Download and test image from image URL
- Test images in local directory

## Installation & Running

0. Download [notAI-tech/NudeNet model](https://github.com/notAI-tech/NudeNet/releases/download/v0/classifier_model.onnx) to `NudeNet/models/classifier_model.onnx`

1. Install the dependencies:

```bash
pip install -e .
```

2. Run server:

```bash
python app.py
```

3. Open browser `http://127.0.0.1:5000`

## Credits

- Base implementation and model: <https://github.com/notAI-tech/NudeNet>
