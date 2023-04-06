import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_haiku(list_of_words):
    prompt = f"Create a haiku that incorporates the following words: {list_of_words}" \
    + f"begin the response with the following title 'Your Haiku says: ' "
    return prompt


list_join = ', '.join(input('Enter space-separated words to include in Haiku: ').split())
haiku = generate_haiku(list_join)

response = openai.Completion.create(engine='text-davinci-003', prompt=haiku, max_tokens=512, temperature=0.7)

print(response['choices'][0]['text'])

