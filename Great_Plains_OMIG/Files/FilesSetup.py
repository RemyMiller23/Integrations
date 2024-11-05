from Great_Plains_OMIG.Utilities.Mapping import *
from GlobalConfig.GlobalConfigFile import *

"""OMIG File"""
def getOMIGHeader():
    headerLine = 'CompanyID\tCompanyName\tYEAR1\tPERIODID\tCompany_Segment\tBOUTIQUE\tMAIN_ACCOUNT\tRELATED_PARTY\tRPCLUSTER\tACCOUNT_DESCRIPTION\tPOSTING_TYPE\tOPENING_BALANCE\tMTD_DEBITAMT\tMTD_CREDITAMT\tMTD_MOVEMENT\tYTD_BALANCE\n'
    return headerLine

def getOMIGBalanceSheetPostingType(Entity):

    CompanyID = Entity
    CompanyName = getCompanyName(Entity)
    YEAR1 = '2021'
    PERIODID = '2'
    Company_Segment = getCompanySegment(Entity)
    BOUTIQUE = getBSBOUTIQUE(Entity)
    MAIN_ACCOUNT = getBSMainAccount(Entity)
    RELATED_PARTY = getRelatedParty(MAIN_ACCOUNT)
    RPCLUSTER = getRPCLUSTER(MAIN_ACCOUNT)
    ACCOUNT_DESCRIPTION = getAccountDescription(MAIN_ACCOUNT)
    POSTING_TYPE = 'Balance Sheet'
    OPENING_BALANCE = getValue1()
    MTD_DEBITAMT = getValue2()
    MTD_CREDITAMT = getValue3()
    MTD_MOVEMENT = round(MTD_DEBITAMT - MTD_CREDITAMT,2)
    YTD_BALANCE = round(OPENING_BALANCE - MTD_CREDITAMT,2)

    BSLine = CompanyID + '\t' + CompanyName + '\t' + YEAR1 + '\t' + PERIODID + '\t' +Company_Segment + '\t' + BOUTIQUE + '\t' + MAIN_ACCOUNT + '\t' + RELATED_PARTY + '\t' + RPCLUSTER + '\t' + ACCOUNT_DESCRIPTION + '\t' + POSTING_TYPE + '\t' + str(OPENING_BALANCE) + '\t' + str(MTD_DEBITAMT) + '\t' + str(MTD_CREDITAMT) + '\t' + str(MTD_MOVEMENT) + '\t' + str(YTD_BALANCE) + '\n'
    return BSLine

def getOMIGProfitAndLossPostingType(Entity):

    CompanyID = Entity
    CompanyName = getCompanyName(Entity)
    YEAR1 = '2021'
    PERIODID = '2'
    Company_Segment = getCompanySegment(Entity)
    BOUTIQUE = getPALBOUTIQUE(Entity)
    MAIN_ACCOUNT = getPALMainAccount(Entity)
    RELATED_PARTY = getRelatedParty(MAIN_ACCOUNT)
    RPCLUSTER = getRPCLUSTER(MAIN_ACCOUNT)
    ACCOUNT_DESCRIPTION = getAccountDescription(MAIN_ACCOUNT)
    POSTING_TYPE = 'Profit and Loss'
    OPENING_BALANCE = '0.00'
    MTD_DEBITAMT = getValue4()
    MTD_CREDITAMT = getValue5()
    MTD_MOVEMENT = round(MTD_DEBITAMT - MTD_CREDITAMT,2)
    YTD_BALANCE = round(MTD_CREDITAMT,2)

    PALLine = CompanyID + '\t' + CompanyName + '\t' + YEAR1 + '\t' + PERIODID + '\t' + Company_Segment + '\t' + BOUTIQUE + '\t' + MAIN_ACCOUNT + '\t' + RELATED_PARTY + '\t' + RPCLUSTER + '\t' + ACCOUNT_DESCRIPTION + '\t' + POSTING_TYPE + '\t' + str(OPENING_BALANCE) + '\t' + str(MTD_DEBITAMT) + '\t' + str(MTD_CREDITAMT) + '\t' + str(MTD_MOVEMENT) + '\t' + str(YTD_BALANCE)
    return PALLine

"""Control File"""
def getControlFileHeader():
    headerLine = 'SOURCE_FILE_NAME'+','+'ROW_COUNT'+','+'TOTAL_DR'+','+'TOTAL_CR'+'\n'
    return headerLine










