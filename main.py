import os, sys, time

#multiprocesing
from multiprocessing import Process,Queue,Pipe

##include interactions process
from interactionsProcess import thread as dp
from interactionsProcess import thread as ip


def main():

    ##create pipe and start child process
    parent_conn,child_conn = Pipe()
    p = Process(target=dp, args=(child_conn,))
    p.start()

    while True:

        print("t-main")

        if parent_conn.poll():
            data = parent_conn.recv()

            print(data)

        time.sleep(1)

    return



if __name__ == "__main__":
    main()