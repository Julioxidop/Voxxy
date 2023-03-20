import logging
import json

#testing, staff
guilds = [1087237828670390382, 1087190146568437834]

def log(guild,input,ident=0):
    txtIdent = ident * "\t"
    print(f'[{guild}]{txtIdent}{input}')
    logging.info(f'[{guild}]{txtIdent}{input}')

def loadJson(dir):
    with open(dir, 'r') as f:
        return json.load(f)

def dumpJson(dir,data):
    with open(dir, 'w') as f:
        json.dump(data, f, indent = 4)