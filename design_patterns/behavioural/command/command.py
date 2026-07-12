from abc import ABC, abstractmethod


# Receiver classes - Light and AC with basic on/off methods
class Light:
    def on(self):
        print("Light turned ON")

    def off(self):
        print("Light turned OFF")


class AC:
    def on(self):
        print("AC turned ON")

    def off(self):
        print("AC turned OFF")


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete command for Light ON
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


# Concrete command for Light OFF
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# Concrete command for AC ON
class AConCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.on()

    def undo(self):
        self.ac.off()


# Concrete command for AC OFF
class ACOffCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.off()

    def undo(self):
        self.ac.on()


# Remote control (Invoker)
class RemoteControl:
    def __init__(self):
        self.buttons = [None, None, None, None]  # Four slots for commands
        self.command_history = []

    def set_command(self, slot, command):
        self.buttons[slot] = command

    def press_button(self, slot):
        if self.buttons[slot]:
            self.buttons[slot].execute()
            self.command_history.append(self.buttons[slot])

    def press_undo(self):
        if self.command_history:
            self.command_history.pop().undo()
        else:
            print("No commands to undo.")


def main():
    light = Light()
    ac = AC()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    ac_on = AConCommand(ac)
    ac_off = ACOffCommand(ac)

    remote = RemoteControl()
    remote.set_command(0, light_on)
    remote.set_command(1, light_off)
    remote.set_command(2, ac_on)
    remote.set_command(3, ac_off)

    remote.press_button(0)  # Light ON
    remote.press_button(2)  # AC ON
    remote.press_button(1)  # Light OFF
    remote.press_undo()  # Undo Light OFF -> Light ON
    remote.press_undo()  # Undo AC ON -> AC OFF


if __name__ == "__main__":
    main()
