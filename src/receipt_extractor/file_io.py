# file_io.py
import os
import base64

def encode_file(path):
    """Encodes a file as a base64 string.

    The file is opened in binary mode, read entirely, and encoded using
    base64 encoding. The resulting value is returned as a UTF-8 string.

    Args:
        path: Path to the file to encode.

    Returns:
        A base64-encoded string representation of the file contents.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath):
    """Lists all files in a directory.

    Iterates over the contents of the given directory and yields the name
    and full path of each file found. Subdirectories are ignored.

    Args:
        dirpath: Path to the directory containing files.

    Yields:
        Tuples containing the filename and its full filesystem path.
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path

