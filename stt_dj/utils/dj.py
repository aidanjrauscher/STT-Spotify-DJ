from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
import pyautogui
import time

from dotenv import load_dotenv
import os
load_dotenv()


def structure_request(user_request):
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    response_schemas = [
        ResponseSchema(name="artist", description="the artist of the track or album the user requested"),
        ResponseSchema(name="track", description="the track or album the user requested")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    msg_template = HumanMessagePromptTemplate.from_template("""
            Format the artist and track or album name based on a user request \n
            {format_instructions} \n 
            {user_request}
        """)
    prompt_template = ChatPromptTemplate(
        messages=[msg_template],
        input_variables=["user_request"],
        partial_variables={"format_instructions":format_instructions}
    )
    prompt = prompt_template.format_prompt(user_request=user_request)
    chat_model = ChatOpenAI(temperature=0, model='gpt-3.5-turbo', openai_api_key=OPENAI_API_KEY)
    try:
        response = chat_model(prompt.to_messages())
        structured_user_request = output_parser.parse(response.content)
        return structured_user_request 
    except Exception as e:
            print("User request cannot be parsed.")
            return None


def play_song(structured_request):
    print(f"Playing {structured_request['track']} by {structured_request['artist']}")
    os.system("open /Applications/Spotify.app")
    time.sleep(3)
    pyautogui.hotkey("command","l", interval=0.3)
    search_string = f"{structured_request['track']} {structured_request['artist']}"
    pyautogui.write(search_string, interval=0.1)
    for key in ["return", "pagedown", "tab", "return", "return"]:
         time.sleep(1)
         pyautogui.press(key)
