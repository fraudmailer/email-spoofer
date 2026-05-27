#!/usr/bin/env python3
# Email Spoofer Script
# For educational purposes only

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse
import random
import time

def send_spoofed_email(sender_email, recipient_email, subject, body, smtp_server, smtp_port, username, password):
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # Login with credentials
        server.login(username, password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print(f"Email sent successfully to {recipient_email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Email Spoofer - Educational Use Only')
    parser.add_argument('--sender', required=True, help='Spoofed sender email address')
    parser.add_argument('--recipient', required=True, help='Target email address')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Email body or path to file')
    parser.add_argument('--smtp-server', default='smtp.gmail.com', help='SMTP server')
    parser.add_argument('--smtp-port', type=int, default=587, help='SMTP port')
    parser.add_argument('--username', required=True, help='SMTP username')
    parser.add_argument('--password', required=True, help='SMTP password')
    parser.add_argument('--file', action='store_true', help='Read body from file')
    
    args = parser.parse_args()
    
    # Read body from file if specified
    if args.file:
        try:
            with open(args.body, 'r') as f:
                email_body = f.read()
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return
    else:
        email_body = args.body
    
    # Send the spoofed email
    send_spoofed_email(
        args.sender, 
        args.recipient, 
        args.subject, 
        email_body,
        args.smtp_server,
        args.smtp_port,
        args.username,
        args.password
    )

if __name__ == "__main__":
    main()