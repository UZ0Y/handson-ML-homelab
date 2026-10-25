import os
import urllib.request
from sklearn.datasets import fetch_openml, load_iris

# Create local data folder
os.makedirs("data", exist_ok=True)

# Ch 2: Download exact book version of California Housing
print("Downloading Ch 2: California Housing (housing.csv)...")
housing_url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
housing_path = os.path.join("data", "housing.csv")

request = urllib.request.Request(housing_url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(request) as response, open(housing_path, "wb") as f:
    f.write(response.read())

# Ch 3: Cache MNIST
print("Downloading Ch 3: MNIST (~11 MB)...")
fetch_openml("mnist_784", version=1, as_frame=False, parser="liac-arff")

# Ch 4: Cache Iris
print("Downloading Ch 4: Iris Dataset...")
load_iris()

print("\nDone! All datasets for Chapters 1-4 are ready.")