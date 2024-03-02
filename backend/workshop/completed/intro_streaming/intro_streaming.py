import os
import json
import boto3

session = boto3.Session(
    profile_name=os.environ.get("BWB_PROFILE_NAME")
) #sets the profile name to use for AWS credentials

bedrock = session.client(
    service_name='bedrock-runtime', #creates a Bedrock client
    region_name=os.environ.get("BWB_REGION_NAME"),
    endpoint_url=os.environ.get("BWB_ENDPOINT_URL")
)

def chunk_handler(chunk):
    print(chunk, end='')

def get_streaming_response(prompt, streaming_callback):

    bedrock_model_id = "anthropic.claude-v2:1" #set the foundation model

    body = json.dumps({
        "prompt": prompt, #ANTHROPIC
        "max_tokens_to_sample": 4000,
        "temperature": 0, 
        "top_k": 250, 
        "top_p": 1, 
        "stop_sequences": ["\n\nHuman:"] 
    })

    response = bedrock.invoke_model_with_response_stream(modelId=bedrock_model_id, body=body) #invoke the streaming method
    stream = response.get('body')
    if stream:
        for event in stream: #process each event returned by the stream
            chunk = event.get('chunk')
            if chunk:
                chunk_json = json.loads(chunk.get('bytes').decode())
                streaming_callback(chunk_json["completion"]) #pass the latest chunk's text to the callback method

prompt = "\n\nHuman:Tell me a story about two puppies and two kittens who became best friends\n\nAssistant:"
                
get_streaming_response(prompt, chunk_handler)

