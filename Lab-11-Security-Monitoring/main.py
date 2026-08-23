from security_monitor import monitor_event

events = [
    ("LOGIN_FAILURE", "HIGH"),
    ("PROMPT_INJECTION", "MEDIUM"),
    ("SAFE_REQUEST", "INFO"),
    ("DATA_EXFILTRATION", "HIGH"),
]
event_count = 0
high_alert_count = 0
medium_alert_count = 0
info_event_count = 0
for event_type, severity in events:
    monitor_event(event_type, severity)
    event_count += 1
    if severity == "HIGH":
        high_alert_count += 1
    elif severity == "MEDIUM":
        medium_alert_count += 1
    elif severity == "INFO":
        info_event_count += 1

print(f"\nTotal security events processed: {event_count}")
print(f"High-severity alerts: {high_alert_count}")
print(f"Medium-severity alerts: {medium_alert_count}")
print(f"Info events: {info_event_count}")
alert_rate = ((high_alert_count + medium_alert_count) / event_count) * 100
print(f"Alert rate: {alert_rate}%") 