import re

def check_output(ai_output):
    MAX_OUTPUT_LENGTH = 1000

    if len(ai_output) > MAX_OUTPUT_LENGTH:
        return False

    sensitive_terms = [
        "password",
        "api_key",
        "secret key",
        "access token",
        "private key"
    ]

    clean_output = ai_output.lower()

    for term in sensitive_terms:
        if term in clean_output:
            return False

    ssn_pattern = r"\b\d{3}-\d{2}-\d{4}\b"

    if re.search(ssn_pattern, ai_output):
        return False

    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    if re.search(email_pattern, ai_output):
        return False

    return True
