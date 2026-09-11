"""Binary sensor platform for eaton_easy_e4."""

from typing import TYPE_CHECKING

from .filter import ENTITY_DESCRIPTIONS, IntegrationBlueprintFilterSensor

# Read-only platform: the coordinator already serializes the fetch.
PARALLEL_UPDATES = 0

if TYPE_CHECKING:
    from custom_components.eaton_easy_e4.data import IntegrationBlueprintConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant,
    entry: IntegrationBlueprintConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the binary_sensor platform."""
    async_add_entities(
        IntegrationBlueprintFilterSensor(entry.runtime_data.coordinator, description)
        for description in ENTITY_DESCRIPTIONS
    )
