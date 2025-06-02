# Packing App

This Flask app allows barcode scanning into dynamic pallets from Excel files.

## Features
- Upload Excel files with item data and ship dates
- Scan barcodes to build pallets dynamically
- Master list with live scanned quantity updates
- Color-coded row highlighting for scanned vs shipped
- Option to reset scans or delete pallets

## How to Run
```bash
pip install -r requirements.txt
python app.py
```

Then go to http://localhost:5000 in your browser.
