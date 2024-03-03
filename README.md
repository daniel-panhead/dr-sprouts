<p align="center">
  <img width="105" height="115" src="https://github.com/daniel-panhead/dr-sprouts/assets/57362494/4f488e66-8586-42a6-aa15-e5720f6b8eff">
</p>

# Ask Dr. Sprouts!

Does your plant look diseased, and you don’t know what to do? Dr. Sprouts is a plant disease diagnosis tool that tells you what might be wrong!

## Under the Hood

We are using AWS Bedrock, backed by the Anthropic Claude 2.1 LLM, to generate responses to queries. In addition, in order to reinforce our answers,
we are using Amazon Knowledge Base to provide the LLM with scientific papers about plant diseases and symptoms. This allows Dr. Sprouts to provide answers backed by real scientific research.

In order to serve the app, we are using a Python FastAPI backend to interface with AWS Bedrock and React.js for our frontend interface.

Save your plants today!
