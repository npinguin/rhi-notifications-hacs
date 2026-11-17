"""HA-native readiness entity and coalesced change indication; no second data store."""
from uuid import uuid4

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import callback
from homeassistant.helpers.event import async_call_later


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([PilotStatus(entry)], update_before_add=True)


class PilotStatus(SensorEntity):
    _attr_has_entity_name = True
    _attr_name = "RHI Notifications pilot status"
    _attr_icon = "mdi:bell"
    _attr_should_poll = False
    _unrecorded_attributes = frozenset({"rhi_notifications_update_token"})

    def __init__(self, entry):
        self._attr_unique_id = entry.entry_id + "_pilot_status"
        self.runtime = entry.runtime_data
        self._pending = None

    def _read_status(self):
        data = self.runtime.status()
        self._attr_native_value = data["state"]
        self._attr_extra_state_attributes = {k:v for k,v in data.items() if k != "state"}
        # Only an opaque invalidation token; scoped services still own all reads.
        self._attr_extra_state_attributes["rhi_notifications_update_token"] = uuid4().hex

    async def async_update(self):
        self._read_status()

    async def async_added_to_hass(self):
        await super().async_added_to_hass()
        self.runtime.status_listener = self._schedule
        self.async_on_remove(self._detach)
        self._read_status()

    @callback
    def _schedule(self):
        if self._pending is None:
            self._pending = async_call_later(self.hass, .2, self._publish)

    @callback
    def _publish(self, _now):
        self._pending = None
        self._read_status()
        self.async_write_ha_state()

    @callback
    def _detach(self):
        self.runtime.status_listener = None
        if self._pending is not None:
            self._pending()
            self._pending = None
