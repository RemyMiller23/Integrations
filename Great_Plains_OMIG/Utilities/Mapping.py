def getCompanyName(Entity):
    CompanyNames = {'FAGM': 'Futuregrowth Asset Management (Pty) Ltd',
                    'OASPV': 'Oa Aa Sa Pa Va',
                    'OMAIH': 'Old Mutual AIH',
                    'OMALT': 'Old Mutual ALT',
                    'OMAM': 'Old Mutual Investment Group',
                    'OMGH': 'Old Mutual GH',
                    'OMIHC': 'Old Mutual IHC',
                    'OMPRP': 'Old Mutual PRP',
                    'OSSPV': 'Oa Sa Sa Pa Va',
                    'UMBO': 'Ua Ma Ba Oa',
                    'WIN': 'Winterbreeze Trading'}
    return CompanyNames[Entity]

def getCompanySegment(Entity):
    CompanySegment = {'FAGM': '1730',
                    'OASPV': '1921',
                    'OMAIH': '1622',
                    'OMALT': '1521',
                    'OMAM': '1500',
                    'OMGH': '1621',
                    'OMIHC': '1600',
                    'OMPRP': '1900',
                    'OSSPV': '1821',
                    'UMBO': '1930',
                    'WIN': '1800'}
    return CompanySegment[Entity]

def getBSBOUTIQUE(Entity):
    BSBOUTIQUE = {'FAGM': '3000',
                    'OASPV': '0',
                    'OMAIH': '3000',
                    'OMALT': '0',
                    'OMAM': '0',
                    'OMGH': '0',
                    'OMIHC': '0',
                    'OMPRP': '0',
                    'OSSPV': '0',
                    'UMBO': '3000',
                    'WIN': '0'}
    return BSBOUTIQUE[Entity]

def getPALBOUTIQUE(Entity):
    PALBOUTIQUE = {'FAGM': '4700',
                    'OASPV': 'B400',
                    'OMAIH': '4700',
                    'OMALT': 'B400',
                    'OMAM': 'S250',
                    'OMGH': 'B400',
                    'OMIHC': 'S250',
                    'OMPRP': 'S250',
                    'OSSPV': 'B400',
                    'UMBO': '4700',
                    'WIN': 'S250'}
    return PALBOUTIQUE[Entity]

def getBSMainAccount(Entity):
    BSMainAccount = {'FAGM': '1655040',
                    'OASPV': '1655010',
                    'OMAIH': '1655040',
                    'OMALT': '1655010',
                    'OMAM': '1603320',
                    'OMGH': '1655010',
                    'OMIHC': '1603320',
                    'OMPRP': '1603320',
                    'OSSPV': '1655010',
                    'UMBO': '1655040',
                    'WIN': '1603320'}
    return BSMainAccount[Entity]

def getPALMainAccount(Entity):
    PALMainAccount = {'FAGM': '3158100',
                    'OASPV': '3022040',
                    'OMAIH': '3158100',
                    'OMALT': '3022040',
                    'OMAM': '5201091',
                    'OMGH': '3022040',
                    'OMIHC': '5201091',
                    'OMPRP': '5201091',
                    'OSSPV': '3022040',
                    'UMBO': '3158100',
                    'WIN': '5201091'}
    return PALMainAccount[Entity]

def getRelatedParty(MainAccount):
    RelatedParty = {'1655010': '204',
                    '1603320': '0',
                    '1655040': '1731',
                    '3022040': '0',
                    '3158100': '0',
                    '5201091': '0'}
    return RelatedParty[MainAccount]

def getRPCLUSTER(MainAccount):
    RPCLUSTER = {'1655010': '0',
                    '1603320': '0',
                    '1655040': '4',
                    '3022040': '0',
                    '3158100': '0',
                    '5201091': 'C450'}
    return RPCLUSTER[MainAccount]

def getAccountDescription(MainAccount):
    AccountDescription = {'1655010': 'Share Capital - Ordinary',
                    '1603320': 'Share Capital - Ordinary',
                    '1655040': 'Prov - Post Retirement Benefit',
                    '3022040': 'Salary - Permanent staff',
                    '3158100': 'Software License Fee',
                    '5201091': 'Salaries Permanent Staff'}
    return AccountDescription[MainAccount]



