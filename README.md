# Activity Advisor API - LIA

## Overview

This is a simple Python API using Flask designed to Advise Activities. It provides a POST endpoint which takes Indexareas and return recommended activities to enhance the indexarea. 

## Features

- **Activity suggestions**: Suggest activities depending on which index area and index question that need action.

## Technologies Used

- Python 3.12
- GPT4All
- Meta-Llama-3-8B-Instruct
- Flask

## Getting Started

### Prerequisites

- Python 3.12

### Setup

1. Clone the repository:

   git bash
   ```bash
   git clone https://github.com/AxelLedung/Activity_Advisor_API.git
   ```
   Powershell
   ```powershell
   cd .\QOL_scripts
   ./setup.ps1
   ```

### API Endpoints

Below is a list of available API endpoints with their descriptions:

### Descriptions
- **POST** `/activity_advice?index_area=Effektivitet&index_question=Beslutsprocessen` - Retrieves a json-string with activity description for resolving issues with "Effektivitet" and "Beslutsprocessen".

### File Breakdown

1. **`main.py`** -  Entry point for the API.
2. **`suggest_activity.py`** - Uses the model to create prompt and convert the prompt into json structure for response.
4. **`/models`** - Used to store the model when downloaded via setup.ps1.
5. **`/promptfiles`** - Contains generated prompts for quicker loading.
6. **`/QOL_scripts`** - Contains scripts to setup dependencies, enviroment and models, and run the program using devmode and prodmode.
7. **`/activities`** - Stores started and completed activities for future suggestions (`.json` files).
