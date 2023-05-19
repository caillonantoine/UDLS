import argparse
import base64
import logging
import os
import sys

import flask
import lmdb
import requests
from torch.utils import data

from . import AudioExample


class HTTPAudioExampleDataset(data.Dataset):

    def __init__(self, url: str):
        super().__init__()
        self.url = url

        self.length = int(self.fetch_content("len"))

    def __len__(self):
        return self.length

    def __getitem__(self, index: int):
        ae = self.fetch_content("get", index)
        ae = AudioExample(base64.b64decode(ae))
        return ae.as_dict()

    def fetch_content(self, *path):
        url = "/".join([self.url] + list(map(str, path)))
        return requests.get(url).text


def main():

    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='Remote dataset serving')
    parser.add_argument("db_path", help="dataset path")
    parser.add_argument("port", type=int, help="port to serve")

    args = parser.parse_args()

    env = lmdb.Environment(
        args.db_path,
        readonly=True,
        lock=False,
        readahead=False,
    )

    logging.info("parsing dataset")
    with env.begin() as txn:
        keys = list(txn.cursor().iternext(values=False))

    db_length = len(keys)

    app = flask.Flask(__name__)

    @app.route("/len")
    def get_length():
        return flask.jsonify(db_length)

    @app.route("/get/<index>")
    def get_element(index: int):
        index = int(index)
        if index >= db_length:
            return "invalid index"

        with env.begin() as txn:
            ae = AudioExample(txn.get(keys[index]))

        ae = base64.b64encode(bytes(ae))

        return ae

    @app.route("/")
    def root():
        return (f"<h1>UDLS remote serving</h1>"
                f"Current dataset: {os.path.abspath(args.db_path)}")

    logging.info("starting server")
    app.run("0.0.0.0", port=args.port, debug=False)


if __name__ == "__main__":
    sys.exit(main())
