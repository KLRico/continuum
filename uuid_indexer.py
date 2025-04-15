import uuid
import json
from pathlib import Path
from datetime import datetime

# Define root repo directory
repo_root = Path("/mnt/data/continuum_repo/continuum-main")

# File types to include
include_extensions = {".md", ".txt"}

# Collect metadata for each relevant file
index = []

for path in repo_root.rglob("*"):
    if path.suffix.lower() in include_extensions and path.is_file():
        file_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, str(path.relative_to(repo_root))))
        file_metadata = {
            "uuid": file_uuid,
            "title": path.stem.replace("_", " ").title(),
            "path": str(path.relative_to(repo_root)),
            "type": path.parts[-2] if len(path.parts) > 1 else "misc",
            "tags": [],
            "created": datetime.fromtimestamp(path.stat().st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat()
        }
        index.append(file_metadata)

# Save to index.json
index_path = repo_root / "index.json"
with open(index_path, "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2)

index_path
