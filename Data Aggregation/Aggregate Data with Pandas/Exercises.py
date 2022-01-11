#6
grouped = happiness2015.groupby('Region')

#g7
grouped = happiness2015.groupby('Region')

#8
grouped = happiness2015.groupby('Region')
#9
import numpy as np
grouped = happiness2015.groupby('Region')
happy_grouped = grouped['Happiness Score']
def dif(group):
    return (group.max() - group.mean())

