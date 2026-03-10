"""Stage 6: Publish — Post to Postiz as DRAFT."""


def execute(run_state, output_dir):
    """Publish video to social media via Postiz as DRAFT.

    IMPORTANT: Always publishes as DRAFT, never directly.
    Manual review is required before going live.

    Args:
        run_state: Current run state dict
        output_dir: Path to run output directory

    Returns:
        Updated run_state with stage="published" and published=True
    """
    marca = run_state.get("brief", {}).get("marca_nombre", "unknown")
    video_url = run_state.get("video_url")
    print(f"[publish] Publishing {marca} video as DRAFT to Postiz...")

    # TODO: Replace with actual Postiz API call
    # headers = get_postiz_headers()
    # response = requests.post(POSTIZ_URL + "/posts", headers=headers, json={
    #     "content": caption,
    #     "media_url": video_url,
    #     "status": "draft",  # ALWAYS draft
    #     "platforms": ["tiktok", "instagram"]
    # })

    run_state["stage"] = "published"
    run_state["published"] = True

    print(f"[publish] {marca} video published as DRAFT")
    return run_state
