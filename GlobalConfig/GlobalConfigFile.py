from random import *
import os
from datetime import datetime, timedelta

class TextFormat:
    end = '\033[0m'
    underline = '\033[4m'

def GreatPlainsDirectory():
    directory = 'C:\\Users\\x507964\\OneDrive - Old Mutual\\Desktop\\Group Finance\\Work\\Integrations\\Regression\\Great Plains'
    return directory

def OMInsureDirectory():
    directory = 'C:\\Users\\x507964\\OneDrive - Old Mutual\\Desktop\\Group Finance\\Work\\Integrations\\Regression\\OM Insure'
    return directory

def getFileTimeStamp():
    currentTime = datetime.today().strftime('%Y%m%d%H%M%S')
    currentTime = str(currentTime)
    return currentTime

def getFolderDateStamp():
    currentTime = datetime.today().strftime('%d %B %Y')
    currentTime = str(currentTime)
    return currentTime

def getSQLDateStamp():
    currentTime = datetime.today().strftime('%Y-%m-%d')
    currentTime = str(currentTime)
    return currentTime

def getValue1():
    multiplier = random()
    preValue = randint(10000,9999999)
    value = multiplier * preValue
    value = round(value,2)
    return value

def getValue2():
    multiplier = random()
    preValue = randint(10000,9999999)
    value = multiplier * preValue
    value = round(value,2)
    return value

def getValue3():
    multiplier = random()
    preValue = randint(10000,9999999)
    value = multiplier * preValue
    value = round(value,2)
    return value

def getValue4():
    multiplier = random()
    preValue = randint(10000,99999)
    value = multiplier * preValue
    value = round(value,2)
    return value

def getValue5():
    multiplier = random()
    preValue = randint(10000,99999)
    value = multiplier * preValue
    value = round(value,2)
    return value

def getControlFileMessage():
    message = TextFormat.underline + f"CONTROL FILE:" + TextFormat.end
    return message

def getOMIGSQL():
    date = getSQLDateStamp()
    sqlLine = ("\n" + TextFormat.underline + f"SQL QUERY TO RUN:" + TextFormat.end + "\n"
                f"select * from rubix_stage.omig_trialbalance where edl_process_dt > '{date}';")
    return sqlLine

def getOMInsureSQL():
    date = getSQLDateStamp()
    sqlLine = ("\n" + TextFormat.underline + f"SQL QUERIES TO RUN:" + TextFormat.end + "\n"
               f"select * from rubix_stage.omi_glbalances where edl_process_dt > '{date}';\n"
                f"select * from rubix_stage.omi_glcodecombination where edl_process_dt > '{date}';\n"
                f"select * from ubix_stage.omi_glcodedescriptions where edl_process_dt > '{date}';")
    return sqlLine



