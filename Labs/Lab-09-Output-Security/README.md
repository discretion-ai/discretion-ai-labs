# Lab 09 - AI Output Security

## Objective

Demonstrate how an application can inspect AI-generated output before allowing that output to reach the user.

The goal is to prevent sensitive information, personally identifiable information (PII), or excessive output from being exposed.

## Security Controls Implemented

This lab implements several output security controls:

- Maximum output length validation
- Sensitive keyword detection
- Social Security Number (SSN) detection
- Email address detection

## Test Results

### Normal Output

Input:

The customer appointment is scheduled for Monday.

Result:

SAFE: Output approved.

### Sensitive Information

Input:

The customer's password is Blue123.

Result:

BLOCKED: Output failed security validation.

### SSN Detection

Input:

The customer's SSN is 123-45-6789.

Result:

BLOCKED: Output failed security validation.

### Email Detection

Input:

The customer's email is john.smith@example.com

Result:

BLOCKED: Output failed security validation.

## Security Architecture

AI Model
   ↓
Output Security Validation
   ↓
Approved Output
   ↓
User

Potentially sensitive output is blocked before it reaches the user.

## Key Lesson

AI applications should not automatically trust model output.

Security controls should exist between the AI model and the user to validate output and reduce the risk of exposing sensitive information.