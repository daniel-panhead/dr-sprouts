import os
from langchain.llms.bedrock import Bedrock

##################################################################

llm = Bedrock( #create a Bedrock llm client
    credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
    region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
    endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
    model_id="ai21.j2-ultra-v1" #set the foundation model
)

##################################################################

prompt = "What is the largest city in Vermont?"
    
response_text = llm.predict(prompt) #return a response to the prompt

print(response_text)
