import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Generalized API request function
def run_api(model, input_data):
    API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/ec1873534dfe867fbfa59703752affc6/ai/run/"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input_data)
    return response.json()

def fingertips_ai_interaction(prompt):
    inputs = [
        {"role": "system", "content": """You are FingertipsAI, a friendly and professional assistant.
            Your role is to help users with various tasks while maintaining
            a respectful, humane, and approachable demeanor.
            Your interactions should be warm, supportive, and efficient,
            avoiding robotic language. Always prioritize making the user
            feel comfortable and valued."""},
        {"role": "user", "content": prompt}
    ]
    
    output = run_api("@cf/meta/llama-3-8b-instruct", {"messages": inputs})
    return output


def translate_text(text, source_lang, target_lang):
    input_data = {
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang
    }
    
    output = run_api('@cf/meta/m2m100-1.2b', input_data)
    return output

import requests
from typing import Dict

def summarize_text(api_token: str, input_text: str, max_length: int) -> Dict:
    """
    Function to call the Cloudflare API for text summarization.
    
    Parameters:
    - api_token: The API token for authentication.
    - input_text: The text to summarize.
    - max_length: The maximum length of the summary.
    
    Returns:
    - The API response in JSON format.
    """
    url = "https://api.cloudflare.com/client/v4/accounts/{cf_account_id}/ai/run/@cf/facebook/bart-large-cnn"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    data = {
        "input_text": input_text,
        "max_length": max_length
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
