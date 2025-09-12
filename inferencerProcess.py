import os, sys, time
from multiprocessing import Process,Pipe

from dotenv import load_dotenv, dotenv_values
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"), override=True)

#inference related includes
from openai import OpenAI

##initialize objects
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


##helper funcions
def inference():
    ##example request
    
    print("----- standard request -----")
    completion = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            },
        ],
    )
    print(completion.choices[0].message.content)

    return


def thread(child_conn):
    ## thread event loop, calls inference
    print("Connected to OpenAI")

    #
    while True:
        
        #check pipe
        if child_conn.poll():
            data = child_conn.recv()

            #data is to be stored in a struct
            print(data)

        time.sleep(0.5)
        #print("i-loop")
    
    return ##do not return

##implement openai backend first, then local api