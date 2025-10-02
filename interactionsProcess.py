import os,sys,time
from multiprocessing import Process,Pipe

from dotenv import load_dotenv, dotenv_values 
load_dotenv()

import structs

import discord
from discord import Intents
import asyncio

<<<<<<< HEAD
async def send_as_segments(channel, message):
    segments = [message[i:i+2000] for i in range(0, len(message), 2000)]
    
    i=0
    for segment in segments:
        #hyphenate broken text
        if i != len(segments)-1: segment = segment+"-"

        #send message segment
        await channel.send(segment)

        #sleep (can be ignored if last iteration)
        await asyncio.sleep(0.2)
        i+=1

    return
=======
##local state class
class State:
    def __init__(self):
        #
        self.tickets=[]

        return
    
    def pushTicket(self, ticket):

        ##validate ticket

        #push ticket to array
        self.tickets.append(ticket)

    def getTicket(self, ticketID):
        for ticket in self.tickets:
            if ticket.id == ticketID:
                return ticket
            
        return None
    
    def closeTicket(self, ticketID):
        for ticket in self.tickets:
            if ticket.id == ticketID:
                self.tickets.remove(ticket)
        return

state = State()
>>>>>>> 6d9a5f6873b3802ae575408cb206857d8eca20db

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
            
            #check outgoing message queue
            if child_conn.poll():

                data = child_conn.recv()
                
                if (not data):
                    print("An unknown error has occured, nonetype?")
                    continue

<<<<<<< HEAD
                #send message segment
                channel = client.get_channel(int(data.channel)) #TODO hyphenate broken text and come up with solution for large tables
                await send_as_segments(channel, data.content)
=======
                #find ticket (checkout)
                ticket = state.getTicket(data.id)
                if not ticket:
                    print("TICKET NOT FOUND, timeout?")

                #TODO break up large messages
                channel = client.get_channel(int(data.channel))
                await channel.send(data.content)
>>>>>>> 6d9a5f6873b3802ae575408cb206857d8eca20db

                ##close ticket
                state.closeTicket(data.id)

                #debug
                print(len(state.tickets))

            #check tickets for typing indicator
            for ticket in state.tickets:
                channel = client.get_channel(int(ticket.channel))
                await channel.typing()
                #print(f"typing in {ticket.channel}")

            await asyncio.sleep(0.3)

    #on message handler
    @client.event
    async def on_message(message):
        #print(message, "\n", dir(message))

        if message.author.id == 1152264823271329822:
            return
        
        #open ticket (checkIn)
        ticket = structs.Ticket(
            id=message.id,
            author=message.author.id,
            channel=message.channel.id,
            guild=message.guild.id if message.guild is not None else None, #messy turnary
            dob=time.time() #float
        )
        state.pushTicket(ticket)

        ##pack struct
        mStruct = structs.inMessage(
            id=message.id,
            author=message.author.id,
            author_name=message.author.display_name,
            channel=message.channel.id,
            channel_name="message.channel.auto", #TODO BRO TF IS THIS LMFAOOOOO, this can be a turnary operator like guild
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