from milvus_client import MelvisClient

client = MelvisClient().client

res = client.delete(
    collection_name="quick_setup",
    ids=[12]
)

print("Result:", res)

# Delete entities by filter
res = client.delete(
    collection_name="quick_setup",
    filter="id in [5,6,7,8,9]"
)
print(res)
