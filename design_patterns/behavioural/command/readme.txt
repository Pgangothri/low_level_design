C++
|
Java
|
Python
Introduction
Behavioral design patterns focus on how objects interact and communicate with each other, defining the flow of control in a system. These patterns make it easier to manage the interactions between objects, promoting loose coupling and enhancing flexibility.

Imagine a remote control that sends commands to various devices, like turning on the lights or adjusting the volume. The user doesn’t need to understand the internal workings of the devices, just the commands they can give. This is a perfect example of what behavioral patterns like the Command Pattern help us achieve.

The Command Pattern encapsulates a request as an object, allowing for more flexible and dynamic command handling. In the upcoming sections, we’ll dive deeper into how the Command Pattern works and how it can be applied in real-world scenarios.

Command Pattern
The Command Pattern is a behavioral design pattern that turns a request into a separate object, allowing you to decouple the code that issues the request from the code that performs it.
Formal Definition
The Command Pattern is a behavioral design pattern that encapsulates a request as an object, allowing for parameterization of clients with different requests, queuing of requests, and logging of the requests. It lets you add features like undo, redo, logging, and dynamic command execution without changing the core business logic.

This allows you to execute commands at a later time, in a flexible manner, without having to interact directly with the request's execution details.
Real-Life Analogy
Think of a remote control used to turn on or off the lights or an air conditioner (AC). When you press a button to turn on the lights or adjust the temperature, you don’t need to understand how the internal circuits work or how the AC receives the signal. You just press the "On" or "Off" button, and the remote control takes care of sending the command.

Similarly, the Command Pattern decouples the sender of a request (the remote control) from the receiver (the light or AC), providing flexibility and simplicity in handling commands.
Four Key Components
Client: Initiates the request and sets up the command object.
Invoker: Asks the command to execute the request.
Command: Defines a binding between a receiver object and an action.
Receiver: Knows how to perform the actions to satisfy a request.

Understanding the Problem
Let's say we're building a simple remote control system where devices like lights and air conditioner can be turned on and off. Here's a naive implementation of the code:
Python


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


# Invoker - NaiveRemoteControl class to control devices
class NaiveRemoteControl:
    def __init__(self, light, ac):
        self.light = light
        self.ac = ac
        self.last_action = ""

    # Command methods
    def press_light_on(self):
        self.light.on()
        self.last_action = "LIGHT_ON"

    def press_light_off(self):
        self.light.off()
        self.last_action = "LIGHT_OFF"

    def press_ac_on(self):
        self.ac.on()
        self.last_action = "AC_ON"

    def press_ac_off(self):
        self.ac.off()
        self.last_action = "AC_OFF"

    # Undo last action
    def press_undo(self):
        if self.last_action == "LIGHT_ON":
            self.light.off()
            self.last_action = "LIGHT_OFF"
        elif self.last_action == "LIGHT_OFF":
            self.light.on()
            self.last_action = "LIGHT_ON"
        elif self.last_action == "AC_ON":
            self.ac.off()
            self.last_action = "AC_OFF"
        elif self.last_action == "AC_OFF":
            self.ac.on()
            self.last_action = "AC_ON"
        else:
            print("No action to undo.")


def main():
    light = Light()
    ac = AC()
    remote = NaiveRemoteControl(light, ac)

    remote.press_light_on()
    remote.press_ac_on()
    remote.press_light_off()
    remote.press_undo()  # Should undo LIGHT_OFF -> Light ON
    remote.press_undo()  # Should undo AC_ON -> AC OFF

if __name__ == "__main__":
    main()

While the implementation works, it suffers from some significant issues.
Issues in the Code
1. Tight Coupling:
The NaiveRemoteControl class directly calls methods on the Light and AC classes. If additional devices need to be added in the future, changes will be required in the remote control class. This violates the open/closed principle, where classes should be open for extension but closed for modification.
2. Lack of Flexibility:
The commands are hardcoded in the remote control class. If new actions or different command sequences are required, modifying the remote control code is necessary, leading to potential maintenance challenges.
3. Undo Functionality:
The pressUndo method is tightly coupled with the commands. This makes it difficult to add more complex undo functionality, especially when dealing with multiple actions or a variety of devices.
4. Hardcoded Commands:
The remote control class directly defines commands like pressLightOn, pressACOn, etc. This makes the system rigid and difficult to modify. Adding new actions or commands would require changing the remote control code, leading to challenges in maintaining or extending the system.
5. Maintaining Command History:
The original approach doesn’t have a centralized mechanism to track previously executed commands. This leads to difficulties in implementing features like undo, where the last action needs to be reversed efficiently.

The Solution
The issues in the previous implementation can be addressed by using the Command Pattern. By applying this pattern, it becomes easier to encapsulate requests as objects, allowing for flexible and reusable command handling. The command pattern decouples the request sender (Invoker) from the receiver (Light/AC) and provides a unified way to handle multiple commands and actions.
Code Implementation:
Python


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
How Command Pattern Resolves the Issues
Issue	How Command Pattern Resolves the Issue
Tight Coupling	By using the Command Pattern, the RemoteControl class no longer directly interacts with the devices. It now interacts with command objects (e.g., LightOnCommand, ACOffCommand), which decouples the logic.
Lack of Flexibility	With the Command Pattern, new commands (e.g., for new devices or actions) can be created as new Command implementations without changing the RemoteControl class. This allows for easy extension.
Undo Functionality	The Command Pattern provides a consistent structure for undoing commands. Each concrete command (e.g., LightOnCommand, ACOffCommand) has its own undo() method, which allows easy reversal of actions.
Hardcoded Commands	The Command Pattern uses an interface for commands, which allows dynamic assignment of different commands to slots in the remote. This makes the command assignments flexible and customizable.
Maintaining Command History	The Command Pattern introduces a stack (commandHistory) in the RemoteControl class, which tracks previously executed commands. This makes the undo functionality centralized and easier to manage.
Conclusion
The Command Pattern effectively addresses tight coupling, lack of flexibility, and challenges in maintaining and reusing commands. By encapsulating requests into command objects, the system becomes more modular, extendable, and easier to maintain in the long term.

Suitable Scenarios for Command Pattern
Decoupling Sender from Receiver
Use the Command Pattern when there is a need to decouple the sender (Invoker) from the receiver (the object performing the action).
Undo/Redo Support
The Command Pattern is useful when you require built-in support for undoing or redoing actions.
Batch Operations
When multiple actions need to be executed as part of a batch (e.g., applying night mode), the Command Pattern allows easy implementation.
Plug-in Architecture
It facilitates the creation of flexible, extensible systems where new commands can be added without affecting the core system.
Creating Macros or Composite Commands
Use the pattern to group multiple commands together, enabling complex actions to be executed in sequence as a single macro.

Pros and Cons of the Command Pattern
Pros
Decouples Sender and Receiver
The sender (Invoker) and receiver (the device or action) are decoupled, allowing for flexibility and easier maintenance.
Supports Undo/Redo Functionality
The Command Pattern inherently supports undo and redo actions, allowing for easier management of state reversals.
Easily Extensible and Reusable
New commands can be added without modifying existing code, and commands can be reused across different parts of the application.
Cons
Increases the Number of Classes
Implementing the Command Pattern can result in a large number of small classes for each command, potentially increasing the complexity.
Can Add Unnecessary Complexity for Simple Tasks
For simple applications, the Command Pattern may introduce unnecessary complexity, making it harder to manage than simpler alternatives.
Requires Careful Design for Undo/Redo
Implementing undo/redo functionality correctly requires careful design and additional effort, especially for complex command chains.

Class Diagram


22





Command Pattern - Theory - TUF+