# step1: setup GROQ API key
import os
import base64
from groq import Groq   # ✅ Correct import

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# step2: convert image to required format
def encode_image(image_path):
    image_file=open(image_path, "rb") 
    return  base64.b64encode(image_file.read()).decode("utf-8")

# step3: setup multimodal LLM
query = "placeholder for query"
model = model = "meta-llama/llama-4-scout-17b-16e-instruct"
  # ✅ vision model


def analyze_image_with_query(query, model, encoded_image, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)   # ✅ Correct class name

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
    )

    return chat_completion.choices[0].message.content

