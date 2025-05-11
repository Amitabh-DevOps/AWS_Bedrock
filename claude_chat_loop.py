import boto3
import json
import base64

# Initialize Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def send_to_claude(messages):
    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": messages
    }

    try:
        response = bedrock.invoke_model(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps(request_body)
        )
        response_body = json.loads(response['body'].read())
        return response_body["content"][0]["text"]
    except Exception as e:
        return f"[Error] {str(e)}"

def main():
    messages = []
    image_path = input("Enter image path (or leave empty to skip): ").strip()
    
    if image_path:
        try:
            encoded = encode_image(image_path)
            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",  # or "image/png"
                            "data": encoded
                        }
                    },
                    {
                        "type": "text",
                        "text": "What's in this image?"
                    }
                ]
            })
            reply = send_to_claude(messages)
            print(f"Claude: {reply}")
            messages.append({"role": "assistant", "content": [{"type": "text", "text": reply}]})
        except Exception as e:
            print(f"[Image Error] {str(e)}")
    
    print("\nStart chatting with Claude (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        messages.append({
            "role": "user",
            "content": [{"type": "text", "text": user_input}]
        })
        reply = send_to_claude(messages)
        print(f"Claude: {reply}")
        messages.append({"role": "assistant", "content": [{"type": "text", "text": reply}]})

if __name__ == "__main__":
    main()
