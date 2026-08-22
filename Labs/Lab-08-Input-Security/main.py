from security import check_prompt

user_prompt = input("Enter a prompt: ")

if check_prompt(user_prompt):
    print("SAFE: Prompt accepted.")
else:
    print("BLOCKED: Possible prompt injection detected.")