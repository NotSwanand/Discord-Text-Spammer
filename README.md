# Discord Multi-Bot Spammer

This project demonstrates a simple implementation of multiple Discord bots working in parallel to perform automated tasks in a Discord server.

> **Disclaimer:** This script should only be used for educational purposes and must comply with Discord's [Terms of Service](https://discord.com/terms). Spamming, automating without permission, or disrupting servers can result in account suspension or legal actions.

---

## Features

- **Bot 1, Bot 2, and Bot 3**:
  - Sends a random word from a predefined list (`arr`) to a specified channel every 3 seconds.
- **Main Client**:
  - Listens for a specific embed footer message and automatically claims a number using the `.claim` command.

---

## Prerequisites

- Python 3.8 or higher
- The `discord.py` library (Install with `pip install discord.py`)

---

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/discord-multi-bot-spammer.git
   cd discord-multi-bot-spammer
2. Install dependencies:
```
pip install discord.py
```
3. Update the script:

Replace add spammer token here with the bot tokens for your three bots.
Replace add server id here with the Discord server ID you want the main client to operate in.
Replace add channel id here with the channel IDs where the bots will post messages.
4. Run the script:
```
python your-script-name.py
```
