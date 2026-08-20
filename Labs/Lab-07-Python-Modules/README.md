# Lab 07 - Python Modules

## Objective

Learn how to organize Python code into separate modules and import functions between files.

## What I Built

This lab separates the Discretion AI model-management logic from the main application.

### model_manager.py

Contains reusable functions that:

- Return available AI models
- Return information about a selected model
- Store model name, type, and status

### main.py

The main application:

1. Imports functions from model_manager.py
2. Displays available local AI models
3. Allows the user to select a model
4. Passes the selected model to the model manager
5. Displays information about the selected model

## Example

Available models: ['Llama', 'Mistral', 'Gemma']

Select a model: Mistral

Selected model:
{'name': 'Mistral', 'type': 'Local LLM', 'status': 'Ready'}

## Concepts Practiced

- Python modules
- Importing functions
- Functions
- Lists
- Dictionaries
- User input
- Separating application logic into multiple files

## Discretion AI Connection

This lab introduces modular application design.

Future versions of Discretion AI can use separate modules for model management, document processing, security controls, RAG, and interaction with local Ollama models.