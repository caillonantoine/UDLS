from typing import Literal, Optional

import numpy as np

try:
    import jax.numpy as jnp
except:
    pass

try:
    import torch
except:
    pass

from .generated import AudioExample as AudioExamplePB

DTYPE_TO_PRECISION = {
    np.int16: AudioExamplePB.Precision.INT16,
    np.int32: AudioExamplePB.Precision.INT32,
    np.int64: AudioExamplePB.Precision.INT64,
    np.float16: AudioExamplePB.Precision.FLOAT16,
    np.float32: AudioExamplePB.Precision.FLOAT32,
    np.float64: AudioExamplePB.Precision.FLOAT64,
}

PRECISION_TO_DTYPE = {
    AudioExamplePB.Precision.INT16: np.int16,
    AudioExamplePB.Precision.INT32: np.int32,
    AudioExamplePB.Precision.INT64: np.int64,
    AudioExamplePB.Precision.FLOAT16: np.float16,
    AudioExamplePB.Precision.FLOAT32: np.float32,
    AudioExamplePB.Precision.FLOAT64: np.float64,
}


class AudioExample(object):

    def __init__(
            self,
            b: Optional[str] = None,
            output_type: Literal["numpy", "torch", "jax"] = "numpy") -> None:
        if b is not None:
            self.ae = AudioExamplePB.FromString(b)
        else:
            self.ae = AudioExamplePB()

        self.output_type = output_type

    def get(self, key: str):
        buf = self.ae.buffers[key]
        if buf is None:
            raise KeyError(f"key '{key}' not available")

        array = np.frombuffer(
            buf.data,
            dtype=PRECISION_TO_DTYPE[buf.precision],
        ).reshape(buf.shape)

        if self.output_type == "numpy":
            pass
        elif self.output_type == "jax":
            array = jnp.array(array)
        elif self.output_type == "torch":
            array = torch.from_numpy(array)
        else:
            raise ValueError(f"Output type {self.output_type} not available")

        return array

    def put(self, key: str, array: np.ndarray, dtype: np.dtype):
        buffer = self.ae.buffers[key]

        buffer.data = np.asarray(array).astype(dtype).tobytes()
        buffer.shape.extend(array.shape)
        buffer.precision = DTYPE_TO_PRECISION[dtype]

    def __str__(self) -> str:
        repr = []
        repr.append("AudioExample(")
        for key in self.ae.buffers:
            array = self.get(key)
            repr.append(f"\t{key}[{array.dtype}] {array.shape},")
        repr.append(")")
        return "\n".join(repr)

    def __bytes__(self) -> str:
        return self.ae.SerializeToString()
