from model_manager import get_models, get_model_info

models = get_models()
print("Available models:", models)

selected_model = input("Select a model: ")
model_info = get_model_info(selected_model)

print("Selected model:", model_info)