
This project is a simple command-line application written in Python that processes a directory of receipt images and extracts structured information from each receipt using a language model.

For every receipt image, the program extracts:
- Receipt date
- Total amount spent
- Vendor name
- Expense category (from a predefined list)

The output is returned as a JSON object mapping each receipt filename to the extracted information.

## Project Structure

- `src/receipt_extractor/` — application source code
- `app/receipts/` — input receipt images
- `.venv/` — virtual environment
- `Makefile` — convenience command to run the application
- `requirements.txt` — Python dependencies

## set up instructions 

### 1. create virtual environment 

```bash
python -m venv .venv
source .venv/bin/activate 
```

### 2. install dependencies
```
pip install openai 
```
### 3. set open ai key 
```
export OPENAI_API_KEY=your_api_key_here
```

### 4. running the program 
```
make run
```