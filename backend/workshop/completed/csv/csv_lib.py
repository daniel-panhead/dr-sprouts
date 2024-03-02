import os
import pandas as pd
from io import StringIO
from langchain.llms.bedrock import Bedrock

#

def get_llm():

    llm = Bedrock( #create a Bedrock llm client
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id="ai21.j2-ultra-v1", #use the AI21 Jurassic-2 Ultra model
        model_kwargs = {"maxTokens": 1024, "temperature": 0.0 } #for data extraction, minimum temperature is best
    )

    return llm

#

def validate_and_return_csv(response_text):
    #returns has_error, response_content, err 
    try:
        csv_io = StringIO(response_text)
        return False, pd.read_csv(csv_io), None #attempt to load response CSV into a dataframe
    
    except Exception as err:
        return True, response_text, err

#

def get_csv_response(input_content): #text-to-text client function
    
    llm = get_llm()

    response = llm.predict(input_content) #the text response for the prompt
    
    return validate_and_return_csv(response)

