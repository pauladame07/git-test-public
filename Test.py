import requests
import json

API_KEY = "0e9393db-27c2-46fd-b013-4f9f7864338a"

def generate_image(model_id, prompt):
    url = f"https://api.tryleap.ai/api/v1/images/models/{model_id}/inferences"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {API_KEY}"
    }
    data = {
        "prompt": prompt,
        "steps": 50,
        "width": 512,
        "height": 512,
        "numberOfImages": 1,
        "seed": 4523184
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = json.loads(response.text)
    inference_id = response_data['id']
    print(f"Inference ID: {inference_id}. Status: {response_data['status']}")
    image_url = response_data['output']['url']
    image_response = requests.get(image_url)
    image = image_response.content
    return inference_id, response_data['status'], image

# example usage
model_id = "9eb2997f-a563-4455-96cf-c241f2a2cf1a"
prompt = "A photo of a cat with a hat"
inference_id, status, image = generate_image(model_id, prompt)
# do something with the generated image
print(image)