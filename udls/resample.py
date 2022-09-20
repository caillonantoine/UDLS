import argparse
import functools
import multiprocessing
import pathlib
import subprocess
import sys
from os import makedirs, path
from typing import Iterable, Sequence, Tuple

from tqdm import tqdm


def resample_audio(audio: Tuple[int, str], output_dir, segment_time,
                   sampling_rate):
    audio_idx, audio_path = audio
    process = subprocess.Popen(
        [
            'ffmpeg',
            '-loglevel',
            'panic',
            '-hide_banner',
            '-i',
            audio_path,
            '-f',
            'segment',
            '-segment_time',
            str(segment_time),
            '-af',
            'dynaudnorm, silenceremove=stop_periods=-1:stop_duration=1:stop_threshold=-60dB',
            '-ar',
            str(sampling_rate),
            '-ac',
            '1',
            path.join(output_dir, f'audio_{audio_idx}_%05d.wav'),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()


def search_files(input_dir: str, ext: Sequence[str]) -> Iterable:
    file_id = 0
    for e in ext:
        files = pathlib.Path(input_dir).rglob(f'*.{e}')
        for file in files:
            yield file_id, file
            file_id += 1


def main():
    parser = argparse.ArgumentParser(description='Audio dataset preprocessing')
    parser.add_argument(
        '--ext',
        nargs='+',
        default=["wav", "mp3", "opus", "ogg", "aif", "aiff", "flac"],
        help='input dataset format')
    parser.add_argument('--sr', default="44100", help='target sampling rate')
    parser.add_argument("--output",
                        default=".",
                        help="output directory location")
    parser.add_argument("--input",
                        default=".",
                        help="input directory location")
    parser.add_argument("--len",
                        default=600,
                        help="length (in second) of target audio")
    parser.add_argument("--augment", default=False, action="store_true")

    args = parser.parse_args()

    out_dir = path.join(args.output, f"out_{args.sr}")
    makedirs(out_dir)

    files = list(search_files(args.input, args.ext))

    with multiprocessing.Pool() as pool:
        processed = pool.imap_unordered(
            functools.partial(resample_audio,
                              output_dir=out_dir,
                              segment_time=args.len,
                              sampling_rate=args.sr), files)
        
        for _ in tqdm(processed, total=len(files)):
            pass
        


if __name__ == "__main__":
    sys.exit(main())
