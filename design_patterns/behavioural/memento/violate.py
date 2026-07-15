# Originator class: stores the current state of the resume
class ResumeEditor:
    def __init__(self):
        self.name = ""
        self.education = ""
        self.experience = ""
        self.skills = []


# ResumeSnapshot acts like a memento, but isn't encapsulated properly
class ResumeSnapshot:
    def __init__(self, editor):
        # Constructor: captures the current state from ResumeEditor
        self.name = editor.name
        self.education = editor.education
        self.experience = editor.experience
        self.skills = editor.skills.copy()  # Deep copy

    def restore(self, editor):
        # Restore function: applies the stored state back to ResumeEditor
        editor.name = self.name
        editor.education = self.education
        editor.experience = self.experience
        editor.skills = self.skills.copy()  # Deep copy


# Main driver to demonstrate snapshot creation and restoration
def main():
    editor = ResumeEditor()
    editor.name = "Alice"
    editor.education = "B.Tech in CS"
    editor.experience = "2 years at ABC Corp"
    editor.skills = ["Java", "SQL"]

    # Step 1: Create a snapshot before making changes
    snapshot = ResumeSnapshot(editor)

    # Step 2: Modify the resume
    editor.name = "Alice Johnson"
    editor.skills.append("Spring Boot")

    print("After changes:")
    print("Name:", editor.name)
    print("Skills:", editor.skills)

    # Step 3: Restore previous state using snapshot
    snapshot.restore(editor)

    print("\nAfter undo:")
    print("Name:", editor.name)
    print("Skills:", editor.skills)


if __name__ == "__main__":
    main()
