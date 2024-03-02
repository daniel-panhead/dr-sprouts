import sys
import os
from langchain.llms.bedrock import Bedrock


def get_text_response(input_content, temperature): #text-to-text client function
    
    model_kwargs = { #AI21
        "maxTokens": 1024, 
        "temperature": temperature, 
        "topP": 0.5, 
        "stopSequences": [], 
        "countPenalty": {"scale": 0 }, 
        "presencePenalty": {"scale": 0 }, 
        "frequencyPenalty": {"scale": 0 } 
    }
    
    llm = Bedrock( #create a Bedrock llm client
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id="ai21.j2-ultra-v1",
        model_kwargs = model_kwargs
    )
    
    return llm.predict(input_content) #return a response to the prompt


for i in range(3):
    response = get_text_response(sys.argv[1], float(sys.argv[2]))
    print(response)
