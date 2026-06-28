# Bank Transfer Tracker

A lightweight Python tool for analyzing bank statements in PDF format.
Extracts outgoing transfers and enables fast recipient-based searches
with transaction counts and total amounts.

## How It Works

The tool runs in two stages:

**Stage 1 — Extract (`extract.py`)**
Parses a bank statement PDF and extracts all outgoing "Transfer To"
transactions into a structured CSV file.

**Stage 2 — Search (`search.py`)**
Loads the CSV and lets you search by recipient name, returning the
number of transactions and total amount sent to that person.

## Usage

**Step 1 — Set your PDF path in `extract.py`:**
```python
PDF_FILE = "path/to/your/bank_statement.pdf"
```

**Step 2 — Run the extractor:**
```bash
python extract.py
```

**Step 3 — Search for a recipient:**
```bash
python search.py
```

Then enter the recipient's name when prompted.

## Search Tips

- Full name returns the most precise results
- Partial names (first + middle, or middle + last) also work
- Searching by first name only returns all transactions
  to anyone with that name combined

## Requirements

```bash
pip install pdfplumber
```

## Project Structure