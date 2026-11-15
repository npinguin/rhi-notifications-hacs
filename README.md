# RHI Notifications

Native and qualified domain event discovery, incident inbox, acknowledgement, history, rules, native notify entities and legacy notify actions with persistent delivery status.

## Installation

1. Add `https://github.com/npinguin/rhi-notifications-hacs` as a custom Integration repository in HACS. Enable prereleases and select the published TEST version.
2. Back up Home Assistant, install, restart, and add **RHI Notifications** in Settings → Devices & services.
3. Enable optional UX in integration options. Add `/rhi_notifications/frontend/notifications-card.js` as a JavaScript module dashboard resource and add a card with `type: custom:rhi-notifications-card` to an existing view.

Supported TEST: HA OS/Container 2026.11.1, 64-bit amd64 or arm64 (CPython 3.14 musl). No mandatory Foundation. Submission is not proof of receipt. Mobile action callbacks, specialized recipient policy, full mixed-package and physical device acceptance remain unqualified. Keep existing Basic configuration.

## License

See bundled notices for protected TEST permission and third-party licenses.
