import os
from langchain.llms.bedrock import Bedrock

def get_titan_response(model, input_content, temperature, top_p, max_token_count, stop_sequence): #text-to-text client function
    
    model_kwargs = { #For the LangChain Bedrock implementation, these parameters will be added to the textGenerationConfig item that LangChain creates for us
        "maxTokenCount": max_token_count, 
        "stopSequences": [stop_sequence],
        "temperature": temperature, 
        "topP": top_p
    }
    
    llm = Bedrock( #create a Bedrock llm client
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id=model, #use the requested model
        model_kwargs = model_kwargs
    )
    
    return llm.predict(input_content) #return a response to the prompt

