import os,sys,time
from multiprocessing import Process,Pipe

from dotenv import load_dotenv, dotenv_values 
load_dotenv()

import discord
from discord import Intents
import asyncio

#i dont know if discord.py will let me run this in function space
def thread(child_conn):

    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        global state
        print("Connected to Discord")
        while True:
            await asyncio.sleep(0.5)
            
            #print("t-eLoop")

    @client.event
    async def on_message(message):
        print(message)

    client.run(os.getenv("DISCORD_KEY"))


##this entire behavior can be replaced with the discord interactions