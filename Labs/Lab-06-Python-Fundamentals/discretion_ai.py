business = "Discretion AI"
model = "Local AI"

print(f"{business} is starting...")
print(f"AI model: {model}")

def greet_user(name):
    print(f"Welcome to {business}, {name}!")

name = input("Enter your name: ")
greet_user(name)

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult user detected")
else:
    print("Minor user detected")

models = ["Llama", "Mistral", "Gemma" ]
print("Available AI Models:")
for model in models:
    print(model)

selected_model = input("Select an AI model: ").capitalize()
if selected_model in models:
    print(f"You selected: {selected_model}")
else:
    print("That model is not available.")

model_info = {
    "name": selected_model,
    "type": "Local LLM",
    "status": "Ready"
}

print("Model Information:")
print(model_info)

print(f"Model Name: {model_info['name']}")
print(f"Model Type: {model_info['type']}")
print(f"Model Status: {model_info['status']}")

print("\n--- Discretion AI Launcher ---")

if model_info["status"] == "Ready":
    print(f"Starting {model_info['name']}...")
    print(f"Model type: {model_info['type']}")
    print("Local AI system is ready.")
else:
    print("Model cannot be started.")
    