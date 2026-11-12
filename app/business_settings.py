import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_FILE = PROJECT_ROOT / "business" / "settings.json"
DEFAULT_SETTINGS = {
    "brand_name": "Threadlane",
    "assistant_tone": "Warm, clear, and concise",
    "escalation_guidance": "If the supplied policies do not answer the question, tell the customer and direct them to a human support representative.",
    "policies": "",
    "order_lookup_enabled": True,
}


def get_business_settings() -> dict:
    if not SETTINGS_FILE.exists():
        return DEFAULT_SETTINGS.copy()
    stored = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    if not isinstance(stored, dict):
        raise ValueError("Business settings must be a JSON object.")
    return {**DEFAULT_SETTINGS, **stored}


def save_business_settings(settings: dict) -> dict:
    SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_file = SETTINGS_FILE.with_suffix(".tmp")
    temporary_file.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary_file.replace(SETTINGS_FILE)
    return settings