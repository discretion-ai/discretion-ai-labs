# Lab 13.3 — Installing and Verifying Ollama on macOS

## 1. Lab Overview

**Project:** Discretion AI Labs  
**Environment:** Apple Silicon Mac mini  
**Difficulty:** Beginner  
**Prerequisites:** Basic Terminal knowledge and access to macOS  
**Estimated time:** 20–30 minutes, excluding downloads

### Objective

Install and verify Ollama, a local AI model runtime that allows users to download, manage, and execute large language models (LLMs) on their own computers.

This lab establishes the foundation for running local AI models without relying on cloud-based inference services.

By the end of this lab, students will be able to:

- Explain what Ollama does.
- Install Ollama on an Apple Silicon Mac.
- Verify the Ollama command-line interface (CLI).
- Confirm the Ollama server is responding.
- List locally installed AI models.
- Identify basic Ollama security considerations.
- Troubleshoot common installation issues.

---

## 2. What Is Ollama?

Ollama is software for running and managing AI models locally.

It provides:

- A command-line interface.
- A local API for applications.
- Model downloading and management.
- Support for multiple compatible AI models.
- Integration with tools such as Open WebUI and automation platforms.

Ollama is not itself an AI model.

For example:

- **Ollama:** The software that runs models.
- **IBM Granite:** An AI model that can run through Ollama.
- **Open WebUI:** A browser-based interface for interacting with compatible model runtimes.

### Why Ollama Matters to Discretion AI

Discretion AI focuses on building private AI environments where sensitive client information can remain under local control.

Ollama provides the model runtime for that architecture.

Running inference locally does not automatically guarantee complete privacy. Network access, application integrations, model downloads, logging, and security settings must also be considered.

---

## 3. Prerequisites

Before beginning, confirm:

- You have an Apple Silicon Mac.
- You can access the Terminal application.
- You have sufficient available storage.
- You have internet access for downloading the Ollama installer.
- You can install applications on the Mac.

Homebrew is useful but is not required for the official macOS Ollama application installation.

Docker is also not required to run Ollama natively on macOS.

---

## 4. Download Ollama

### Step 1 — Open the Official Website

Open Safari and navigate to:

https://ollama.com/download

### Step 2 — Select macOS

Download the macOS version of Ollama.

Avoid downloading installers from untrusted third-party websites.

### Step 3 — Install Ollama

Open the downloaded archive or installer.

Follow the installation instructions to place Ollama in the Applications folder and complete any requested setup.

### Step 4 — Launch Ollama

Open Ollama from the Applications folder.

Complete any initial setup prompts.

Ollama may operate in the background and provide a menu bar icon.

**Expected result:** Ollama is installed and its local service can be started.

---

## 5. Verify the Ollama CLI

Open Terminal or the integrated terminal in Visual Studio Code.

Enter:

```bash
ollama --version
```

### Explanation

This command displays the installed Ollama version.

It helps confirm that the command-line application is available.

### Expected Result

A version number should appear.

Example from the Discretion AI development environment:

```text
ollama version is 0.34.4
```

The version may differ depending on when the lab is completed.

### Troubleshooting

If the terminal reports:

```text
command not found: ollama
```

Confirm Ollama is installed, launch the application, and restart the terminal.

If the command remains unavailable, review the official macOS installation documentation.

---

## 6. Verify the Ollama Server

Ollama exposes a local HTTP API, normally using port 11434.

Enter:

```bash
curl http://127.0.0.1:11434/api/version
```

### Explanation

- `curl` sends an HTTP request.
- `127.0.0.1` refers to the local computer.
- `11434` is Ollama's default API port.
- `/api/version` requests the running server version.

### Expected Result

A JSON response similar to:

```json
{"version":"0.34.4"}
```

Your installed version may be different.

### Troubleshooting

If the request cannot connect, confirm that the Ollama application or server is running.

For native macOS installations, launch the Ollama application.

Alternatively, `ollama serve` can start the server manually when no other Ollama server is already running.

Do not start a second server if one is already listening on the same port.

---

## 7. List Installed Models

Enter:

```bash
ollama list
```

### Explanation

This command displays models already downloaded to the local Ollama environment.

It includes information such as:

- Model name
- Model identifier
- Storage size
- Modification date

### Expected Result for a New Installation

```text
NAME    ID    SIZE    MODIFIED
```

An empty list is normal when no models have been downloaded.

**Important:** Installing Ollama does not automatically mean an AI model has been installed.

The next lab will introduce IBM Granite.

---

## 8. Check Running Models

Enter:

```bash
ollama ps
```

### Explanation

This command displays AI models currently loaded into memory by Ollama.

It can help identify resource usage and whether a model is running.

### Expected Result

If no models are running, the command displays column headings without any model entries.

This is normal before installing the first model.

---

## 9. Understanding the Local AI Architecture

The initial Discretion AI development environment consists of several components.

| Component | Purpose |
|---|---|
| macOS | Host operating system |
| Homebrew | Package management |
| Git and GitHub | Version control and documentation |
| Docker Desktop | Container runtime and management |
| Ollama | Local AI model runtime |
| IBM Granite | Planned first AI model |
| Open WebUI | Planned browser-based AI interface |
| n8n | Planned workflow automation |

Ollama runs natively on the Mac in this initial configuration.

Docker Desktop will be used for other components as the project progresses.

### Why Use Native Ollama?

Native Ollama can take advantage of Apple Silicon acceleration without requiring the model runtime to run inside a Linux container.

This is a practical starting point for developing and testing local AI applications on a Mac mini.

---

## 10. Security Considerations

Local AI systems still require security controls.

### Protect the Local API

Ollama normally listens on the loopback interface.

Avoid exposing the Ollama API to external networks unless there is a documented business requirement and appropriate security controls.

### Restrict Unnecessary Access

Do not expose Ollama directly to the public internet.

Use appropriate authentication, network controls, and access restrictions when integrating it with other services.

### Verify Model Sources

Download models from trusted sources and review their licensing, origin, and suitability before using them with client data.

### Protect Sensitive Information

Do not commit the following to public GitHub repositories:

- Client documents
- Passwords
- API keys
- Access tokens
- Sensitive prompts or outputs
- Confidential configuration files

### Monitor Resource Consumption

Large AI models can consume significant memory and disk space.

Select models appropriate for the available hardware.

### Apply Security Frameworks

Relevant security practices include:

- Least privilege
- Secure configuration
- Dependency and supply-chain review
- Logging and monitoring
- OWASP guidance for LLM applications
- Data privacy and retention controls

---

## 11. Troubleshooting

### Problem: Ollama Command Not Found

**Possible cause:** The application is not installed correctly or the CLI is not available in the terminal environment.

**Resolution:** Confirm installation, launch Ollama, restart Terminal, and review the official documentation.

### Problem: Cannot Connect to Ollama Server

**Possible cause:** The local Ollama service is not running.

**Resolution:** Launch Ollama and repeat the API verification test.

### Problem: Port 11434 Is Already in Use

**Possible cause:** Another Ollama server or application is already listening on the port.

**Resolution:** Check whether Ollama is already running before attempting to start another instance.

### Problem: No Models Listed

**Possible cause:** No AI models have been downloaded.

**Resolution:** This is expected during Lab 13.3. Model installation will occur in the next lab.

### Problem: Model Runs Slowly

**Possible cause:** The model may exceed practical memory or processing limits.

**Resolution:** Consider smaller models, appropriate quantization, and reducing unnecessary background workloads.

---

## 12. Verification Results

### Discretion AI Development Environment

**Hardware:** Mac mini with Apple Silicon and 24 GB unified memory

**Ollama version:** 0.40.6

**Installation status:** Confirmed

**CLI verification:** Passed

**Model listing:** Passed — no models installed

**API version test:** Passed — server returned 0.40.6

**Running model check:** Passed - no models

### Commands Used

```bash
ollama --version
ollama list
curl http://127.0.0.1:11434/api/version
ollama ps
```

Record the actual results of each command before marking the lab complete.

---

## 13. Knowledge Check

1. What is the difference between Ollama and an AI model?
2. Why is Ollama useful for private AI deployments?
3. Which command displays the installed Ollama version?
4. What is the purpose of `ollama list`?
5. What does `ollama ps` display?
6. What is the default Ollama API port?
7. Why should Ollama's API not be exposed directly to the public internet?
8. Why does an empty model list not indicate an installation failure?
9. What advantages can native Ollama offer on Apple Silicon?
10. Why should model provenance and licensing be reviewed before client deployment?

---

## 14. Lesson Completion Checklist

- [x] Ollama installation confirmed.
- [x] Ollama CLI version verified.
- [x] List installed models using `ollama list`.
- [x] Verify the local API using `curl`.
- [x] Inspect running models using `ollama ps`.
- [x] Record verification results.
- [x] Review security considerations.
- [x] Commit and push the completed lesson to GitHub.

---

**Next Lesson:** Lab 13.4 — Downloading, Running, and Testing IBM Granite Locally.