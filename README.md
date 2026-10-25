# handson-ML-homelab

My code, notes, and implementations while working through *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* by Aurélien Géron.

I am adapting the deep learning chapters to **PyTorch** instead of Keras/TensorFlow to get familiar with PyTorch's syntax and ecosystem early on. I'm using this repo to track my progress as a second-year computer science student building a foundation in machine learning.

## Setup & Environment

This environment runs on Python 3.13 inside a PowerShell virtual environment.

```powershell
# Create virtual environment
py -3.13 -m venv homl-pytorch-env

# Activate virtual environment
.\homl-pytorch-env\Scripts\Activate.ps1

# Install required packages
pip install -r req.txt
```

## Repository Structure

```text
├── req.txt             # Project dependencies
├── main.py             # Scratchpad for quick code tests
└── notebooks/          # Chapter-by-chapter implementations
```

## Goals & Roadmap

- [ ] Complete Part I (Classical ML with Scikit-Learn)
- [ ] Implement custom PyTorch training loops for neural networks
- [ ] Build end-to-end mini projects combining data processing and modeling
- [ ] Maintain clean, documented code for future reference

## Author

- **IYAD DAWOUD** — 2nd Year ISE Student