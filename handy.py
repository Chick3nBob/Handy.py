import discord
    import asyncio

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        if message.content == "Hello":
            await client.send_message(message.channel, "World")

    client.run("NDE3MDUzNzUxMzgwMTQ4MjI0.DXNbGQ.uGVFog4RdXTcGAywz0t5pc2FDPM")
