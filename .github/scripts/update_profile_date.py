from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re


readme = Path(__file__).resolve().parents[2] / "README.md"
original = readme.read_text(encoding="utf-8")
today = datetime.now(ZoneInfo("Asia/Shanghai"))
date_text = f"Today is {today:%B} {today.day}, {today.year}."
updated, count = re.subn(
    r"(?<=<!-- PROFILE_DATE_START -->).*?(?=<!-- PROFILE_DATE_END -->)",
    date_text,
    original,
    flags=re.DOTALL,
)
if count != 1:
    raise SystemExit("Expected exactly one profile date section in README.md.")
if updated != original:
    readme.write_text(updated, encoding="utf-8")
print(date_text)
