from cmath import inf
import json
import websocket
import rel

import src.scrape as scrape

def _on_error(ws, error):
    print(error)

def _on_open(ws: websocket):
    
    with open("./config.json", "r") as configFile:
        data = json.load(configFile)
        twitchConfig = data['twitch']

    ws.send('PASS oauth:' + twitchConfig['secret'])
    ws.send('NICK ' + twitchConfig['user'])

    ws.send('JOIN #' + twitchConfig['channels'])

    ws.send('CAP REQ :twitch.tv/tags twitch.tv/commands')
    ws.send('PRIVMSG #sernone :Johnny 5 is Alive!')

    print('Connection Established')


def _on_message(ws: websocket, message: str):

    print('Message: ' + message)

    #Keep alive
    if message.startswith('PING'):
        reply = message.rsplit(" ")
        print('Sending PONG ' + reply[1])
        ws.send('PONG ' + reply[1])

    # TODO: Still workshoping fun things to do but this show cases the code on how to extract all the proper
    #from the message and process it a certian way.
    if message.startswith('@') and message.__contains__('PRIVMSG'):
        info = message.rsplit(':')
        usrInfo = info[0].rsplit(';')

        #Store some needed info for later
        msg = info[len(info)-1]
        ircInfo = info[len(info)-2]
        chan = ircInfo[ircInfo.find('#'):].strip()

        for usr in usrInfo:
            if usr.startswith('id='):
                msgId = usr
                break

        if msg.lower().__contains__('@gaha_bot'):
            ws.send('@reply-parent-msg-' + msgId + ' PRIVMSG ' + chan + ' :Hey thanks for talking to me, as a bot I get kind of lonely, a lot')


def _on_close(ws: websocket, close_code, close_msg):
    print('Closed: ' + close_code + ', Message: ' + close_msg)

def startBot():
    ws = websocket.WebSocketApp('wss://irc-ws.chat.twitch.tv:443', on_open=_on_open, on_message=_on_message, on_error=_on_error, on_close=_on_close)
    ws.run_forever(dispatcher=rel)
    rel.signal(2, rel.abort)
    rel.dispatch()
    
    #This is for something else.... scrape.runParser(ws, 'butcoffee')