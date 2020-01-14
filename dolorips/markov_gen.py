import io
import random


class Generator(object):

    def __init__(self, open_text=None, book=None, random_book=False):
        self.cache = {}
        self.book = book
        self.random_book = random_book
        self.open_book_file = open_text
        self.words = self._file_to_words()
        self.word_size = len(self.words)
        self._database()

    def _open_file(self):
        if not self.open_book_file:
            if not self.book and self.random_book:
                self.book = self._select_random_book()
            else:
                self.book = 'ELDERINCK'
            self.open_book_file = io.open(f'data/{self.book}.txt', encoding='utf-8')

    def _select_random_book(self):
        booklist = self.list_books()
        return random.choice(booklist)

    def _file_to_words(self):
        self._open_file()
        self.open_book_file.seek(0)
        data = self.open_book_file.read()
        words = data.split()
        return words

    def _triples(self):
        """ Generates triples from the given data string. So if our string were
                        "What a lovely day", we'd generate (What, a, lovely) and then
                        (a, lovely, day).
        """

        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    def _database(self):
        for w1, w2, w3 in self._triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def text(self, size=25):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ' '.join(gen_words)

    get_text=property(text)

    @staticmethod
    def list_books():
        return ['ELDERINCK',
                'PIMPERNEL',
                'REYNAERDE',
                'VEGETARISCH',
                'VONDEL',]
