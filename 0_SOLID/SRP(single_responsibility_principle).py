class Journal:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        self.entries.remove(pos)

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self):
    #     pass

    # def load_from_web(self):
    #     pass


class PersistanceManager:

    @staticmethod
    def save (journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I cried to day')
j.add_entry('I ate a bug')
# j.save('journal_27_04_23.txt')
print(f'Journal Entries: \n {j}')

file = 'journal_27_04_23.txt'
PersistanceManager.save(j, file)

with open(file) as f:
    print(f.read())
