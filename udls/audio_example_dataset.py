import lmdb
import torch.utils.data as data
from .generated import AudioExample
import numpy as np


class WaveformAudioExampleDataset(data.Dataset):

    def __init__(self, path, buffer_key='waveform') -> None:
        super().__init__()
        self.env = lmdb.open(path, readonly=True)
        with self.env.begin() as txn:
            self.keys = list(txn.cursor().iternext(values=False))
        self.buffer_key = buffer_key

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, index):
        ae = AudioExample()

        with self.env.begin() as txn:
            ae.ParseFromString(txn.get(self.keys[index]))

        buffer = ae.buffers[self.buffer_key]

        array = np.frombuffer(
            buffer.data,
            dtype=np.int16,
        ).reshape(-1)

        array = array.astype(np.float32) / (2**15 - 1)

        return array