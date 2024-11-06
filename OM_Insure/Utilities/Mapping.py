from GlobalConfig.GlobalConfigFile import *

"""Balances File"""
def getLedgerName(Entity):
    ledgerName = {'BOT': 'MF Financial',
            'IFRS17': 'MF IFRS 17',
            'NAM': 'MF Production - FIN',
            'ZA': 'MF Financial'}
    return ledgerName[Entity]

def getLedgerID(Entity):
    ledgerID = {'BOT': '300000004185520',
            'IFRS17': '300000022988771',
            'NAM': '300000004185522',
            'ZA': '300000004185520'}
    return ledgerID[Entity]

def getCodeCombinationID():
    ID = randint(100000000000000, 999999999999999)
    return ID

def getCurrency(Entity):
    Currency = {'BOT': 'BWP',
            'IFRS17': 'ZAR',
            'NAM': 'NAD',
            'ZA': 'USD'}
    return Currency[Entity]

def getPeriodName(Entity):
    PeriodName = {'BOT': '23-Mar',
            'IFRS17': 'Adj-22',
            'NAM': '21-Aug',
            'ZA': '22-Jan'}
    return PeriodName[Entity]

def getTime():
    currentTime = datetime.today().strftime('%X')
    currentTime = str(currentTime)
    return currentTime

def getLastUpdatedBy(Entity):
    LastUpdatedBy = {'BOT': 'KMOSWETE',
            'IFRS17': 'NMUDAU',
            'NAM': 'TMBHELE',
            'ZA': 'ganesh.g.r@oracle.com'}
    return LastUpdatedBy[Entity]

def getValue(Entity):
    Value = {'BOT': getValue1(),
            'IFRS17': getValue2(),
            'NAM': getValue3(),
            'ZA': getValue4()}
    return Value[Entity]



"""Code Combinations File"""
def getChartOfAccountsID(Entity):
    ChartOfAccountsID = {'BOT': '4001',
            'IFRS17': '12001',
            'NAM': '4001',
            'ZA': '4001'}
    return ChartOfAccountsID[Entity]

def getAccountType(Entity):
    AccountType = {'BOT': 'O',
            'IFRS17': 'A',
            'NAM': 'E',
            'ZA': 'E'}
    return AccountType[Entity]

def getSegment1(Entity):
    Segment1 = {'BOT': 'BOT',
            'IFRS17': 'MFC',
            'NAM': 'NAM',
            'ZA': 'MFC'}
    return Segment1[Entity]

def getSegment2(Entity):
    Segment2 = {'BOT': '852',
            'IFRS17': 'ROP',
            'NAM': 'WD',
            'ZA': '884'}
    return Segment2[Entity]

def getSegment3(Entity):
    Segment3 = {'BOT': '85220',
            'IFRS17': 'ROPPL',
            'NAM': 'WDCGB',
            'ZA': '88410'}
    return Segment3[Entity]

def getSegment4(Entity):
    Segment4 = {'BOT': '310',
            'IFRS17': '4350',
            'NAM': '6370',
            'ZA': '7920'}
    return Segment4[Entity]

def getCreatedBy(Entity):
    CreatedBy = {'BOT': 'DCBDBE914C561C3DE053BA43660A2B49',
            'IFRS17': 'TMBHELE',
            'NAM': 'DCBDBE914C561C3DE053BA43660A2B49',
            'ZA': 'DCBDBE914C561C3DE053BA43660A2B49'}
    return CreatedBy[Entity]

def getLastUpdateLogin(Entity):
    LastUpdateLogin = {'BOT': 'E4E2CCA2174C0BF5E0538C645C0AC399',
            'IFRS17': 'FE84E2E01268BD4CE0538B645C0A66EE',
            'NAM': 'E4E2CCA2174C0BF5E0538C645C0AC399',
            'ZA': 'E4E2CCA2174C0BF5E0538C645C0AC399'}
    return LastUpdateLogin[Entity]
