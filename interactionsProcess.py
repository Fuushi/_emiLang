import os,sys,time
from multiprocessing import Process,Pipe

from dotenv import load_dotenv, dotenv_values 
load_dotenv()

import structs

import discord
from discord import Intents
import asyncio

async def get_history(channel) -> list:
    #returns array of dict
    history = []
    async for msg in channel.history(limit=10):
        history.append({
            "author": str(msg.author),
            "content": msg.content,
            "created_at": msg.created_at.timestamp()
        })
    return history

#i dont know if discord.py will let me run this in function space
def thread(child_conn):

    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    #task loop
    @client.event
    async def on_ready():
        global state
        print("Connected to Discord")
        while True:

            if child_conn.poll():

                data = child_conn.recv()
                
                if (not data):
                    print("An unknown error has occured, nonetype?")
                    continue

                #TODO break up large messages
                channel = client.get_channel(int(data.channel))
                await channel.send(data.content)

            await asyncio.sleep(0.3)

    #on message handler
    @client.event
    async def on_message(message):
        #print(message, "\n", dir(message))

        if message.author.id == 1152264823271329822:
            return

        ##pack struct
        mStruct = structs.inMessage(
            id=message.id,
            author=message.author.id,
            author_name=message.author.display_name,
            channel=message.channel.id,
            channel_name="message.channel.auto",
            guild=message.guild.id if message.guild is not None else None, #messy
            guild_name=message.guild.name if message.guild is not None else None,
            content=message.content,
            dob=time.time(),
            preload_history = await get_history(message.channel) #really messy
        )

        print(mStruct)

        #send struct to monolith and return
        child_conn.send(
            mStruct
        )
    
        return


        
    client.run(os.getenv("DISCORD_KEY"))


##this entire behavior can be replaced with the discord interactions