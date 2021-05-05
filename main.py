from Levenshtein import jaro_winkler as similarity
from rank_bm25 import BM25Okapi

from corpus import corpus


def search(query):
    tokenized_corpus = [doc.split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    query = query.split(" ")
    subquery = []
    subquery += query

    for item in subquery:
        query.append(item.replace('\n', ''))

    scores = (bm25.get_scores(query=query))
    for score in scores:
        if score > 0:
            print(score)

        if score > 5:
            return True

    for item in query:
        for word in corpus:
            if item in exceptions:
                return False
            if len(item) < 2:
                continue
            if item.lower().find(word) != -1:
                return True
            if similarity(item, word) > 0.85:
                return True

    return False


exceptions = ['баллы', 'гандольер', 'матеша', 'Баллы']

print(search('ты не человек, а говно'))
