"""Read-only diagnostics; do not export events, recipients or household identifiers."""
import json
from pathlib import Path


async def async_get_config_entry_diagnostics(hass, entry):
    version = await hass.async_add_executor_job(
        lambda: json.loads(Path(__file__).with_name("manifest.json").read_text())["version"])
    from .frontend import ux_diagnostics
    health=entry.runtime_data.status()
    return {"ux": ux_diagnostics(hass, entry), "identity":{"domain":"rhi_notifications","version":version},
            "health":health,"configuration":{"mode":"pilot"},
            "build_handoff":{"foundation_required":False},
            "execution":{"external_delivery":health["external_delivery"]},"publication":{"contract":"candidate_v1","cutover_ready":False}}
