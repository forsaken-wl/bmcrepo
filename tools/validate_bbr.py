#!/usr/bin/env python3
import pathlib, re, sys

fields = {"name", "provides", "libprovides", "depends", "makedepends",
          "requiredby", "upstream", "relurl", "checksum"}
errors = []

for path in sorted(pathlib.Path(".").rglob("*.bbr")):
    names = []
    seen = set()
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^-(\w+)(?:\s*:)?\s*(.*)$", line)
        if not m:
            errors.append(f"{path}:{lineno}: malformed field")
            continue
        field, value = m.group(1), m.group(2).strip()
        if field not in fields:
            errors.append(f"{path}:{lineno}: unknown field {field}")
            continue
        if field == "name":
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+-]*", value):
                errors.append(f"{path}:{lineno}: invalid package name")
            names.append(value)
        if field in {"depends", "makedepends", "requiredby", "provides", "libprovides"} and value:
            for item in value.split(","):
                item = item.strip()
                if not item:
                    errors.append(f"{path}:{lineno}: empty list item")
                elif item in seen and field in {"depends", "makedepends"}:
                    pass
        if field in seen and field == "name":
            errors.append(f"{path}:{lineno}: duplicate name field")
        seen.add(field)
    if len(names) != 1:
        errors.append(f"{path}: expected exactly one name field, found {len(names)}")
    if "name" not in seen:
        errors.append(f"{path}: missing name field")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("all .bbr recipes valid")
