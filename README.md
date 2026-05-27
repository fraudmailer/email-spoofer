# Email Spoofer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

<p align="center">
Lightweight SMTP utility written in Python.
</p>

---

## Overview

Email Spoofer is a lightweight Python-based SMTP utility designed for custom email delivery through authenticated SMTP servers.

Built as a single-file script, the project focuses on simplicity, portability, and fast execution without unnecessary dependencies or complex setup.

---

## Features

- Custom sender address support
- SMTP authentication
- TLS encrypted connections
- Plaintext email delivery
- File-based message body support
- Command-line interface
- Lightweight single-file architecture
- Cross-platform compatibility
- Minimal dependencies

---

## Repository Structure

```bash
.
└── spoofer.py
```

---

## Requirements

- Python 3.10+
- Internet connection
- Access to a valid SMTP server

---

# Installation

## Clone Repository

```bash
git clone https://github.com/fraudmailer/email-spoofer.git
cd email-spoofer
```

---

# Usage

## Basic Execution

```bash
python spoofer.py \
  --sender sender@example.com \
  --recipient target@example.com \
  --subject "Test Message" \
  --body "Hello from Email Spoofer" \
  --smtp-server smtp.gmail.com \
  --smtp-port 587 \
  --username your@email.com \
  --password yourpassword
```

---

# Command Line Arguments

| Argument | Description |
|---|---|
| `--sender` | Sender email address |
| `--recipient` | Target recipient email |
| `--subject` | Email subject |
| `--body` | Email body text or file path |
| `--smtp-server` | SMTP server address |
| `--smtp-port` | SMTP server port |
| `--username` | SMTP authentication username |
| `--password` | SMTP authentication password |
| `--file` | Read email body from file |

---

# Example

```bash
python spoofer.py \
  --sender admin@example.com \
  --recipient test@example.com \
  --subject "SMTP Test" \
  --body message.txt \
  --file \
  --username smtp_user \
  --password smtp_password
```

---

# Example Output

```bash
[+] Connecting to SMTP server...
[+] Starting TLS session...
[+] Authenticating...
[+] Sending email...
Email sent successfully to target@example.com
```

---

# Design Philosophy

- Single-file portability
- Minimal setup requirements
- Lightweight execution
- Easy command-line operation
- Fast deployment

---

# Use Cases

- SMTP workflows
- Email delivery operations
- Mail relay interaction
- Header experimentation
- Python SMTP automation
- Command-line mail operations

---

# Disclaimer

Use responsibly.

The author is not responsible for misuse or damage caused by this software.
