import openpyxl
from openpyxl import Workbook
import random

# Sample item data
items = [
    ("1001", "Widget Type A", "P1"),
    ("1002", "Widget Type B", "P1"),
    ("1003", "Widget Type C", "P2"),
    ("1004", "Gadget Type A", "P2"),
    ("1005", "Gadget Type B", "P3"),
    ("1006", "Widget Type D", "P3"),
    ("1007", "Gadget Type C", "P4"),
    ("1008", "Widget Type E", "P4"),
    ("1009", "Gadget Type D", "P5"),
    ("1010", "Widget Type F", "P5"),
    ("1011", "Widget Type G", "P6"),
    ("1012", "Gadget Type E", "P6"),
    ("1013", "Widget Type H", "P7"),
    ("1014", "Gadget Type F", "P7"),
    ("1015", "Widget Type I", "P8"),
    ("1016", "Gadget Type G", "P8"),
    ("1017", "Widget Type J", "P9"),
    ("1018", "Gadget Type H", "P9"),
    ("1019", "Widget Type K", "P10"),
    ("1020", "Gadget Type I", "P10"),
]

wb = Workbook()
ws = wb.active
ws.title = "Packing List"

# Add header
ws.append(["Item Name", "Description", "Scanned Quantity", "Expected Quantity"])

# Add rows
for item_id, description, pallet in items:
    expected = random.randint(3, 10)
    scanned = random.randint(0, expected)
    ws.append([item_id, description, scanned, expected])

# Save file
wb.save("packing_list.xlsx")
print("✅ Excel file 'packing_list.xlsx' created.")
