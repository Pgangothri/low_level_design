C++
|
Java
|
Python
Prototype Pattern
The Prototype Pattern is a creational design pattern used to clone existing objects instead of constructing them from scratch. It enables efficient object creation, especially when the initialization process is complex or costly.
Formal Definition:
"Prototype pattern creates duplicate objects while keeping performance in mind. It provides a mechanism to copy the original object to a new one without making the code dependent on their classes."

In simpler terms:
Imagine you already have a perfectly set-up object, like a configured game character or a ready-to-send email template. Instead of building a new one every time (which can be repetitive and expensive), you just copy the existing one and make small adjustments. This is what the Prototype Pattern does. It allows you to create new objects by copying existing ones, saving time and resources.
Real-life Analogy (Photocopy Machine)
Think of preparing ten offer letters. Instead of typing the same letter ten times, you write it once, photocopy it, and change just the name on each copy. This is how the Prototype Pattern works: start with a base object and produce modified copies with minimal changes.

Understanding
Let's understand better through a common challenge in software systems.

Consider an email notification system where each email instance requires extensive setup: loading templates, configurations, user settings, and formatting. Creating every email from scratch introduces redundancy and inefficiency.

Now imagine having a pre-configured prototype email, and simply cloning it for each user while modifying a few fields (like the name or content). That would save time, reduce errors, and simplify the logic.

Suitable Use Cases
Apply the Prototype Pattern in these situations:
Object creation is resource-intensive or complex.
You require many similar objects with slight variations.
You want to avoid writing repetitive initialization logic.
You need runtime object creation without tight class coupling.

Real-life Example
Imagine we're building a Email Template System at TUF:
Bad Code: Incomplete Use of Design Principles
Python


from typing import List

# A concrete email class with expensive setup
class WelcomeEmail:
    def __init__(self) -> None:
        # Subject is fixed for the template
        self.subject = "Welcome to TUF+"

        # Default content
        self.content = "Hi there! Thanks for joining us."

        # Simulate heavy initialization work (template parsing)
        self.template_tokens: List[str] = ["{name}", "{plan}", "{cta_link}"]

    def set_content(self, new_content: str) -> None:
        self.content = new_content

    def send(self, to: str) -> None:
        print(f"Sending to {to}: [{self.subject}] {self.content}")


def main() -> None:
    # Every variation rebuilds the same template again and again
    email1 = WelcomeEmail()
    email1.send("user1@example.com")

    email2 = WelcomeEmail()
    email2.set_content("Hi there! Welcome to TUF Premium.")
    email2.send("user2@example.com")

    email3 = WelcomeEmail()
    email3.set_content("Thanks for signing up. Let's get started!")
    email3.send("user3@example.com")


if __name__ == "__main__":
    main()
Issues in the Bad design
Repetitive initialization:
Template setup repeats for every instance.
This wastes time and increases chances of inconsistency.
No cloning mechanism:
We cannot reuse a pre-configured base template.
Each instance must be constructed from scratch.
Harder to scale:
More templates means more repeated construction code.

Good Code (Prototype Pattern Applied)
Python


from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List
import copy


# Prototype Interface
class EmailTemplate(ABC):
    @abstractmethod
    def clone(self) -> "EmailTemplate":
        pass

    @abstractmethod
    def set_content(self, content: str) -> None:
        pass

    @abstractmethod
    def send(self, to: str) -> None:
        pass


# Concrete Prototype
class WelcomeEmail(EmailTemplate):
    def __init__(self) -> None:
        # Fixed template subject
        self.subject = "Welcome to TUF+"

        # Default content
        self.content = "Hi there! Thanks for joining us."

        # Simulate heavy initialization work (template parsing)
        self.template_tokens: List[str] = ["{name}", "{plan}", "{cta_link}"]

        # Example nested config that must be deep-copied safely
        self.style: Dict[str, object] = {"font": "Inter", "size": 14}

    def clone(self) -> "EmailTemplate":
        # Deep copy is safer when objects hold nested mutable state
        return copy.deepcopy(self)

    def set_content(self, new_content: str) -> None:
        self.content = new_content

    def send(self, to: str) -> None:
        print(f"Sending to {to}: [{self.subject}] {self.content}")
        print(f"Style: font={self.style['font']}, size={self.style['size']}")


# Registry that stores prototypes and hands out clones
class EmailTemplateRegistry:
    def __init__(self) -> None:
        self._templates: Dict[str, EmailTemplate] = {}

    def register_template(self, template_type: str, prototype: EmailTemplate) -> None:
        self._templates[template_type] = prototype

    def get_template(self, template_type: str) -> EmailTemplate:
        # Always return a clone so the prototype stays unchanged
        return self._templates[template_type].clone()


def main() -> None:
    registry = EmailTemplateRegistry()

    # Register pre-configured prototype once
    registry.register_template("welcome", WelcomeEmail())

    # Clone and customize per user
    email1 = registry.get_template("welcome")
    email1.set_content("Hi Alice, welcome to TUF Premium!")
    email1.send("alice@example.com")

    print("---")

    email2 = registry.get_template("welcome")
    email2.set_content("Hi Bob, thanks for joining!")
    email2.send("bob@example.com")


if __name__ == "__main__":
    main()
Benefits of Good Design
Implements clone(): Creates a copy instead of reconstructing the object.
Introduces Registry: Central place stores prototypes and returns clones.
Decouples creation from usage: Client code does not depend on construction details.
Improves performance: Expensive setup happens once per prototype registration.

Deep Cloning VS Shallow Cloning
In Python, copying is explicit and you typically choose between:
Shallow copy: copies the object, but nested objects are still shared.
Deep copy: copies the object and also recursively copies nested objects.

In the context of Prototype Pattern, deep cloning is often preferred, especially when templates contain nested mutable objects like dictionaries, lists, or configuration objects. It ensures that changes in one clone do not accidentally affect the prototype or another clone.

In the good design above, clone() uses: copy.deepcopy(self)

Mutability Pitfalls While Cloning
Python makes it very easy to hold mutable state (lists, dicts, sets). That is powerful, but it also makes shallow cloning risky.

Good prototype implementations in Python usually follow these practices:
Prefer deep copy for templates: Especially when nested configs exist.
Be careful with default mutable arguments: Avoid patterns like def __init__(self, tags=[]).
Use __copy__ and __deepcopy__ for full control: If you want fine-grained copy behavior.

Pros of Prototype Pattern
Faster object creation: No need to reinitialize objects from scratch.
Cleaner code: Less repeated setup and fewer chances of mistakes.
Runtime customization: Clone and tweak per request.
Works naturally with registries: dict-based registries are simple in Python.

Cons of Prototype Pattern
Deep cloning can be expensive: deepcopy copies everything recursively.
Circular references need care: deepcopy handles many cycles, but custom objects can still complicate it.
Clone correctness depends on design: You must be intentional about what state is copied.

Class Diagram
The class diagram below illustrates the structure of the Prototype Pattern, showing how the various components interact with each other. Only the specification perspective is shown here, as the implementation perspective is not relevant for this pattern.



18





