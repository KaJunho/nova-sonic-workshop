import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")
modelId = 'amazon.nova-pro-v1:0'

prompt = "AWSについて教えて"

messages = [
    {
        "role": "user",
        "content": [{"text": prompt}],
    }
]

inferenceConfig = {
    "temperature": 0.1,
    "topP": 0.9,
    "maxTokens": 500,
    "stopSequences":[]
}

response = client.converse(
    modelId=modelId ,
    messages=messages,
    inferenceConfig=inferenceConfig
)

print(response["output"]["message"]["content"][0]["text"])