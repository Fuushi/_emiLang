TIMEOUT=60


import os, sys, time

#multiprocessing
from multiprocessing import Process,Pipe

from dotenv import load_dotenv, dotenv_values
load_dotenv()

import structs

##main thread loop
def thread(interactions_conn, inference_conn): ##should have 2 pipes, one for inference one for interactions

    while True:

        ##poll interactions for new messages
        if interactions_conn.poll():

            data = interactions_conn.recv()

            print(data)

            ##load relavent context, scope, curriculum
                #TODO

            ##build context
            ##implicit constructor when creating context struct?
            ctx=structs.Context(data.preload_history)

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
            modelMessage = structs.outMessage(
                id=None,
                channel=data.channel,
                guild=data.guild,
                content = inferenceResp['content'],
                media=[]
            )

            ##(possible executive function clause here)

            #pipe back to interactions
            interactions_conn.send(modelMessage)

            ##finish up

        time.sleep(1)

        ##if no messages were sent, possible executive function or sleep review



    return #exit clause