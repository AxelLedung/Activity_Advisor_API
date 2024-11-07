# Activity Advisor API - Quicksearch AB

## Overview

This is a simple Python API using Flask designed to Advise Activities. It provides a POST endpoint which takes Indexareas and return recommended activities to enhance the indexarea. 

## Features

- **Localization**: Supports multi-language responses using `.resx` files.
- **Logging**: Integrated logging for Error Management.
- **Swagger Documentation**: Auto-generated API documentation using Swagger (Swashbuckle).

## Technologies Used

- Python 3.12
- Meta-Llama-3-8B-Instruct
- Flask

## Getting Started

### Prerequisites

- Python 3.12
- Meta-Llama-3-8B-Instruct

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/AxelLedung/Activity_Advisor_API.git

### API Endpoints

Below is a list of available API endpoints with their descriptions:

### Descriptions
- **POST** `/api/describe-graph/{jsonString}&{graphType}&{breakdownCode}&{timeCode}&{lang}` - Retrieves a description for the graph data.

### File Breakdown

1. **`appsettings.json`** - Contains configuration settings like connection strings and logging levels.
2. **`Program.cs`** - Entry point for the API. Configures services, middleware, and application settings.
4. **`/Controllers`** - Holds API controllers managing different resources (e.g., `GraphController`).
5. **`/Models`** - Contains data models used throughout the API (e.g., `Graph`, `GraphData`, `DescriptionData`).
6. **`/Services`** - Houses service classes responsible for logic and data manipulation.
7. **`/Resources`** - Stores localization files for supporting multiple languages (`.resx` files).
8. **`/Logs`** -- Logs the errors per date error occured.
