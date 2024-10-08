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

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("Chest workout")
j.add_entry("Math homework")
print(f"Journal entries:\n{j}")

file = "./journal.txt"
PersistanceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
