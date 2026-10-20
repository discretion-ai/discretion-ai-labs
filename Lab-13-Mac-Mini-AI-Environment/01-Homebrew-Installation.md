# Lab 13.1 — Installing and Verifying Homebrew on macOS

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain what Homebrew is and why developers use it.
- Install Homebrew on an Apple Silicon Mac.
- Configure the Terminal to recognize Homebrew.
- Verify that Homebrew is installed and working.
- Perform basic installation troubleshooting.

## 1. What Is Homebrew?

Homebrew is a package manager for macOS. It allows developers to install and manage software using Terminal commands.

Instead of manually downloading every application, Homebrew can install supported software packages and their dependencies.

**Why Discretion AI uses Homebrew:**

Homebrew helps establish a consistent development environment for installing and maintaining command-line tools used in local AI development.

Official website: https://brew.sh/

## 2. Prerequisites

Before starting, you should have:

- An Apple Silicon Mac (M-series processor).
- A supported version of macOS.
- An internet connection.
- Administrator access to your Mac.
- Access to the macOS Terminal.

**Note:** The Discretion AI development machine is a Mac mini M4 with 24 GB of unified memory.

## 3. Open Terminal

There are two ways to access Terminal.

**Option A — macOS Terminal**

1. Press Command + Space.
2. Type `Terminal`.
3. Press Enter.

**Option B — VS Code Integrated Terminal**

1. Open Visual Studio Code.
2. Select Terminal from the top menu.
3. Click New Terminal.

The Terminal window should display a command prompt.

## 4. Check Whether Homebrew Is Already Installed

Run:

```bash
brew --version
```

If Homebrew is installed, its version will appear.

If you receive `command not found: brew`, Homebrew may be missing or not configured in your shell.

## 5. Install Homebrew

Visit https://brew.sh/ to confirm the official installation command.

At the time this guide was written, the command was:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Paste the command into Terminal and press Enter.

**Security note:** This command downloads and executes an installation script. Review the official Homebrew website and installation instructions before running it. Only use the official source.

During installation:

1. macOS may request your administrator password.
2. Type your password and press Enter. Password characters may not appear while typing.
3. Review the installation information.
4. Follow the prompts to continue.
5. Wait for installation to finish.

Homebrew may also install Apple's Command Line Tools if needed.

## 6. Configure Homebrew on Apple Silicon

On Apple Silicon Macs, Homebrew normally installs under:

```text
/opt/homebrew
```

If the installer provides instructions to add Homebrew to your shell environment, follow them.

For the default zsh shell, the commands are typically:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

These commands help your Terminal locate Homebrew.

Do not repeatedly append the same configuration line if Homebrew is already configured.

## 7. Verify the Installation

Run:

```bash
brew --version
```

Expected result:

```text
Homebrew <version-number>
```

Then run:

```bash
brew doctor
```

This checks for potential configuration problems.

An ideal result is:

```text
Your system is ready to brew.
```

Warnings do not always mean Homebrew is unusable. Review them individually before making changes.

## 8. Basic Homebrew Commands

| Command | Purpose |
|---|---|
| `brew --version` | Display installed version |
| `brew doctor` | Check configuration |
| `brew update` | Update package information |
| `brew list` | List installed packages |
| `brew info <package>` | Show package details |
| `brew install <package>` | Install a package |

## 9. Troubleshooting

### Problem: `brew: command not found`

Possible causes:

- Homebrew is not installed.
- Homebrew is installed but missing from your shell PATH.

Check whether the executable exists:

```bash
ls /opt/homebrew/bin/brew
```

If it exists, review the shell configuration instructions in Section 6.

### Problem: Administrator password is not visible

This is normal behavior in macOS Terminal.

Type the password carefully and press Enter.

### Problem: Installation fails

Verify your internet connection, review the Terminal error message, and consult the official Homebrew documentation before retrying.

## 10. Discretion AI Lab Verification

**Development machine:** Mac mini M4, 24 GB unified memory

**Verified command:**

```bash
brew --version
```

**Observed result:**

```text
Homebrew 7.0.9
```

**Status:** Installation and command-line availability verified.

**Additional diagnostic test:**

Command executed:
`brew doctor`

Observed result:
`Your system is ready to brew.`

**Result: PASS**

Homebrew installation, shell configuration,
and diagnostic verification completed successfully.

## 11. Security Considerations

- Install software from trusted sources.
- Review scripts before executing them.
- Avoid unnecessary administrator privileges.
- Keep installed tools updated.
- Never commit passwords, access tokens, or sensitive configuration data to GitHub.

## 12. Knowledge Check

1. What is Homebrew?
2. Why is Homebrew useful for a local AI development environment?
3. Where does Homebrew normally install on Apple Silicon Macs?
4. What command displays the installed Homebrew version?
5. What does `brew doctor` check?

## Lesson Completion Checklist

- [x] Homebrew installation confirmed.
- [x] Homebrew version verified.
- [x] Run `brew doctor` and document the results.
- [x] Review and resolve relevant warnings.
- [ ] Commit and push the completed lesson to GitHub.

**Next lesson:** Lab 13.2 — Git and GitHub Setup.