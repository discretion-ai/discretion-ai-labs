# Lab 13.2 — Installing and Verifying Docker Desktop on macOS

## 1. Lab Overview

In this lesson, we will install, configure, and verify Docker Desktop on an Apple Silicon Mac.

Docker will provide the containerization platform for our Discretion AI development environment. Later lessons will use Docker to deploy Open WebUI, n8n, and other supporting AI services.

**Estimated time:** 30–45 minutes

**Difficulty:** Beginner

**Prerequisites:**
- Apple Silicon Mac (M-series processor)
- macOS with administrator access
- Internet connection
- Terminal access
- Homebrew installed (Lab 13.1)

## 2. Learning Objectives

By completing this lesson, students will be able to:

1. Explain what Docker and containers are.
2. Install Docker Desktop on macOS.
3. Start and configure Docker Desktop.
4. Verify the Docker CLI and Docker Engine.
5. Run a test container.
6. Understand basic Docker security considerations.
7. Troubleshoot common installation problems.

## 3. What Is Docker?

Docker is a platform used to package and run applications inside containers.

A container includes an application and its required dependencies, helping it run consistently across different environments.

Unlike traditional virtual machines, containers generally share the host operating system's kernel. On macOS, Docker Desktop runs Linux containers using a lightweight Linux virtual machine.

### Why Docker Matters for Discretion AI

Docker will help us:

- Deploy applications consistently.
- Reduce software dependency conflicts.
- Separate AI services into individual containers.
- Simplify updates and maintenance.
- Package solutions for future client deployments.

Docker does not automatically make applications secure or completely isolated.

## 4. Download Docker Desktop

1. Open Safari or another web browser.
2. Visit https://www.docker.com/products/docker-desktop/
3. Select the download for **Mac with Apple Silicon**.
4. Wait for the download to complete.
5. Open the downloaded `.dmg` file.
6. Drag Docker into the Applications folder.

**Important:** Download Docker from the official Docker website. Review Docker Desktop licensing requirements before business or commercial deployment.

## 5. Start Docker Desktop

1. Open Finder.
2. Select Applications.
3. Double-click Docker.
4. Approve any macOS security prompts after confirming the application is from Docker.
5. Follow the Docker Desktop setup wizard.
6. Accept the terms if appropriate.
7. Wait for Docker Desktop to finish starting.

Docker Desktop may request permission to install privileged helper components or configure networking.

Grant only the permissions necessary for the selected installation configuration.

## 6. Verify the Docker CLI

Open Terminal or the integrated terminal in Visual Studio Code.

Run:

```bash
docker --version
```

Example output:

```text
Docker version 29.8.0, build 88096ef
```

The version number may differ.

This confirms that the Docker command-line interface is installed and accessible.

**Note:** This command alone does not confirm that the Docker Engine is running.

## 7. Verify the Docker Engine

Run:

```bash
docker info
```

The command should display information about the Docker client and server, including configuration, storage, and runtime information.

If the Docker Engine is unavailable, an error may indicate that it cannot connect to the Docker daemon.

**Troubleshooting:** Start Docker Desktop, wait until the engine is running, and retry.

### Lab Verification Record

- Docker CLI version observed: `29.8.0`
- `docker info` completed successfully: Yes
- Docker Engine accessible: Yes

These results were recorded on the Discretion AI development Mac mini. Other computers may report different versions.

## 8. Run Your First Docker Container

Run:

```bash
docker run --rm hello-world
```

Docker will download the image if it is not already available and start a temporary container.

Expected output includes:

```text
Hello from Docker!
```

The `--rm` option automatically removes the container after it finishes.

This test verifies that Docker can retrieve an image, create a container, and execute it.

If the image cannot be downloaded, check network connectivity and Docker Hub access.

## 9. Inspect Docker Containers

List running containers:

```bash
docker ps
```

List all containers, including stopped containers:

```bash
docker ps -a
```

List downloaded images:

```bash
docker images
```

These commands will be useful when troubleshooting future Discretion AI services.

## 10. Security Considerations

Docker introduces additional configuration and security responsibilities.

Follow these guidelines:

- Download Docker from trusted sources.
- Keep Docker Desktop and container images updated.
- Avoid running containers with unnecessary privileges.
- Do not expose container ports publicly unless required.
- Avoid storing passwords or API keys directly in source code.
- Do not commit secrets to GitHub.
- Use trusted container images and review their configuration.
- Apply resource limits where appropriate.
- Review container networking before deploying client applications.
- Never mount the Docker socket into untrusted containers.

For Discretion AI, protecting local client data and minimizing unnecessary network exposure will be priorities.

## 11. Troubleshooting

### Problem: `docker: command not found`

Possible causes:

- Docker Desktop was not installed correctly.
- The terminal needs to be restarted.
- Docker's CLI directory is not in the shell's PATH.

**Resolution:** Verify Docker Desktop installation and its CLI configuration.

### Problem: Cannot connect to the Docker daemon

Possible causes:

- Docker Desktop is not running.
- Docker Engine has not finished starting.
- The selected Docker context is incorrect.

**Resolution:** Open Docker Desktop, verify the engine is running, and retry `docker info`.

### Problem: Container image download fails

Possible causes:

- Internet connection unavailable.
- Docker Hub temporarily unavailable.
- Proxy or firewall restrictions.

**Resolution:** Verify connectivity and Docker's proxy settings.

## 12. Knowledge Check

1. What is Docker?
2. What is the difference between a container and a virtual machine?
3. Why does Docker Desktop use a Linux virtual machine on macOS?
4. What does `docker --version` verify?
5. Why is `docker info` useful?
6. What does the `--rm` option do?
7. Why should Docker containers avoid unnecessary privileges?

## 13. Lesson Completion Checklist

- [x] Docker Desktop installation confirmed.
- [x] Docker CLI version verified.
- [x] Docker Engine verified using `docker info`.
- [x] Run the `hello-world` test container.
- [x] Inspect containers and images.
- [x] Document testing results.
- [ ] Commit and push the completed lesson to GitHub.

**Next lesson:** Lab 13.3 — Ollama Installation and Verification.