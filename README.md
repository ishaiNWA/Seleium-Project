# WebLinkChecker

This is a tool for checking registration operations on websites,
matching the format of: \`https://immediatfolex.ai/\`.

## Description

WebLinkChecker automatically validates registration functionality across multiple website instances and reports issues through Telegram notifications.

## Prerequisites

- Python 3.x
- Telegram Bot Account
- Chrome/Firefox Browser (for Selenium)
- NordVPN (or equivalent VPN service)

## Installation

Create virtual environment:

\```bash
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
\```

Install requirements:

\```bash
pip install -r requirements.txt
\```

## Configuration

1. Create a \`.env\` file in the project root directory
2. Add your Telegram credentials:
   \```
   TELEGRAM_BOT_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   \```

3. Configure VPN connection:

- Connect to NordVPN (or your VPN service)
- Select United Kingdom as your connection location
- Ensure VPN connection is stable before running the script

## Usage

Modify the "url_list" variable in the main function to specify target websites (must match format: \`https://immediatfolex.ai/\`)

Run the script:

\```bash
python3 main.py
\```

## Error Logging

The application logs different types of failures to separate log files based on the error type:

- Registration errors
- Page errors
- Internal system errors
  Each error type is documented in its respective log file for easy troubleshooting.
