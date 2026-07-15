# Originator with Memento inside
class ResumeEditor:
    def __init__(self):
        self._name = ""
        self._education = ""
        self._experience = ""
        self._skills = []

    def setName(self, name):
        self._name = name

    def setEducation(self, education):
        self._education = education

    def setExperience(self, experience):
        self._experience = experience

    def setSkills(self, skills):
        self._skills = skills

    def printResume(self):
        print("x:----- Resume -----")
        print("Name:", self._name)
        print("Education:", self._education)
        print("Experience:", self._experience)
        print("Skills:", self._skills)
        print("x:------------------")

    # Save the current state as a Memento
    def save(self):
        return self.Memento(
            self._name, self._education, self._experience, self._skills.copy()
        )

    # Restore state from Memento
    def restore(self, memento):
        self._name = memento.getName()
        self._education = memento.getEducation()
        self._experience = memento.getExperience()
        self._skills = memento.getSkills()

    # Inner Memento class
    class Memento:
        def __init__(self, name, education, experience, skills):
            self.__name = name
            self.__education = education
            self.__experience = experience
            self.__skills = skills

        def getName(self):
            return self.__name

        def getEducation(self):
            return self.__education

        def getExperience(self):
            return self.__experience

        def getSkills(self):
            return self.__skills


# Caretaker
class ResumeHistory:
    def __init__(self):
        self.history = []

    def save(self, editor):
        self.history.append(editor.save())

    def undo(self, editor):
        if self.history:
            editor.restore(self.history.pop())


# Main driver
def main():
    editor = ResumeEditor()
    history = ResumeHistory()

    editor.setName("Alice")
    editor.setEducation("B.Tech CSE")
    editor.setExperience("Fresher")
    editor.setSkills(["Java", "DSA"])
    history.save(editor)

    editor.setExperience("SDE Intern at TUF+")
    editor.setSkills(["Java", "DSA", "LLD", "Spring Boot"])
    history.save(editor)

    editor.printResume()  # Shows updated experience
    print()

    history.undo(editor)
    editor.printResume()  # Shows resume after one undo
    print()

    history.undo(editor)
    editor.printResume()  # Shows resume after second undo (initial state)


if __name__ == "__main__":
    main()
