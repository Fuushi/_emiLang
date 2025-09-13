import os, sys, time
from multiprocessing import Process,Pipe

from dotenv import load_dotenv, dotenv_values
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"), override=True)

#inference related includes
from openai import OpenAI

import structs

##initialize objects
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


##helper funcions
def inference(ctx):
    ##example request
    
    print("----- standard request -----")
    completion = client.chat.completions.create(
        model="gpt-5-nano",
        messages=ctx,
    )
    print(completion.choices[0].message.content)

    return {
        "author" : "Assistant",
        "content" : completion.choices[0].message.content
    }


def thread(child_conn):
    ## thread event loop, calls inference
    print("Connected to OpenAI")

    #
    while True:
        
        #check pipe
        if child_conn.poll():
            data = child_conn.recv()

            #data is to be stored in a struct
            print(f"DATA RECIEVED AT INFERENCER {data}")

            #run inference
            model_response_packet = inference(data.get_ctx())
            
            #pipe data back
            child_conn.send(model_response_packet)
            

        time.sleep(0.5)
        #print("i-loop")
    
    return ##do not return

##implement openai backend first, then local api