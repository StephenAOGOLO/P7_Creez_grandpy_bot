class Sentence():

    THE_SENTENCES = [
        {'id': 1, 'sentence': 'my first sentence', 'status': 'OK'},
        {'id': 2, 'sentence': 'my second sentence', 'status': 'KO'},
        {'id': 3, 'sentence': 'my third sentence', 'status': 'KO'},
        {'id': 4, 'sentence': 'my fourth sentence', 'status': 'OK'}
    ]

    @classmethod
    def all(cls):
        return cls.THE_SENTENCES

    @classmethod
    def find(cls, id):
        return cls.THE_SENTENCES[int(id) - 1]