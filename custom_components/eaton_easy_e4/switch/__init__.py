"""Switch platform for eaton_easy_e4."""

from typing import TYPE_CHECKING

from .example_switch import ENTITY_DESCRIPTIONS, IntegrationBlueprintSwitch

# Acts on the device: the coordinator does not limit outbound calls.
PARALLEL_UPDATES = 1

if TYPE_CHECKING:
    from custom_components.eaton_easy_e4.data import IntegrationBlueprintConfigEntry
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant,
    entry: IntegrationBlueprintConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the switch platform."""
    async_add_entities(
        IntegrationBlueprintSwitch(entry.runtime_data.coordinator, description) for description in ENTITY_DESCRIPTIONS
    )
