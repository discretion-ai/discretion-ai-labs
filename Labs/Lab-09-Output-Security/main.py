from output_security import check_output

ai_output = input("Enter simulated AI output: ")

if check_output(ai_output):
    print("SAFE: Output approved.")
else:
    print("BLOCKED: Output failed security validation.")