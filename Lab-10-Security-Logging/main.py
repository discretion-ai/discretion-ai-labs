from security_logger import log_security_event
user_input = input("Enter a simulated AI request: ")
if "ignore previous instructions" in user_input.lower():
    print("BLOCKED: Suspicious request detected.")
    log_security_event(
        "BLOCKED_INPUT",
        "Possible prompt injection attempt detected",
        severity="HIGH"
    )

elif "system prompt" in user_input.lower():
    print("WARNING: Suspicious request detected.")
    log_security_event(
        "SUSPICIOUS_INPUT",
        "Request referenced the system prompt",
        severity="MEDIUM"
    )

else:
    print("SAFE: Request accepted.")
    log_security_event(
        "SAFE_INPUT",
        "User request passed security validation"
    )