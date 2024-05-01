from gensim.models import Word2Vec
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Sample sentences
sentences = [
    ['hello', 'world'],
    ['hello', 'cat'],
    ['hello', 'dog'],
    ['world', 'dog'],
    ['world', 'cat'],
    ['cat', 'dog']
]

# Train a Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=3, min_count=1, workers=4, sg=0)  # sg=0 uses CBOW model

# Access the word vector for "hello"
print("Vector for word 'hello':", model.wv['hello'])

# Find similar words to "hello"
print("Words similar to 'hello':", model.wv.most_similar('hello'))
