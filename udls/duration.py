import math
import sys
from glob import glob

import librosa as li


def main():
    durations = list(map(lambda n: li.get_duration(filename=n), glob("*.wav")))
    d = sum(durations)
    hours = math.floor(d / 3600)
    minutes = math.floor((d % 3600) / 60)
    seconds = math.floor(d % 60)
    print(f"Found {len(durations)} .wav files")
    print(f"total duration: {hours}h {minutes:02d}m {seconds:02d}s")


if __name__ == "__main__":
    sys.exit(main())
