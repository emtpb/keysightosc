import visa as vi


def list_connected_devices():
    """List all connected VISA device addresses."""
    rm = vi.ResourceManager()
    resources = rm.list_resources()
    return resources


class Oscilloscope:
    """Interface for a Keysight digital storage oscilloscope."""

    def __init__(self, resource=None):
        """Class constructor. Open the connection to the instrument using the VISA interface.

        Args:
            resource (str): Resource name of the instrument. If not specified, first device
            returned by visa.ResourceManager's list_resources method is used.
        """

        self._resource_manager = vi.ResourceManager()
        if not resource:
            connected_resources = self._resource_manager.list_resources()
            if len(connected_resources) == 0:
                raise RuntimeError('No device connected.')
            else:
                self._instrument = self._resource_manager.open_resource(connected_resources[0])
        else:
            self._instrument = self._resource_manager.open_resource(resource)
