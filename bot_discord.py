import os

import discord
from dotenv import load_dotenv

from chat import chat

load_dotenv()
private_messages = []
group_messages = []


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        channel = message.channel
        content = message.content
        type_channel = channel.type

        if message.author == self.user:
            return

        await channel.typing()

        if '/gpt ' in content and 'text' in type_channel:
            group_messages.append(
                {"role": "user", "content": content.replace('/gpt ', '')})
            await self.reply(channel, group_messages)

        if 'private' in type_channel:
            private_messages.append(
                {"role": "user", "content": content})
            await self.reply(channel, private_messages)

    async def reply(self, channel, array):
        response = chat(array)
        await channel.send(response.choices[0].message.content)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.environ.get('DISCORD_KEY'))
