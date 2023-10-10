"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = dict()
    for item in items:
        itemAsString = str(item)
        #check if item in dict
        if itemAsString in frequencies:
            frequencies[itemAsString] +=1
        else:
            frequencies[itemAsString] = 1
    return frequencies
