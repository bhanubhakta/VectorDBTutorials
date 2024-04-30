from collections import defaultdict
import re


def bagOfWords(vocab, documents):
    vocabIndexMap = {word.strip().lower(): index for index,
                     word in enumerate(vocab)}

    bagOfWordsVec = [0] * len(vocab)

    wordFreq = defaultdict(int)

    for doc in documents:
        doc = re.sub(r'[^\w\s]', '', doc)
        words = doc.split(" ")
        for word in words:
            word = word.strip().lower()
            wordFreq[word] += 1

    for word, freq in wordFreq.items():
        index = vocabIndexMap.get(word, -1)
        count = wordFreq[word]
        if index > -1:
            bagOfWordsVec[index] = count

    return bagOfWordsVec


vocab = "a, am, and, anywhere, are, be, boat, box, car, could, dark, do, eat, eggs, fox, goat, good, green, ham, here, house, I, if, in, let, like, may, me, mouse, not, on, or, rain, Sam, say, see, so, thank, that, the, them, there, they, train, tree, try, will, with, would, you"
vocab = vocab.split(",")
documents = ["I would not like them here or there.", "I would not like them anywhere.",
             "I do not like green eggs and ham.", "I do not like them., Sam-I-am."]

print(bagOfWords(vocab, documents))
