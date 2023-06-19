

class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.worlds = plain_text.split(' ')
        self.tokens = {}

    def __getitem__(self, item):
        wt = self.WordToken()
        self.tokens[item] = wt
        return self.tokens[item]

    class WordToken:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize
    
    def __str__(self):
        result = []
        for i in range(len(self.worlds)):
            w = self.worlds[i]
            if i in self.tokens and w.capitalize:
                w = w.upper()
            result.append(w)
        return ' '.join(result)

if __name__ == '__main__':
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence)
