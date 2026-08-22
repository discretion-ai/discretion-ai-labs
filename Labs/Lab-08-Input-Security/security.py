def check_prompt(user_input):
    MAX_PROMPT_LENGTH = 500

    if len(user_input) > MAX_PROMPT_LENGTH:
        return False

        suspicious_phrases = [
        "ignore previous instructions",
        "reveal system prompt",
        "bypass security",
        "forget everything",
        "previous directions",
        "hidden instructions",
        "disregard previous",
        "override instructions"
    ]

    clean_input = user_input.lower()

    for phrase in suspicious_phrases:
        if phrase in clean_input:
            return False

    return True