# Create the UUID resolver function scaffold

import hashlib

# Load index.json
with open(index_path, 'r', encoding='utf-8') as f:
    index_data = json.load(f)

# Map UUID to metadata for fast lookup
uuid_lookup = {entry['uuid']: entry for entry in index_data}

# UUID resolver function
def resolve_uuid(uuid_string):
    entry = uuid_lookup.get(uuid_string)
    if not entry:
        return {"error": "UUID not found"}
    
    file_path = repo_root / entry["path"]
    if not file_path.exists():
        return {"error": "File not found"}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return {
        "uuid": uuid_string,
        "metadata": entry,
        "content": content
    }

# Example: resolve the first UUID
example_uuid = index_data[0]['uuid']
resolved_packet = resolve_uuid(example_uuid)
resolved_packet.keys()  # Show structure
