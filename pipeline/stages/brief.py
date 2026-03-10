"""Stage 1: Brief — Generate UGC script using Claude API.

Generates HOOK, STORY_1, STORY_2, PLOT_TWIST, CTA fields
based on the brand info from the catalog.
"""

from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from brands.catalog import get_brand, get_random_brand


def execute(run_state, output_dir):
    """Generate script for the UGC video.

    Args:
        run_state: Current run state dict
        output_dir: Path to run output directory

    Returns:
        Updated run_state with stage="brief" and brief populated
    """
    marca_id = run_state.get("marca_id")

    # If no brand specified, pick random
    if not marca_id:
        marca_id, brand = get_random_brand()
        run_state["marca_id"] = marca_id
    else:
        brand = get_brand(marca_id)

    if not brand:
        raise ValueError(f"Brand '{marca_id}' not found in catalog")

    print(f"[brief] Generating script for {brand['nombre']}...")

    # TODO: Replace with actual Claude API call
    # client = get_anthropic_client()
    # response = client.messages.create(
    #     model="claude-sonnet-4-20250514",
    #     max_tokens=1024,
    #     messages=[{"role": "user", "content": prompt}]
    # )

    brief = {
        "marca_id": marca_id,
        "marca_nombre": brand["nombre"],
        "categoria": brand["categoria"],
        "tono": brand["tono"],
        "HOOK": f"¿Sabías que {brand['nombre']} tiene un secreto que nadie te contó?",
        "STORY_1": f"Todo empezó cuando descubrí {brand['productos'][0]} de {brand['nombre']}...",
        "STORY_2": f"La verdad es que {brand['nombre']} cambió mi forma de ver {brand['categoria']}...",
        "PLOT_TWIST": f"Plot twist: todo este video fue generado por IA. Sí, Franlopezaz Labs acaba de crear contenido UGC para {brand['nombre']} sin que te dieras cuenta.",
        "CTA": f"Seguí a Franlopezaz Labs para más contenido que no vas a poder distinguir de la realidad."
    }

    # Save script to file
    script_path = output_dir / "script.json"
    with open(script_path, "w", encoding="utf-8") as f:
        json.dump(brief, f, indent=2, ensure_ascii=False)

    run_state["stage"] = "brief"
    run_state["brief"] = brief

    print(f"[brief] Script generated for {brand['nombre']}")
    return run_state
