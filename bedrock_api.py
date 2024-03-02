# allows call to Bedrock
import os
import json
import boto3

session = boto3.session.Session()
AWS_REGION = session.region_name
from langchain.llms.bedrock import Bedrock

llm = Bedrock(
        region_name = AWS_REGION,
        model_kwargs={"max_tokens_to_sample":500,"temperature":0.95,"top_k":250,"top_p":0.999,"anthropic_version":"bedrock-2023-05-31"},
        model_id="anthropic.claude-v2"
    )

# creates Bedrock client

session = boto3.Session(
    profile_name=os.environ.get("BWB_PROFILE_NAME")
) #sets the profile name to use for AWS credentials

bedrock = session.client(
    service_name='bedrock-runtime', #creates a Bedrock client
    region_name=os.environ.get("BWB_REGION_NAME"),
    endpoint_url=os.environ.get("BWB_ENDPOINT_URL")
) 

# build payload for ID call

bedrock_model_id = "ai21.j2-ultra-v1" #set the foundation model

prompt = "What is the largest city in New Hampshire?" #the prompt to send to the model

body = json.dumps({
    "prompt": prompt, #AI21
    "maxTokens": 1024, 
    "temperature": 0, 
    "topP": 0.5, 
    "stopSequences": [], 
    "countPenalty": {"scale": 0 }, 
    "presencePenalty": {"scale": 0 }, 
    "frequencyPenalty": {"scale": 0 }
}) #build the request payload

# call API

response = bedrock.invoke_model(body=body, modelId=bedrock_model_id, accept='application/json', contentType='application/json') #send the payload to Bedrock

# display response

response_body = json.loads(response.get('body').read()) # read the response

response_text = response_body.get("completions")[0].get("data").get("text") #extract the text from the JSON response

print(response_text)
