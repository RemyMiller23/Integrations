from Great_Plains_OMIG.Files.FilesCreation import *
from GlobalConfig.Entities import *

"""Great Plains"""
for Entity in OMIG:
    print(f"Processing File: {Entity}")
    try:
        GenerateGreatPlainsFiles(Entity)
    except Exception as failure:
        print(f"Failed to process {Entity}: {failure}")


"""OMInsure"""
"""for Entity in OMInsure:
    print(f"Processing File: {Entity}")
    try:
        GenerateSourceFiles(Entity)
    except Exception as failure:
        print(f"Failed to process {Entity}: {failure}")"""

"""OMLACSA"""





