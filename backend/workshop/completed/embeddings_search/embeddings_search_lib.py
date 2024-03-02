import os
from langchain.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders.csv_loader import CSVLoader


def get_index(): #creates and returns an in-memory vector store to be used in the application
    
    embeddings = BedrockEmbeddings(
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
    ) #create a Titan Embeddings client
    
    loader = CSVLoader(file_path="sagemaker_answers.csv")

    index_creator = VectorstoreIndexCreator(
        vectorstore_cls=FAISS,
        embedding=embeddings,
        text_splitter=CharacterTextSplitter(chunk_size=300, chunk_overlap=0),
    )

    index_from_loader = index_creator.from_loaders([loader])
    
    return index_from_loader
    

def get_similarity_search_results(index, question):
    results = index.vectorstore.similarity_search_with_score(question)
    
    flattened_results = [{"content":res[0].page_content, "score":res[1]} for res in results] #flatten results for easier display and handling
    
    return flattened_results


def get_embedding(text):
    embeddings = BedrockEmbeddings(
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
    ) #create a Titan Embeddings client
    
    return embeddings.embed_query(text)