"""Morfeo UGC Engine — Character Prebuild

Pre-generates character portraits for faster pipeline execution.
Useful for building a pool of characters before scheduled runs.

Usage:
    python prebuild.py --count 5
    python prebuild.py --marca havanna
"""

import argparse
import json
from pathlib import Path
from datetime import datetime

from brands.catalog import get_brand, get_random_brand, list_brands


OUTPUT_DIR = Path(__file__).parent.parent / "output" / "prebuilt"


def prebuild_character(marca_id=None):
    """Pre-generate a character portrait for a brand."""
    if marca_id:
        brand = get_brand(marca_id)
        if not brand:
            print(f"[prebuild] Brand '{marca_id}' not found")
            return None
    else:
        marca_id, brand = get_random_brand()

    print(f"[prebuild] Generating character for {brand['nombre']}...")

    # TODO: Replace with actual ComfyDeploy Portrait Master call
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    char_dir = OUTPUT_DIR / f"{marca_id}_{timestamp}"
    char_dir.mkdir(parents=True, exist_ok=True)

    metadata = {
        "marca_id": marca_id,
        "marca_nombre": brand["nombre"],
        "created_at": datetime.utcnow().isoformat() + "Z",
        "portrait_url": f"[STUB] prebuilt_{marca_id}_{timestamp}.png"
    }

    meta_path = char_dir / "metadata.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print(f"[prebuild] Character for {brand['nombre']} saved to {char_dir}")
    return metadata


def main():
    parser = argparse.ArgumentParser(description="Morfeo Character Prebuild")
    parser.add_argument("--count", type=int, default=1, help="Number of characters to generate")
    parser.add_argument("--marca", help="Specific brand ID")

    args = parser.parse_args()

    for i in range(args.count):
        prebuild_character(args.marca)
        print(f"[prebuild] {i+1}/{args.count} done")


if __name__ == "__main__":
    main()
