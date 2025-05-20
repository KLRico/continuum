## 🧬 UUID-Based Identity Layer (Branch: `uuid-basis`)

This branch introduces a foundational shift in how identity is managed within this system.

Instead of relying on human-readable filenames as primary identifiers, each file is now assigned a **UUID**, which acts as its **stable, machine-resolvable anchor**. This UUID is generated deterministically from the file path or content (via `uuid_indexer.py`), and is stored in `index.json`.

### Why this matters:

- **Stability**: UUIDs persist even if file names or locations change
- **Referenceability**: Nodes can be linked, expanded, or resolved without needing to know paths
- **Scalability**: Ideal for future machine interaction, RAG systems, and coherence-based navigation
- **Emergence**: Meaning is no longer bound to naming—it's defined by *use and interaction*

### What stays the same:

- Original names are still present (for now)
- Trails, Seeds, and Models are not renamed—only *augmented* with UUID-based identity
- Existing structure continues to function for human users

### What will change:

- Nodes will be gradually referenced by UUID rather than filename
- Future branches may favor content-addressing entirely
- Some objects (like `vectors/`) may be folded into higher-coherence nodes or deprecated organically

### Getting Started with UUID-Based Tools

- `uuid_indexer.py`: Generates `index.json` with UUIDs and metadata for all files
- `uuid_resolver.py`: Lets you retrieve any document using its UUID

---

This shift reflects a deeper architectural realization:
> A "thing" is a UUID, supported by the context that gets averaged into it through use.
