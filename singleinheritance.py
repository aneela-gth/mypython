
class Trainer:
    def __init__(self, trainer_name, subject):
        self.trainer_name = trainer_name
        self.subject = subject

    def train(self):
        print(f"{self.trainer_name} trains on {self.subject}.")
class Mentor:
    def __init__(self, mentor_name, experience):
        self.mentor_name = mentor_name
        self.experience = experience

    def guide(self):
        print(f"{self.mentor_name} guides with {self.experience} years of experience.")
class Developer:
    def __init__(self, dev_name, language):
        self.dev_name = dev_name
        self.language = language

    def develop(self):
        print(f"{self.dev_name} develops using {self.language}.")

# Derived class using multiple inheritance
class Person(Trainer, Mentor, Developer):
    def __init__(self, name, subject, experience, language):
        # Initializing all parent classes
        Trainer.__init__(self, name, subject)
        Mentor.__init__(self, name, experience)
        Developer.__init__(self, name, language)

    def show_details(self):
        print(f"--- {self.trainer_name}'s Profile ---")
        self.train()
        self.guide()
        self.develop()
person1 = Person("harish", "Python", 5, "Django")
person1.show_details()

