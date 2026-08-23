from datetime import datetime

def log_security_event(event_type, message, severity="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"{timestamp} | {severity} | {event_type} | {message}"

    with open("security.log", "a") as log_file:
        log_file.write(log_entry + "\n")