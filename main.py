import os, sys, time

#multiprocesing
from multiprocessing import Process,Queue,Pipe

##include process(s)
from interactionsProcess import thread as dp
from inferencerProcess import thread as ip
from chatMonolith import thread as mp


def main():

    ##create pipe and start child process(s)
        #interactions
    interactions_sub_conn,interactions_monolith_conn = Pipe()
    interactions_p = Process(target=dp, args=(interactions_sub_conn,), name="dp", daemon=True)
    interactions_p.start()

        #inferencer
    inference_sub_conn,inference_monolith_conn = Pipe()
    inference_p = Process(target=ip, args=(inference_sub_conn,), name="ip", daemon=True)
    inference_p.start()

        #chat monolith
    monolith_p = Process(target=mp, args=(interactions_monolith_conn,inference_monolith_conn,), name="mp", daemon=True)
    monolith_p.start()


    while True:
        #threads can be managed here if needed (main has to be alive to kill daemons)
        #print("t-main")
        time.sleep(0.2)

    return



if __name__ == "__main__":
    main()