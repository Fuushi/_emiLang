import os, sys, time
from multiprocessing import Process,Pipe

from dotenv import load_dotenv, dotenv_values
load_dotenv()

#inference related includes
from openai import OpenAI

##initialize objects
client = OpenAI()# TODO key=dotenv()


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
    
    return ##do not return


##debug main
inference()


##implement openai backend first