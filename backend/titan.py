import boto3
import json
import os


session = boto3.Session(
    profile_name=os.environ.get("dr-sprout")
) 

bedrock = session.client(
    service_name='bedrock-runtime', #creates a Bedrock client
    region_name=os.environ.get("BWB_REGION_NAME"),
    endpoint_url=os.environ.get("BWB_ENDPOINT_URL")
) 

bedrock_model_id = "amazon.titan-text-express-v1" #set the foundation model

prompt = "What is the largest city in New Hampshire?" #the prompt to send to the model

body = json.dumps({
    "modelId": "amazon.titan-text-express-v1",
    "contentType": "application/json",
    "accept": "application/json",
    "body": prompt
}) #build the request payload


response = bedrock.invoke_model(body=body, modelId=bedrock_model_id, accept='application/json', contentType='application/json') #send the payload to Bedrock

response_body = json.loads(response.get('body').read()) # read the response

response_text = response_body.get("completions")[0].get("data").get("text") #extract the text from the JSON response

def response():
    return response_text




# api_call = {
#     "modelId": "amazon.titan-text-express-v1",
#     "contentType": "application/json",
#     "accept": "application/json",
#     "body": "{\"inputText\":\"this is where you place your input text\",\"textGenerationConfig\":{\"maxTokenCount\":8192,\"stopSequences\":[],\"temperature\":0,\"topP\":1}}"
# }

# The Temperature parameter allows the model to be more "creative" when constructing a response. A temperature of 0 means no randomness - the most likely words are chosen each time. To get more variability in responses, you can set the Temperature value higher and run the same request several times.
# The Response length parameter determines the number of tokens to be returned in the response. You can use this to shorten or increase the amount of content returned by the model. If you set the length too low, you might cut off the response before it is completed.
# You can use the Info links to see an explanation of each parameter.