
from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("daniel-saed/f1-steering-angle")

print(ds)