# UDLS
Unified Dataset Loading System

This repo contains base class for the creation of memory *and* processing efficient custom dataset.
Everything basically relies on the **lmdb** database which allow lightning fast read / write operations.

It also contains *preset* datasets, allowing fast experiments on various data (see example below)


```python
# EXAMPLE CODE FOR LOADING SOLv4 SRING ON A DOMAIN ADAPTATION PROBLEM
import torch
import librosa as li
from udls.datasets import Solv4StringDomainAdaptation


def preprocess(filename):
    """
    This function will be called the first time you initialize the dataset for each file present inside the Solv4string folder. It should return a preprocessed ndarray or Tensor.
    """
    x = li.load(filename, 16000)[0]
    if len(x) % 4096:
        x = x[:-(len(x) % 4096)]
    return x.reshape(-1, 4096)


dataset = Solv4StringDomainAdaptation("preprocess/folder/location", preprocess)
loader = torch.utils.data.DataLoader(dataset, 16, True, drop_last=True)

for step, (domain_index, value) in enumerate(loader):
    # DO SOMETHING INTERESTING WITH YOUR MODEL
    pass
```