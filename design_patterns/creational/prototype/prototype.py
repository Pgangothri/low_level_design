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
