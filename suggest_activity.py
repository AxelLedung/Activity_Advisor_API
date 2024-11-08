import pandas as pd
from gpt4all import GPT4All
import time
import os
import json

project_path = os.path.dirname(os.path.abspath(__file__))
models_directory_path = os.path.join(project_path, "models") 
model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
model_path = os.path.join(models_directory_path, model_name)

model = GPT4All(model_path, allow_download=False)

def get_prompt(index_area, index_question):

    json_structure = {
        "introduction": "",
        "conclusion": "",
        "activities": [
            {
                "title": "",
                "description": ""
            },
            {
                "title": "",
                "description": ""
            },
            {
                "title": "",
                "description": ""
            }
        ]   
    }

    activity_dict = {
        "Effektivitet": [
            "Använder resurser på bästa sätt",
            "Beslutsprocessen",
            "Gemensamt mål",
            "Planerar vårt arbete"
        ],
        "Delaktighet": [
            "Arbetssituation",
            "Kommentera på information",
            "Påverka beslut",
            "Påverka hur",
            "Påverka vad",
            "Tillräckligt med befogenheter"
        ],
        "Arbetsrelaterad utmattning": [
            "Känslomässigt tömd",
            "Trött",
            "Utsliten"
        ],
        "Medarbetarskap": [
            "Ansvar för kompetens",
            "Ansvar informerad",
            "Initiativ till förändring",
            "Öppen för förändring"
        ],
        "Återkoppling": [
            "Kommunicerat vad som förväntas",
            "Konstruktiv dialog",
            "Positiv feedback"
        ],
        "Medarbetarkraft": [
            "Irritation",
            "Koncentrationsvårigheter",
            "Oro",
            "Rastlöshet",
            "Uppgivenhet"
        ],
        "Lärande i arbetet": [
            "Arbete utveklande",
            "Kompetenser tas tillvara",
            "Utvecklas yrkesmässigt"
        ],
        "Arbetstakt": [
            "Fundera",
            "Genomföra",
            "Planera",
            "Reflektera"
        ],
        "Målkvalitet": [
            "Påverkningsbara",
            "Realistiska",
            "Tydliga",
            "Uppföljningsbara"
        ],
        "Ledarskap": [
            "Förklara hur vi ska nå målen",
            "Konsekvent agerande",
            "Tydlig kommunikation"
        ],
        "Socialt klimat": [
            "God sammanhållning",
            "Kollegor ställer upp",
            "Positiv stämning"
        ],
    }
    
    text_prompt = f"""Skriv endast på svenska. Ge tre förslag på aktiviteter en avdelning kan göra för att förbättra:
        {index_area} om många av de anställda har svarat att följande kategori är ett problem: {index_question}.
        Lägg till en inledning och slutsats. Mata in all text i denna json string: {json_structure}
        Returnera endast json strängen UTAN en beskrivning, anteckning eller kommentar innan eller efter json strängen.
        """
    with model.chat_session():
        prompt = model.generate(text_prompt, max_tokens=4096)
    return prompt

def get_activity_advice_as_json(index_area, index_question):

    directory_path = "promptfiles"
    file_path = f"{directory_path}/{index_area}_{index_question}.txt"

    os.makedirs(directory_path, exist_ok=True)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            text = file.read()
    else:
        text = get_prompt(index_area, index_question)
        save_to_file(index_area, index_question, text)
            
    json_object = parse_json(text)

    return json_object

def clean_json_string(json_string):
    # Remove trailing periods or other extraneous characters
    json_string = json_string.strip().rstrip('.')

    # Add a missing closing brace if possible
    if json_string.count('{') > json_string.count('}'):
        json_string += '}'
    elif json_string.count('[') > json_string.count(']'):
        json_string += ']'

    return json_string

def parse_json(json_string):
    json_string = clean_json_string(json_string)
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        print("JSON format issue, attempting to auto-correct.")
        # Additional handling or manual correction could go here if needed
        return None
    
def run_all_prompts(activity_dict):
    for index_area in activity_dict:
        print(f"{index_area} started!")
        for question in activity_dict[index_area]:

            text = get_prompt(index_area, question)
            save_to_file(index_area, question, text)

            time.sleep(0.1)
            print(f"- {question} is completed!")

def save_to_file(index_area, question, text):
    directory_path = "promptfiles"
    file_path = f"{directory_path}/{index_area}_{question}.txt"
    os.makedirs(directory_path, exist_ok=True)

    # Find the first occurrence of '{' and the last occurrence of '}'
    start = text.find('{')
    end = text.rfind('}')

    # Extract the substring
    if start != -1 and end != -1:
        extracted_text = text[start:end + 1]
    else:
        extracted_text = "Couldn't find a json format in the string."

    with open(file_path, 'w') as file:
        file.write(extracted_text)

