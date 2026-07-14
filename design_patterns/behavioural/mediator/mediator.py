
# Mediator Interface
class DocumentSessionMediator:
    def broadcastChange(self, change, sender):
        pass

    def join(self, user):
        pass


# Concrete Mediator Class
class CollaborativeDocument(DocumentSessionMediator):
    def __init__(self):
        self.users = []

    def join(self, user):
        self.users.append(user)

    def broadcastChange(self, change, sender):
        for user in self.users:
            if user != sender:
                user.receiveChange(change, sender)


# User Class
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    # Method for users to make a change
    def makeChange(self, change):
        print(f"{self.name} edited the document: {change}")
        self.mediator.broadcastChange(change, self)

    # Method to receive a change from another user
    def receiveChange(self, change, sender):
        print(f"{self.name} saw change from {sender.name}: \"{change}\"")


# Client Code
if __name__ == "__main__":
    doc = CollaborativeDocument()

    # Creating users
    alice = User("Alice", doc)
    bob = User("Bob", doc)
    charlie = User("Charlie", doc)

    # Joining the collaborative document
    doc.join(alice)
    doc.join(bob)
    doc.join(charlie)

    # Users making changes
    alice.makeChange("Added project title")
    bob.makeChange("Corrected grammar in paragraph 2")
