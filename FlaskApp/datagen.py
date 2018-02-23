import random
import string


def datagen():
    data = "".join(random.choice(string.ascii_lowercase) for _ in xrange(100))
    return data


def article():
    data = datagen()
    articles = [
                {id: 1,
                 'title': 'Article-1',
                 'content': data}]
    return articles
