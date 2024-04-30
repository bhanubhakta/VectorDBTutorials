from pymilvus import model

ef = model.DefaultEmbeddingFunction()

openAiEf = model.dense.OpenAIEmbeddingFunction(
    model_name="text-embedding-3-large",
    api_key="sk-proj-sFTBg8QIbwk04A6CyLTqT3BlbkFJ2a3I4S4UQQKAQ5HfQ5VB",
    dimensions=100
)

# sk-proj-sFTBg8QIbwk04A6CyLTqT3BlbkFJ2a3I4S4UQQKAQ5HfQ5VB

# result = [0] * 5

# result.append(1)
# result.append(2)
docs = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]

embeddings = openAiEf.encode_documents(docs)
print("Embeddings from Open AI:", embeddings)
print("Shape:", type(embeddings))
# , "tree in ocean"
# embeddings = ef.encode_documents(docs)
# print("Embeddings:", embeddings)
