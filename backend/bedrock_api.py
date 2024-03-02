# allows call to Bedrock
import os
import json
import boto3

session = boto3.session.Session()
AWS_REGION = session.region_name

session = boto3.Session(
    profile_name=os.environ.get("BWB_PROFILE_NAME")
) #sets the profile name to use for AWS credentials

bedrock = session.client(
    service_name='bedrock-runtime', #creates a Bedrock client
    region_name=os.environ.get("BWB_REGION_NAME"),
    endpoint_url=os.environ.get("BWB_ENDPOINT_URL")
) 


bedrock_model_id = "anthropic.claude-v2:1" 

prompt = "Human: How do I take care of a plant?\Assistant:" #the prompt to send to the model

body_bedrock = json.dumps({
    "prompt": prompt,
    "max_tokens_to_sample": 300,
    "temperature": 0.5,
    "top_k":250,
    "top_p":1,
    "stop_sequences": []
}) 

response = bedrock.invoke_model(
    body = body_bedrock,
    contentType='application/json',
    accept='application/json',
    modelId= bedrock_model_id
)

response_body = json.loads(response.get('body').read()) 

response_text = response_body.get("completion")

