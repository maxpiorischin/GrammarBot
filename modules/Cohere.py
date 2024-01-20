import os
import requests
from dotenv import load_dotenv

load_dotenv()
cohere_key = os.environ.get("COHERE")
cohere_api = "https://api.cohere.ai/v1/generate"
headers = {
    'Authorization': f'Bearer {cohere_key}',
    'Content-Type': 'application/json'
}

def api_post(prompt):
    data = {
        "prompt": prompt,
        "truncate": "END",
        "return_likelihoods": "NONE"
    }
    response = requests.post(cohere_api, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['generations'][0]['text']
    else:
        return f"Error making api request, status code {response.status_code}"

def get_translation(language, message):
    prompt = f"Given the following message, provide the exact translation to {language}, and do not say anything else other than the translation : {message}"
    return api_post(prompt)


def get_corrected_grammar(message):
    prompt = f"Given the following message, please correct the grammar and do not say anything else but the corrected grammar: {message}"
    return api_post(prompt)
