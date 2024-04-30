import numpy as np
from collections import defaultdict, Counter
from itertools import combinations
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
# Example text corpus
text = "The quick brown fox jumps over the lazy dog. The quick fox is quick."

# Tokenize the text
tokens = word_tokenize(text.lower())

# Vocabulary construction
vocab = list(set(tokens))
vocab_index = {word: i for i, word in enumerate(vocab)}

# Co-occurrence matrix setup
window_size = 2  # Define the context window size
co_occurrence_matrix = np.zeros((len(vocab), len(vocab)), dtype=np.float32)

# Build the co-occurrence matrix
for i in range(len(tokens)):
    token = tokens[i]
    left = tokens[max(i - window_size, 0):i]
    right = tokens[i + 1:i + 1 + window_size]
    context = left + right

    for cont_word in context:
        j = vocab_index[cont_word]
        k = vocab_index[token]
        co_occurrence_matrix[j][k] += 1

# Print the co-occurrence matrix
print("Vocabulary Index:", vocab_index)
print("Co-occurrence Matrix:\n", co_occurrence_matrix)
