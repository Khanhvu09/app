
# 📦 Modern Barcode Packing List App

## 🚀 Features
- Upload Excel files with item details
- Scan barcodes to assign items to dynamically created pallets
- Master List at top, pallets listed below
- Live updates to scanned quantities
- Visual color-coded rows:
  - Green: Fulfilled
  - Red: Over shipped
  - Yellow: Under shipped
- Delete rows or full pallets
- Reset all scanned quantities
- Bootstrap 5 UI with modern styling and icons

## 📄 Excel Format
| PART NUMBER | DESCRIPTION | SALES ORDER | SCANNED QTY | SHIP QTY | ORDER QTY | PALLET |

Leave SCANNED QTY and PALLET empty initially. The app will update them.

## ▶️ Running the App
1. Install dependencies:

```bash
pip install flask openpyxl
```

2. Run the server:

```bash
python app.py
```

3. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📁 Structure
- `app.py`: Flask backend
- `templates/`: UI templates
- `uploads/`: Folder where Excel files are stored

Enjoy a fast, flexible warehouse workflow!
