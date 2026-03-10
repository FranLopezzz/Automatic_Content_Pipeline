"""API client wrappers for external services.

Each client is initialized lazily from environment variables.
Actual API calls are made in the stage modules.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_anthropic_client():
    """Get Anthropic client for Claude API (script generation)."""
    import anthropic
    return anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def get_gemini_client():
    """Get Google Generative AI client (multishot generation)."""
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    return genai


def get_elevenlabs_client():
    """Get ElevenLabs client (TTS / voice generation)."""
    from elevenlabs import ElevenLabs
    return ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))


def get_openai_client():
    """Get OpenAI client (fallback TTS)."""
    from openai import OpenAI
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_comfydeploy_headers():
    """Get headers for ComfyDeploy API calls."""
    return {
        "Authorization": f"Bearer {os.getenv('COMFY_DEPLOY_API_KEY')}",
        "Content-Type": "application/json"
    }


def get_postiz_headers():
    """Get headers for Postiz API calls."""
    return {
        "Authorization": f"Bearer {os.getenv('POSTIZ_API_KEY')}",
        "Content-Type": "application/json"
    }
