## Installation

1. Install AFNI/SUMA via instructions here:
https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/install_instructs/index.html
Linux or MacOS is recommended.
After AFNI/SUMA installation, run the following:
```
cd ~/
\mkdir -p .afni/data
cd .afni/data
afni_open -aw suma_MNI152_2009.tgz
tar xvzf suma_MNI152_2009.tgz
```
This downloads the needed template brain.
## Installing ezsuma
Python should be installed on your computer.
Clone this repository, or download the repo to your computer as a ZIP file and decompress it.
`cd` into the `ezsuma` directory you should now have, and run one of these depending on your preference:
This project uses a standard `pyproject.toml`, so you can install it with whatever tool you prefer.
### Option A: uv (recommended, fastest)
```bash
uv run ezsuma.py
```
### Option B: pip + venv
```bash
python -m venv .venv
source .venv/bin/activate       
pip install -e .
```

### Option C: conda
```bash
conda create -n yourenv python=3.12
conda activate yourenv
pip install -e .
```
