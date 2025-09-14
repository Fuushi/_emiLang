TIMEOUT=60


import os, sys, time, json

#multiprocessing
from multiprocessing import Process,Pipe

from dotenv import load_dotenv, dotenv_values
load_dotenv()

import structs

#load persona
with open("./personas/persona.json", "r") as fp: persona = json.loads(fp.read())

##main thread loop
def thread(interactions_conn, inference_conn): ##should have 2 pipes, one for inference one for interactions

    while True:

        ##poll interactions for new messages
        if interactions_conn.poll():

            userMessage = interactions_conn.recv()

            print(userMessage)

            ##load relavent context, scope, curriculum
                #TODO

            ##build context object (needs to be processed to get rich context before inference)
            ctx=structs.Context(userMessage.preload_history, system=persona['persona']['systemPrompt'])

            ##pipe to and from interencer
                #pipe to
            inference_conn.send(ctx)

                #pipe back (with timeout n)
            
            sTime=time.time()
            inferenceResp = None
            while (time.time() - sTime) < TIMEOUT:

                if inference_conn.poll():
                    sTime = sTime - TIMEOUT+10 #worlds worst break 
                    inferenceResp = inference_conn.recv()

            if inferenceResp == None:
                ##TIMEOUT
                print("Inference Timeout")
                continue

            print(inferenceResp)

            #pack outMessage
            modelMessage = structs.inMessage(
                id=int(time.time()),
                author=1152264823271329822,
                author_name='Emi AI#8362',
                channel=userMessage.channel,
                channel_name=userMessage.channel_name,
                guild=userMessage.guild,
                guild_name=userMessage.guild_name,
                content=inferenceResp['content'],
                dob=time.time(),
                preload_history=[]
            )

            ##(possible executive function clause here)

            #pipe back to interactions
            interactions_conn.send(modelMessage)

            ##finish up

        time.sleep(0.3)

        ##if no messages were sent, possible executive function or sleep review



    return #exit clause