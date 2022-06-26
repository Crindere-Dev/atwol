from pypresence import Presence
import time
import random
import sys
import os

starttime = int(time.time())
client_id = '988073727663149077' # id of your Discord application
large_text = "Atwol" # text of large img of your app
large_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" # large img of your app
small_text = "a timeworn way of life" # text of small img of your app
small_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" # small img of your app
RPC = Presence(client_id)
RPC.connect() # Connect RPC client

while True:
    try:
        file = open("{0}\..\state.txt".format(os.getcwd()), 'r', encoding = "utf-8").read() # get status from file
        
        if "err3" == mb:
            details = "'*.save': Status error"
            state = "Error 3: loaded wrong save-file"
            large_text = "Atwol"
            large_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" 
            small_text = "a timeworn way of life"
            small_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" 
        elif "mm" == mb:
            details = "Main Menu"
            state = None
            large_text = "Atwol"
            large_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" 
            small_text = "a timeworn way of life"
            small_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" 
        elif "sp" == mb:
            details = "Game is loading"
            state = None
            large_text = "Atwol"
            large_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" 
            small_text = "a timeworn way of life"
            small_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" 
        else:
            details = "'state.txt': Status error"
            state = "Error 1: incorrect arg: '{0}'".format(file)
            large_text = "Atwol"
            large_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" 
            small_text = "a timeworn way of life"
            small_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png" 
    except:
        details = "'state.txt': Status error"
        state = "Error 2: file is missing"
        large_text = "Atwol"
        large_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png"" 
        small_text = "a timeworn way of life"
        small_image = "https://cdn.discordapp.com/attachments/987662156889747459/988080272996192307/hh.png"" 
    RPC.update(details=details, state=state, start = starttime, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text) # update status of rpc