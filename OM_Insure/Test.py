from OM_Insure.Files.FilesSetup import *
from GlobalConfig.Entities import *

Entity = OMInsure[3]
print(getBalancesContent(Entity)+'\n\n')
print(getCodeCombinationsContent(Entity))