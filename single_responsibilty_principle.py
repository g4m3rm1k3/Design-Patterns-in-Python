# SRP SOC
# Single Responsibilty Principle/ Separation of Concerns

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f'{self.count}: {text}')
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


j = Journal()
j.add_entry("Chest workout")
j.add_entry("Math homework")
print(f"Journal entries:\n{j}")
