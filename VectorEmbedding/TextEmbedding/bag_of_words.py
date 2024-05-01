from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "the sky is blue",
    "the sun is bright",
    "the sun in the sky is bright",
    "we can see the shining sun the bright sun."
]

# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the documents

bag_of_words = vectorizer.fit_transform(documents)

# Get feature names to use as dataframe column headers
feature_names = vectorizer.get_feature_names_out()

# Create the pandas DataFrame
import pandas as pd
df = pd.DataFrame(bag_of_words.toarray(), columns=feature_names)

print(df)