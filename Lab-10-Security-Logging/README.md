## Secure Logging Principle

Security logs should record enough information to investigate an event without unnecessarily storing sensitive user data.

This lab records:
- Timestamp
- Severity level
- Security event type
- Sanitized event description

The application does not write the complete user request to the security log.

This reduces the risk of passwords, personal information, confidential business data, or other sensitive information being duplicated into log files.

## Key Lesson

AI security logging should provide visibility without creating a new source of sensitive data.

Logs are themselves security-sensitive assets and should be protected, monitored, and retained according to organizational policy.