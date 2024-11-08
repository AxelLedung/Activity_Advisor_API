import pandas as pd
import os
import shutil
from gpt4all import GPT4All

# Path to your local .gguf model file
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
models_directory_path = os.path.join(project_path, "models") 
model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
model_path = os.path.join(models_directory_path, model_name)

os.makedirs(models_directory_path, exist_ok=True)

default_cache_path = os.path.expanduser("~/.cache/gpt4all/")
default_model_path = os.path.join(default_cache_path, model_name)

if not os.path.exists(model_path):
    if not os.path.exists(default_model_path):
        print("Downloading the model to default cache...")
        model = GPT4All(model_name)

    if os.path.exists(default_model_path):
        print("Copying model to project models directory...")
        shutil.copy(default_model_path, model_path)
        print("Done!")
else:
    print("Model already exists in project folder.")