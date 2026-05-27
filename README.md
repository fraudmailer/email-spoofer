# Email Spoofer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

<p align="center">
Lightweight SMTP email testing utility written in Python.
</p>

---

## Overview

Email Spoofer is a lightweight Python script designed for SMTP testing, email header experimentation, and mail delivery research in controlled or authorized environments.

The project uses Python's built-in SMTP libraries to create and send custom email messages through authenticated SMTP servers.

Built as a single-file utility, the project focuses on simplicity, portability, and fast deployment.

---

## Features

* Custom sender address support
* SMTP authentication
* TLS encrypted connections
* Plaintext email delivery
* File-based message body support
* Command-line interface
* Lightweight single-file architecture
* Cross-platform compatibility
* Minimal dependencies

---

## Repository Structure

```bash
.
└── spoofer.py
```

---

## Requirements

* Python 3.10+
* Internet connection
* Access to a valid SMTP server

---

# Installation

## Clone Repository

```bash
[git clone https://github.com/yourname/email-spoofer.git](https://github.com/fraudmailer/email-spoofer)
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

| Argument        | Description                  |
| --------------- | ---------------------------- |
| `--sender`      | Sender email address         |
| `--recipient`   | Target recipient email       |
| `--subject`     | Email subject                |
| `--body`        | Email body text or file path |
| `--smtp-server` | SMTP server address          |
| `--smtp-port`   | SMTP server port             |
| `--username`    | SMTP authentication username |
| `--password`    | SMTP authentication password |
| `--file`        | Read email body from file    |

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

* Single-file portability
* Minimal setup requirements
* Lightweight execution
* Easy command-line operation
* Simple SMTP workflow testing

---

# Use Cases

* SMTP server testing
* Email delivery debugging
* Mail relay validation
* Security research labs
* Internal awareness simulations
* Email header experimentation

---

# Security Notice

This project is intended strictly for:

* Authorized security testing
* Educational research
* Internal lab environments
* Defensive security analysis

Unauthorized usage against third-party systems, phishing campaigns, credential theft, fraud, or malicious activity is strictly prohibited.

Users are responsible for complying with all applicable laws and regulations.

---

# Disclaimer

The developers assume no responsibility for misuse or damage caused by this software.

Use this project only in environments you own or are explicitly authorized to test.

