import time
from OM_Insure.Files.FilesSetup import *
from GlobalConfig.GlobalConfigFile import *
from GlobalConfig.Entities import *

ControlFileTimeStampLabel = None
header_written = False
def GenerateOMInsureFiles(Entity):

    output_directory = os.path.join(os.getcwd(),f'{OMInsureDirectory()}\\{getFolderDateStamp()}')
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    """Source File Name Variables"""
    FileTimeStampLabel = getFileTimeStamp()
    file_name = f'GL_OMIG_{Entity}_{FileTimeStampLabel}.txt'

    """Source File Setup"""
    output_file_path = os.path.join(output_directory,file_name)

    with open(output_file_path, 'w') as fileCreation:
        fileCreation.write(contentHeader())
        fileCreation.write(contentBalanceSheetPostingType(Entity))
        fileCreation.write(contentProfitAndLossPostingType(Entity))
    fileCreation.close()

    file = f'GL_OMIG_{Entity}_{getFileTimeStamp()}.txt'
    print(file+"\n")


    """Directory to Source File"""
    file_directory = f'{OMInsureDirectory()}\\{getFolderDateStamp()}\\{file}'

    """Counting Content Rows in Source File"""
    with open(file_directory, 'r') as fileReading:
        rows = len(fileReading.readlines()) - 1
    fileReading.close()

    row_count = str(rows)

    """Getting Content from Source File"""
    with open(file_directory, 'r') as fileReading:
        contents = fileReading.readlines()
    fileReading.close()

    """Creating Lists of Debits and Credits"""
    debits, credits = [], []

    for values in contents:
        numvalues = values.replace('\n', '').split('\t')
        debits.append(numvalues[12])
        credits.append(numvalues[13])

    """"Summing Debits and Credits"""
    debit1 = float(debits[1])
    debit2 = float(debits[2])
    SumOfDebits = str(round(debit1 + debit2, 2))

    credit1 = float(credits[1])
    credit2 = float(credits[2])
    SumOfCredits = str(round(credit1 + credit2, 2))

    """Control File Creation"""
    global header_written
    global ControlFileTimeStampLabel
    if ControlFileTimeStampLabel is None:
        ControlFileTimeStampLabel = getFileTimeStamp()

    control_file_name = f'CONTROL_OMIG_{ControlFileTimeStampLabel}.csv'

    control_output_file_path = os.path.join(output_directory, control_file_name)

    with open(control_output_file_path, 'a') as controlFileCreation:
        if not header_written:
            controlFileCreation.write(getControlFileHeader())
            header_written = True
        line = f'{file},{row_count},{SumOfDebits},{SumOfCredits}\n'
        controlFileCreation.write(line)
    controlFileCreation.close()

    time.sleep(1)

    if Entity == OMIG[-1]:
        print(getControlFileMessage())
        print(f'{control_file_name}\n{output_directory}')
        return print(f'{getOMIGSQL()}')

