"""Stage 3: Hero — Generate Morpheus fashion scene using ComfyDeploy."""


def execute(run_state, output_dir):
    """Generate hero scene with Morpheus Fashion Design.

    Creates the main scene where the character interacts with the brand product.

    Args:
        run_state: Current run state dict
        output_dir: Path to run output directory

    Returns:
        Updated run_state with stage="hero" and hero_url populated
    """
    marca = run_state.get("brief", {}).get("marca_nombre", "unknown")
    print(f"[hero] Generating Morpheus scene for {marca}...")

    # TODO: Replace with actual ComfyDeploy API call
    # headers = get_comfydeploy_headers()
    # response = requests.post(COMFY_DEPLOY_URL, headers=headers, json={
    #     "deployment_id": MORPHEUS_DEPLOYMENT_ID,
    #     "inputs": { "portrait": portrait_url, "product": product_image }
    # })

    hero_url = f"[STUB] hero_{run_state['id']}.png"
    hero_path = output_dir / "hero_stub.txt"
    hero_path.write_text(f"Hero scene placeholder for {marca}", encoding="utf-8")

    run_state["stage"] = "hero"
    run_state["hero_url"] = hero_url

    print(f"[hero] Morpheus scene generated for {marca}")
    return run_state
