import pdfplumber
import re
import csv

PDF_FILE = r"C:\Users\user\Desktop\Bank_Statment.pdf"
OUTPUT_FILE = "Transactions_To.csv"

EXCLUDE_KEYWORDS = [
    "owealth",
]

print("Extracting transactions... (this runs only once, be patient)")

rows = []

with pdfplumber.open(PDF_FILE) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if not text:
            continue

        lines = text.splitlines()

        for i, line in enumerate(lines):
            line_lower = line.lower()

            # Skip excluded keywords
            if any(keyword in line_lower for keyword in EXCLUDE_KEYWORDS):
                continue

            # Only process Transfer To lines
            if "transfer to" not in line_lower:
                continue

            # Combine current line with next 3 lines
            # to catch split transactions
            combined = " ".join(lines[i:min(i+4, len(lines))])

            # Find ALL amounts in the combined text
            amounts = re.findall(r'(?<!\d)([\d,]+\.\d{2})(?!\d)', combined)

            if not amounts:
                continue

            # Clean amounts and convert to float
            float_amounts = []
            for a in amounts:
                try:
                    float_amounts.append(float(a.replace(',', '')))
                except ValueError:
                    continue

            if not float_amounts:
                continue

            # The largest amount is most likely the transfer amount
            # Smaller ones are usually fees (e.g. ₦50 service charge)
            amount = max(float_amounts)

            # Skip if amount looks like a fee only (under ₦100)
            if amount < 100:
                continue

            rows.append([line.strip(), amount])

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Description", "Amount"])
    writer.writerows(rows)

print(f"Done! {len(rows)} transactions saved to {OUTPUT_FILE}")