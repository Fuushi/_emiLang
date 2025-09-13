import os, sys, time

#multiprocessing
from multiprocessing import Process,Pipe

from dotenv import load_dotenv, dotenv_values
load_dotenv()

##main thread loop
def thread(interactions_conn, inference_conn): ##should have 2 pipes, one for inference one for interactions

    while True:

        ##poll interactions for new messages
        if interactions_conn.poll():

            data = interactions_conn.recv()

            print(data)

        ##load relavent context, scope, curriculum

        ##build context

        ##pipe to and from interencer

        ##(possible executive function clause here)

        #pipe back to interactions

        time.sleep(1)

        ##if no messages were sent, possible executive function or sleep review



    return #exit clause