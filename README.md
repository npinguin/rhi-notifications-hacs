# RHI Notifications

Native and qualified domain event discovery, rule-independent event history, contextual incident inbox and rule editing, native notify entities and legacy notify actions with persistent delivery status, guarded actions and reminders, and reviewed migration preview/import.

## Installation

1. Add `https://github.com/npinguin/rhi-notifications-hacs` as a custom Integration repository in HACS. Enable prereleases and select the published TEST version.
2. Back up Home Assistant, install, restart, and add **RHI Notifications** in Settings → Devices & services.
3. Open the dashboard editor → Add card → RHI Notifications. The card is loaded automatically using the native HA frontend module API; refresh the browser after installation. No manual resource or YAML required. The integration option can disable UX for headless use; explicitly disabled existing entries stay disabled.

Supported TEST: HA OS/Container 2026.11.1, 64-bit amd64 or arm64 (CPython 3.14 musl). No mandatory Foundation. Submission is not proof of receipt. Physical mobile action callbacks, TV/visual receipt, Frigate playback and full mixed-product/site acceptance remain under test. Keep existing Basic configuration.

## License

See bundled notices for protected TEST permission and third-party licenses.
