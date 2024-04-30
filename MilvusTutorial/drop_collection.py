from milvus_client import MelvisClient

client = MelvisClient().client

client.drop_collection(
    collection_name="quick_setup"
)

client.drop_collection(
    collection_name="customized_setup"
)


# Recaps
# There are two ways to create a collection.
# The first is the quick setup, which only
# requires you to provide a name and the
# dimension of the vector field.
# The second is the customized setup,
# which allows you to customize almost
# every aspect of the collection.

# The data insertion process may take some time to complete.
# It is recommended to wait a few seconds after
# inserting data and before conducting similarity searches.

# Filter expressions can be used in both search
# and query requests. However, they are mandatory for query requests.

# 1. Access layer
# 2. Coordination service includes root coordinator, data coordinator
# 	 and query coordinator
# Milvus cluster includes eight microservice components and three
# third-party dependencies. All microservices can be deployed on Kubernetes
# independently from each other
#
