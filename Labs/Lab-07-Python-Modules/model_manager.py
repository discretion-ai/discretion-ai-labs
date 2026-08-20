def get_models():
    models = ["Llama", "Mistral", "Gemma"]
    return models

def get_model_info(model_name):
    return {
        "name": model_name,
        "type": "Local LLM",
        "status": "Ready"
    }