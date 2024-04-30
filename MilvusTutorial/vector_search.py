from milvus_client import MelvisClient

client = MelvisClient().client

query_vectors = [
    [0.041732933, 0.013779674, -0.027564144, -0.013061441, 0.009748648]
]

# "Artificial intelegence"

res = client.search(
    collection_name="quick_setup",
    data=query_vectors,
    limit=3
)
# print("Result with single vector:", res)


# Bulk-vector search

query_vectors = [
    [0.041732933, 0.013779674, -0.027564144, -0.013061441, 0.009748648],
    [0.0039737443, 0.003020432, -0.0006188639, 0.03913546, -0.00089768134]
]

res = client.search(
    collection_name="quick_setup",
    data=query_vectors,
    limit=3
)
# print("Result with Bulk vector search", res)


# # Filtered searches

query_vectors = [
    [0.041732933, 0.013779674, -0.027564144, -0.013061441, 0.009748648]
]

res = client.search(
    collection_name="quick_setup",
    data=query_vectors,
    filter="500 < id < 800",
    limit=3
)
# print("Filtered searches:", res)


# # With non-schema-defined fields
query_vectors = [
    [0.041732933, 0.013779674, -0.027564144, -0.013061441, 0.009748648]
]

res = client.search(
    collection_name="quick_setup",
    data=query_vectors,
    filter='$meta["color"] like "red%"',
    limit=3,
    output_fields=["color"],
)

# print("With non-schema defined fields:", res)

res = client.query(
    collection_name="quick_setup",
    filter="10 < id < 15",
    output_fields=["color"]
)
# print(res)

res = client.get(
    collection_name="quick_setup",
    ids=[1, 2, 3],
    output_fields=["color", "vector"]
)
print(res)
