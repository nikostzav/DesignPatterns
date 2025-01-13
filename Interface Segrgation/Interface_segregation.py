
class Rechargeable:
    def recharge(self):
        raise NotImplementedError("Subclasses must implement the recharge method")

class Switchable:
    def turn_on(self):
        raise NotImplementedError("Subclasses must implement the turn_on method")
    
    def turn_off(self):
        raise NotImplementedError("Subclasses must implement the turn_off method")


class Smartphone(Rechargeable, Switchable):
    def recharge(self):
        print("Smartphone is recharging...")

    def turn_on(self):
        print("Smartphone is turning on...")

    def turn_off(self):
        print("Smartphone is turning off...")


class DesktopComputer(Switchable):
    def turn_on(self):
        print("Desktop Computer is turning on...")

    def turn_off(self):
        print("Desktop Computer is turning off...")


class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device: Switchable):
        self.devices.append(device)

    def manage_devices(self):
        for device in self.devices:
            device.turn_on()
            if isinstance(device, Rechargeable):
                device.recharge()
            device.turn_off()


if __name__ == "__main__":
  
    smartphone = Smartphone()
    desktop_computer = DesktopComputer()

 
    manager = DeviceManager()

   
    manager.add_device(smartphone)
    manager.add_device(desktop_computer)

  
    print("Managing devices:")
    manager.manage_devices()
