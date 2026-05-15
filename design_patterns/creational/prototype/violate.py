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
