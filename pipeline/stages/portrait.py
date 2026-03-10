"""Stage 2: Portrait — Design character using ComfyDeploy Portrait Master."""


def execute(run_state, output_dir):
    """Generate character portrait for the UGC video.

    Uses ComfyDeploy Portrait Master to create a realistic
    AI-generated character that will be the "creator" in the video.

    Args:
        run_state: Current run state dict
        output_dir: Path to run output directory

    Returns:
        Updated run_state with stage="portrait" and portrait_url populated
    """
    marca = run_state.get("brief", {}).get("marca_nombre", "unknown")
    print(f"[portrait] Generating character for {marca}...")

    # TODO: Replace with actual ComfyDeploy API call
    # headers = get_comfydeploy_headers()
    # response = requests.post(COMFY_DEPLOY_URL, headers=headers, json={
    #     "deployment_id": PORTRAIT_DEPLOYMENT_ID,
    #     "inputs": { "prompt": character_prompt }
    # })

    portrait_url = f"[STUB] portrait_{run_state['id']}.png"
    portrait_path = output_dir / "portrait_stub.txt"
    portrait_path.write_text(f"Portrait placeholder for {marca}", encoding="utf-8")

    run_state["stage"] = "portrait"
    run_state["portrait_url"] = portrait_url

    print(f"[portrait] Character designed for {marca}")
    return run_state
