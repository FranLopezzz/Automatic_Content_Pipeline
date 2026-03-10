"""Stage 5: Video — Generate lip-synced video with TTS audio."""

import json


def execute(run_state, output_dir):
    """Generate final video with lip-sync and TTS audio.

    Uses ElevenLabs for TTS, then assembles video clips
    with lip-sync using ffmpeg.

    Args:
        run_state: Current run state dict
        output_dir: Path to run output directory

    Returns:
        Updated run_state with stage="video" and video_url populated
    """
    marca = run_state.get("brief", {}).get("marca_nombre", "unknown")
    selected = run_state.get("selected_shots", [0, 2, 4, 6, 8])
    print(f"[video] Generating video for {marca} with shots {selected}...")

    # TODO: Replace with actual ElevenLabs + ffmpeg pipeline
    # 1. Generate TTS audio for each script section
    # client = get_elevenlabs_client()
    # audio = client.text_to_speech.convert(
    #     text=full_script, voice_id="...", model_id="eleven_multilingual_v2"
    # )
    #
    # 2. Create lip-synced clips with VEED Fabric
    # 3. Concatenate clips with ffmpeg
    # ffmpeg -i clip1.mp4 -i clip2.mp4 ... -filter_complex concat=n=5 output.mp4

    video_url = f"[STUB] final_{run_state['id']}.mp4"
    video_path = output_dir / "video_stub.txt"
    video_path.write_text(f"Video placeholder for {marca}", encoding="utf-8")

    # Save video metadata
    meta = {
        "marca": marca,
        "selected_shots": selected,
        "video_url": video_url,
        "duration_seconds": 50,
        "format": "vertical_9_16"
    }
    meta_path = output_dir / "video_meta.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    run_state["stage"] = "video"
    run_state["video_url"] = video_url

    print(f"[video] Video generated for {marca}")
    return run_state
