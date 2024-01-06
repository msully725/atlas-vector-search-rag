from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
import key_param

client = MongoClient(key_param.MONGO_URI)
dbName = "langchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]

# Define the text embedding model
embeddings = OpenAIEmbeddings(openai_api_key=key_param.openai_api_key)


def mongoQueryVectorSearch(query):
    return [
        {
            "$vectorSearch": {
                "queryVector": embeddings.embed_query(query),
                "path": "embedding",
                "numCandidates": 2,
                "index": "vector_index",
                "limit": 1
            }
        }
    ]

def vector_search_data(query):
    # Convert question to vector using OpenAI embeddings
    vectorSearchQuery = embeddings.embed_query(query)
    cursor = collection.aggregate(vectorSearchQuery)
    docs = list(cursor)
    as_output = docs[0]['text']
    print(as_output)

vector_search_data('Who is Goku?')