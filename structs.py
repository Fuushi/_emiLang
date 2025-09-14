import time

##This file contains commonly used structs for passing data between process(s)

#the primary struct for interactions messages contains all scoping info
class inMessage:
    def __init__(self,
        id : int,
        author : str,
        author_name : int,
        channel : int,
        channel_name : str,
        guild : int,
        guild_name : str,
        content : str,
        dob : float = time.time(),
        preload_history : list = []
        ):
        
        self.id = id
        self.author = author
        self.author_name = author_name
        self.channel = channel
        self.channel_name = channel_name
        self.guild = guild
        self.guild_name = guild_name
        self.content = content
        self.dob = dob
        self.preload_history = preload_history

        return
    
class outMessage:
    def __init__(self,
        id : int,
        channel : int,
        guild : int,
        content : str,
        media : list = [] #file path(s)
        ):

        self.id = id
        self.channel = channel
        self.guild = guild
        self.content = content
        self.media = media

        return
    
class Context:
    #CONTEXT IS CHANNEL SPECIFIC
    def __init__(self,
        array : list,
        system : dict = None
        ):
        ##stores an array of dictionaries sorted oldest to newest
        self.raw_ctx=array[::-1]
        self.system=system

        return

    def get_ctx(self, limit : int = 100):
        ##only returns the author and content elements,
        ##even though class supports arbitrary additonal elements

        i=0
        ret = []
        for element in self.raw_ctx[::-1]:
            #runs new to old

            ret.append(
                {
                    "role": "assistant" if element['author'] == 'Emi AI#8362' else "user",
                    "content": element['content']
                }
            )

            if i >= limit:
                if self.system: ret.append(self.system)
                return ret[::-1]
            
            i+=1

        if self.system: ret.append(self.system)
        return ret[::-1]
        