from pathlib import Path
import re

# ریشه پروژه
ROOT = Path(".")

# پوشه‌هایی که باید نادیده گرفته شوند
IGNORE_DIRS = {".venv", "__pycache__"}

# پیدا کردن اولین class داخل فایل
CLASS_PATTERN = re.compile(
    r"^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?:\(|:)", re.MULTILINE
)

for folder in ROOT.rglob("*"):
    if not folder.is_dir():
        continue

    # رد کردن پوشه‌های نادیده گرفته شده (بدون حساسیت به حروف بزرگ/کوچک)
    if any(part.lower() in IGNORE_DIRS for part in folder.parts):
        continue

    imports = []

    for py_file in sorted(folder.glob("*.py")):
        if py_file.name == "__init__.py":
            continue

        text = py_file.read_text(encoding="utf-8")

        match = CLASS_PATTERN.search(text)
        if not match:
            continue

        class_name = match.group(1)
        module_name = py_file.stem

        imports.append(f"from .{module_name} import {class_name}")

    if imports:
        init_file = folder / "__init__.py"
        init_file.write_text("\n".join(imports) + "\n", encoding="utf-8")
        print(f"Generated: {init_file}")
