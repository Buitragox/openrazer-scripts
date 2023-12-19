from openrazer.client import DeviceManager
from openrazer.client.devices import RazerDevice

device_manager = DeviceManager()
amount_devices = len(device_manager.devices)
print(f"Found {amount_devices} Razer devices")

for device in device_manager.devices:
    print("-----------------------------------------")
    device: RazerDevice
    print(device.name)
    print("Is charging:", device.is_charging)
    print(f"Battery: {device.battery_level}%")
