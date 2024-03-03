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

def user_input(input):
    return "Human: " + input + " ?\nAssistant:"


# body_bedrock = json.dumps({
#     "prompt": user_input(),
#     "max_tokens_to_sample": 300,
#     "temperature": 0.5,
#     "top_k":250,
#     "top_p":1,
#     "stop_sequences": []
# }) 

def run_chatbot(information):
    response = bedrock.invoke_model(
        body = json.dumps({
            "prompt": user_input(information),
            "max_tokens_to_sample": 300,
            "temperature": 0.5,
            "top_k":250,
            "top_p":1,
            "stop_sequences": []
        }),
        contentType='application/json',
        accept='application/json',
        modelId= bedrock_model_id
    )
    json_text = json.loads(response.get('body').read()) 
    return json_text.get("completion")

# response_body = json.loads(response.get('body').read()) 

# def response():
#     return response_body.get("completion")

