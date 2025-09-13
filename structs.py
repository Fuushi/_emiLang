import time

##This file contains commonly used structs for passing data between process(s)

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

        return