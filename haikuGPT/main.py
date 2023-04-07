import openai
import os 
import webbrowser
from dotenv import load_dotenv

# load OpenAI API Key from the .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Functions
def generate_haiku(list_of_words):
    """
    Takes in a list of words and passes it as an argument to create the OpenAI API prompt 
    that generates a Haiku, which incorporates the list of words.

    Args:
        list_of_words (str): A list of words that are user-inputted.

    Returns:
        str: A prompt to be used to generate the Haiku
    """

    prompt = f"Create a haiku that incorporates the following words: {list_of_words}" \
    + "Additionally, generate an appropriate title for the Haiku and begin the response \
    with 'HaikuGPT presents ' then add the title after that"
    return prompt


def extract_title(title):
    """
    Extracts the title generated by HaikuGPT from the result_text string.

    Args:
        result_text (str): The response string from OpenAI API.

    Returns:
        str: The title of the Haiku generated by HaikuGPT.
    """
    # Find the index of the colon that separates the prompt from the title
    colon_index = result_text.find(':')

    # If the colon is not found, return None
    if colon_index == -1:
        return None

    # Extract the title after the colon and remove any leading or trailing whitespace
    title = result_text[colon_index+1:].strip()

    return title

def dalle2_prompt(title):
    """
    Takes in the title of the Haiku to act as the prompt for dalle2 image generation

    Args:
        title (str): title of the Haiku obtained from extract_title() function

    Returns:
        str: A prompt to be used to guide the style of the image generation
    """
    prompt = f"{title}, abstract, creative, art"
    return prompt

# Convert user input to list and call generate_haiku() function
user_input = input("Enter the words you want in the Haiku separated by commas: ")
input_list = user_input.split(",")
input_list = [x.strip() for x in input_list]
haiku = generate_haiku(input_list)

# Pass in the prompt to the openai function and store response 
response = openai.Completion.create(engine='text-davinci-003', prompt=haiku, max_tokens=512, temperature=0.7)
result_text = response['choices'][0]['text']

# generate image based on title
image_response = openai.Image.create(
    prompt=dalle2_prompt(extract_title(result_text)),
    n=1,
    size='1024x1024')

# display the generated Haiku and image
print(result_text)

image_url = image_response['data'][0]['url']
webbrowser.open(image_url)
