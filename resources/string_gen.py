from telethon.sessions import StringSession
from telethon.sync import TelegramClient

ok = """ ______  _              __   __
|  ____|(_)             \ \ / /
| |__    _  _ __   ___   \ V / 
|  __|  | || '__| / _ \   > <  
| |     | || |   |  __/  / . \ 
|_|     |_||_|    \___| /_/ \_\
                               
"""
print(ok)
APP_ID = int(input("Enter APP ID here: \n"))
API_HASH = input("Enter API HASH here: \n")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    try:
        session = client.session.save()
        client.send_message("me", f"String Session \nTap To Copy. Do join @Fire_X_Userbot \n`{session}`")
        print("String Generated Sucessfully Check Your Saved Message.")
    except Exception as sed:
        print(f"Something Went Wrong While Generating String \nError : {sed}")
