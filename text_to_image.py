import boto3
import json
import base64
import os
from datetime import datetime

def generate_images(prompt_text, num_images=1):
    # Initialize the Bedrock client
    bedrock = boto3.client(
        service_name='bedrock-runtime',
        region_name='us-east-1'  # Change this to your region
    )

    # Prepare the request body
    request_body = {
        "textToImageParams": {
            "text": prompt_text
        },
        "taskType": "TEXT_IMAGE",
        "imageGenerationConfig": {
            "cfgScale": 8,
            "seed": 42,
            "quality": "standard",
            "width": 1024,
            "height": 1024,
            "numberOfImages": num_images
        }
    }

    try:
        # Invoke the model
        response = bedrock.invoke_model(
            modelId="amazon.titan-image-generator-v2:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps(request_body)
        )

        # Parse the response
        response_body = json.loads(response['body'].read())
        
        # Save the generated images
        for idx, image_data in enumerate(response_body.get('images', [])):
            image_bytes = base64.b64decode(image_data)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_image_{timestamp}_{idx+1}.png"
            
            # Create directory if it doesn't exist
            os.makedirs('generated_images', exist_ok=True)

            for idx, image_data in enumerate(response_body.get('images', [])):
                image_bytes = base64.b64decode(image_data)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"generated_image_{timestamp}_{idx+1}.png"
                
                # Update filename with directory path before saving
                full_path = os.path.join('generated_images', filename)

                with open(full_path, 'wb') as f:
                    f.write(image_bytes)
                print(f"Saved image: {full_path}")

    except Exception as e:
        print(f"Error generating images: {str(e)}")

if __name__ == "__main__":
    # Example usage
    prompt = "A vibrant action scene of a kids' cricket match in a sunny park. Six children aged 8-12 wearing colorful cricket gear, two actively playing while others fielding. The batsman is in motion hitting the ball, bowler in mid-action. Natural lighting with sun casting soft shadows. Background shows lush green grass, mature trees, and clear blue sky. Crisp details in 4K quality, photorealistic style with natural colors and composition and images that do not conflict your AUP or AWS Responsible AI Policy."
    generate_images(prompt)