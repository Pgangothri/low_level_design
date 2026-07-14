# Class representing a User in a collaborative document editor
class User:
    def __init__(self, name):
        self.name = name
        self.others = []  # List of users that have access to this user

    # Method to add a collaborator to this user (grants access to the user)
    def addCollaborator(self, user):
        self.others.append(user)

    # Method to make a change to the document and notify all collaborators
    def makeChange(self, change):
        print(f"{self.name} made a change: {change}")
        for u in self.others:
            u.receiveChange(change, self)  # Notify each collaborator about the change

    # Method to receive a change notification from another user
    def receiveChange(self, change, from_user):
        print(f"{self.name} received: \"{change}\" from {from_user.name}")


# Client Code
if __name__ == "__main__":
    # Creating users
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Adding collaborators (Alice gives access to Bob and Charlie)
    alice.addCollaborator(bob)
    alice.addCollaborator(charlie)

    # Alice makes a change, notifying Bob and Charlie
    alice.makeChange("Updated the document title")

    # Bob makes a change, but no collaborators are
    # notified because Bob has no collaborators added
    bob.makeChange("Added a new section to the document")
