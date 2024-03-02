import os
from langchain.llms.bedrock import Bedrock


def get_text_response(input_content): #text-to-text client function

    llm = Bedrock( #create a Bedrock llm client
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id="cohere.command-text-v14", #set the foundation model
        model_kwargs={
            "max_tokens": 512,
            "temperature": 0,
            "p": 0.01,
            "k": 0,
            "stop_sequences": [],
            "return_likelihoods": "NONE"
        }
    )
    
    return llm.predict(input_content) #return a response to the prompt

