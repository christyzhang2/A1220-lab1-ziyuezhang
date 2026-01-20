# main.py
import json
import argparse
from . import file_io as io_mod
from . import gpt

def clean_amount(value):
    """normalize monetary amount
    removes dollar sign if present and convert to float
    """
    if value is None: 
        return value 
    
    if isinstance(value, str):
        value = value.replace("$", "").strip()
    
    try:
        return float(value)
    except (ValueError, TypeError):
        return value

def process_directory(dirpath):
    results = {}
    for name, path in io_mod.list_files(dirpath):
        image_b64 = io_mod.encode_file(path)
        data = gpt.extract_receipt_info(image_b64)
        if "amount" in data:
            data["amount"] = clean_amount(data["amount"])

        results[name] = data
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath")
    parser.add_argument("--print", action="store_true")
    args = parser.parse_args()

    data = process_directory(args.dirpath)
    if args.print:
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()

