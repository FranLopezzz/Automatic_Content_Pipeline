"""Stage 4: Multishot — Generate 10 shot variations using Gemini."""

import json


def execute(run_state, output_dir):
    """Generate 10 shot variations of the UGC scene.

    Uses Google Gemini (Nano Banana Pro) to create 10 different
    angles/compositions of the character with the product.

    Args:
        run_state: Current run state dict
        output_dir: Path to run output directory

    Returns:
        Updated run_state with stage="multishot" and shots populated
    """
    marca = run_state.get("brief", {}).get("marca_nombre", "unknown")
    print(f"[multishot] Generating 10 shot variations for {marca}...")

    # TODO: Replace with actual Gemini API call
    # genai = get_gemini_client()
    # model = genai.GenerativeModel("gemini-2.0-flash")
    # for i in range(10):
    #     response = model.generate_content([image, prompt_variation])
    #     shots.append(response.image_url)

    shots = [f"[STUB] shot_{i}_{run_state['id']}.png" for i in range(10)]

    shots_path = output_dir / "shots.json"
    with open(shots_path, "w", encoding="utf-8") as f:
        json.dump(shots, f, indent=2)

    run_state["stage"] = "multishot"
    run_state["shots"] = shots
    run_state["selected_shots"] = []

    print(f"[multishot] 10 variations generated for {marca}")
    return run_state
