# Discord Bot for Command Execution (Windows Only)

A Python-based Discord bot is designed to wait for commands on a Discord server and execute them on the machine where the bot is running. It only works on Windows operating systems.

## Features

- **Startup Notification:** Sends a message to a specified Discord channel upon startup, indicating the user logged into Windows.
- **Command Execution:** Executes system commands received via Discord messages and returns the output directly to the channel.
- **Message Handling:** Responds to specific text commands (e.g., `!cmd <command>`) and replies with command results or error messages.

## Requirements

- Python 3.x
- `discord.py` library
- Windows operating system

## Configuration

1. **Token:** Replace the `token` variable in the script with your own Discord bot token.
2. **Channel ID:** Update the `channel_id` variable with the ID of the Discord channel where the startup message will be sent.
3. **Command Output Handling:** The bot handles command outputs. If the result exceeds 2000 characters, it saves the output to a file and sends it as an attachment.

## Disclaimer
I am not responsible for any misuse of this bot. The user assumes all responsibility for ensuring that the bot is used in a lawful and appropriate manner.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
