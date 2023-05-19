import argparse
import base64
import os
import sys

import flask
import lmdb

from . import AudioExample


def main():
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
        return (f"<h1>UDLS remote serving<h1>"
                f"Current dataset: {os.path.abspath(args.db_path)}")

    app.run("0.0.0.0", port=args.port, debug=False)


if __name__ == "__main__":
    sys.exit(main())
