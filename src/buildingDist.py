# Grid consisting of all school buildings used for classes

import math



A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7

#input the strings of the buildings to get the distance. For example, "CHEM", "ENGR"
#returns a float rounded to 2 decimal points.
def getDist(build1, build2):
    distance = round(math.sqrt(((keyDist[build1][0] - keyDist[build2][0])**2 + (keyDist[build1][1] - keyDist[build2][1])**2)), 2)
    return distance

#given a tuple with two items, find the closest building. A tuple is (1, 1). You can use capital letters instead for the first one, like (A, 1). Using it for the second one works but is not recommended for clarity.
# It returns the string of the abbreviation, not the distance itself.
def calcDist(location):
    minDist = 20
    nameMin = ""
    for key in keyDist:
        curDist = math.sqrt((keyDist[key][0] - location[0])**2 + (keyDist[key][1] - location[1])**2)
        if (curDist < minDist):
            nameMin = key
            minDist = curDist
    return nameMin


# An alphabetical list of all keys used.
keylist = ['AD', 'BIO', 'CHEM', 'ENGR', 'FA', 'ILSB', 'ITE', 'LH1', 'LIB', 'M/P', 'PAHB', 'PHYS', 'PUP', 'RAC', 'SHER', 'SOND', 'TRC', 'UC']

# A/B/C etc are assigned numbers. a/b/c are incorrect and will not work 
keyDist = { 'LIB':(D,5), 'TRC':(D,10), 'LH1':(F,6), 'BIO':(F,5), 'M/P':(F,5), 'CHEM':(F,5), 'FA':(F,5), 'PAHB':(F,4), 'ENGR':(F,5), 'ITE':(G,5), 'SHER':(G,5), 'UC':(F,5), 'AD':(G,5), 'SOND':(G,5), 'RAC':(G,6), 'ILSB':(F,6), 'PHYS':(E,7), 'PUP':(E,7) }


# Name of the building the code refers to, for reference.
keys = { 'LIB':'Albin O Kuhn Library and Gallery', 'TRC':'Technology Research Center', 'LH1':'Lecture Hall 1', 'BIO':'Biological Sciences Building', 'M/P':'Math and Psychology Building', 'CHEM':'Meyerhoff','FA':'Fine Arts Building', 'PAHB':'Performing Arts and Humanities Building', 'ENGR':'Engineering Building', 'ITE':'Information Technology/Engineering Building', 'SHER':'Sherman Hall', 'UC':'University Center', 'AD':'Administration Building', 'SOND':'Sondheim Hall', 'RAC':'Retriever Activities Center', 'ILSB':'Interdisciplinary Life Sciences Building', 'PHYS':'Physics Building', 'PUP':'Public Policy Building'}


#Contains the distance of each building to the given building. The list of list is sorted by the alphabetical order of the abbreviation of the building it corresponds to, and does not contain the building itself. i.e. a building with a distance of 0.0 in this list is a building in the same sector, but never the actual building itself. 

#To get the closest building, use sortedDistance[X][0], where X is the abbreviation's position in an alphabetical list of all abbreviations, "keylist", starting with "AD" at 0 and ending with "UC" at 17.
sortedDistance = [[(0.0, 'ITE'), (0.0, 'SHER'), (0.0, 'SOND'), (1.0, 'BIO'), (1.0, 'CHEM'), (1.0, 'ENGR'), (1.0, 'FA'), (1.0, 'M/P'), (1.0, 'RAC'), (1.0, 'UC'), (1.41, 'ILSB'), (1.41, 'LH1'), (1.41, 'PAHB'), (2.83, 'PHYS'), (2.83, 'PUP'), (3.0, 'LIB'), (5.83, 'TRC')], [(0.0, 'CHEM'), (0.0, 'ENGR'), (0.0, 'FA'), (0.0, 'M/P'), (0.0, 'UC'), (1.0, 'AD'), (1.0, 'ILSB'), (1.0, 'ITE'), (1.0, 'LH1'), (1.0, 'PAHB'), (1.0, 'SHER'), (1.0, 'SOND'), (1.41, 'RAC'), (2.0, 'LIB'), (2.24, 'PHYS'), (2.24, 'PUP'), (5.39, 'TRC')], [(0.0, 'BIO'), (0.0, 'ENGR'), (0.0, 'FA'), (0.0, 'M/P'), (0.0, 'UC'), (1.0, 'AD'), (1.0, 'ILSB'), (1.0, 'ITE'), (1.0, 'LH1'), (1.0, 'PAHB'), (1.0, 'SHER'), (1.0, 'SOND'), (1.41, 'RAC'), (2.0, 'LIB'), (2.24, 'PHYS'), (2.24, 'PUP'), (5.39, 'TRC')], [(0.0, 'BIO'), (0.0, 'CHEM'), (0.0, 'FA'), (0.0, 'M/P'), (0.0, 'UC'), (1.0, 'AD'), (1.0, 'ILSB'), (1.0, 'ITE'), (1.0, 'LH1'), (1.0, 'PAHB'), (1.0, 'SHER'), (1.0, 'SOND'), (1.41, 'RAC'), (2.0, 'LIB'), (2.24, 'PHYS'), (2.24, 'PUP'), (5.39, 'TRC')], [(0.0, 'BIO'), (0.0, 'CHEM'), (0.0, 'ENGR'), (0.0, 'M/P'), (0.0, 'UC'), (1.0, 'AD'), (1.0, 'ILSB'), (1.0, 'ITE'), (1.0, 'LH1'), (1.0, 'PAHB'), (1.0, 'SHER'), (1.0, 'SOND'), (1.41, 'RAC'), (2.0, 'LIB'), (2.24, 'PHYS'), (2.24, 'PUP'), (5.39, 'TRC')], [(0.0, 'LH1'), (1.0, 'BIO'), (1.0, 'CHEM'), (1.0, 'ENGR'), (1.0, 'FA'), (1.0, 'M/P'), (1.0, 'RAC'), (1.0, 'UC'), (1.41, 'AD'), (1.41, 'ITE'), (1.41, 'PHYS'), (1.41, 'PUP'), (1.41, 'SHER'), (1.41, 'SOND'), (2.0, 'PAHB'), (2.24, 'LIB'), (4.47, 'TRC')], [(0.0, 'AD'), (0.0, 'SHER'), (0.0, 'SOND'), (1.0, 'BIO'), (1.0, 'CHEM'), (1.0, 'ENGR'), (1.0, 'FA'), (1.0, 'M/P'), (1.0, 'RAC'), (1.0, 'UC'), (1.41, 'ILSB'), (1.41, 'LH1'), (1.41, 'PAHB'), (2.83, 'PHYS'), (2.83, 'PUP'), (3.0, 'LIB'), (5.83, 'TRC')], [(0.0, 'ILSB'), (1.0, 'BIO'), (1.0, 'CHEM'), (1.0, 'ENGR'), (1.0, 'FA'), (1.0, 'M/P'), (1.0, 'RAC'), (1.0, 'UC'), (1.41, 'AD'), (1.41, 'ITE'), (1.41, 'PHYS'), (1.41, 'PUP'), (1.41, 'SHER'), (1.41, 'SOND'), (2.0, 'PAHB'), (2.24, 'LIB'), (4.47, 'TRC')], [(2.0, 'BIO'), (2.0, 'CHEM'), (2.0, 'ENGR'), (2.0, 'FA'), (2.0, 'M/P'), (2.0, 'UC'), (2.24, 'ILSB'), (2.24, 'LH1'), (2.24, 'PAHB'), (2.24, 'PHYS'), (2.24, 'PUP'), (3.0, 'AD'), (3.0, 'ITE'), (3.0, 'SHER'), (3.0, 'SOND'), (3.16, 'RAC'), (5.0, 'TRC')], [(0.0, 'BIO'), (0.0, 'CHEM'), (0.0, 'ENGR'), (0.0, 'FA'), (0.0, 'UC'), (1.0, 'AD'), (1.0, 'ILSB'), (1.0, 'ITE'), (1.0, 'LH1'), (1.0, 'PAHB'), (1.0, 'SHER'), (1.0, 'SOND'), (1.41, 'RAC'), (2.0, 'LIB'), (2.24, 'PHYS'), (2.24, 'PUP'), (5.39, 'TRC')], [(1.0, 'BIO'), (1.0, 'CHEM'), (1.0, 'ENGR'), (1.0, 'FA'), (1.0, 'M/P'), (1.0, 'UC'), (1.41, 'AD'), (1.41, 'ITE'), (1.41, 'SHER'), (1.41, 'SOND'), (2.0, 'ILSB'), (2.0, 'LH1'), (2.24, 'LIB'), (2.24, 'RAC'), (3.16, 'PHYS'), (3.16, 'PUP'), (6.32, 'TRC')], [(0.0, 'PUP'), (1.41, 'ILSB'), (1.41, 'LH1'), (2.24, 'BIO'), (2.24, 'CHEM'), (2.24, 'ENGR'), (2.24, 'FA'), (2.24, 'LIB'), (2.24, 'M/P'), (2.24, 'RAC'), (2.24, 'UC'), (2.83, 'AD'), (2.83, 'ITE'), (2.83, 'SHER'), (2.83, 'SOND'), (3.16, 'PAHB'), (3.16, 'TRC')], [(0.0, 'PHYS'), (1.41, 'ILSB'), (1.41, 'LH1'), (2.24, 'BIO'), (2.24, 'CHEM'), (2.24, 'ENGR'), (2.24, 'FA'), (2.24, 'LIB'), (2.24, 'M/P'), (2.24, 'RAC'), (2.24, 'UC'), (2.83, 'AD'), (2.83, 'ITE'), (2.83, 'SHER'), (2.83, 'SOND'), (3.16, 'PAHB'), (3.16, 'TRC')], [(1.0, 'AD'), (1.0, 'ILSB'), (1.0, 'ITE'), (1.0, 'LH1'), (1.0, 'SHER'), (1.0, 'SOND'), (1.41, 'BIO'), (1.41, 'CHEM'), (1.41, 'ENGR'), (1.41, 'FA'), (1.41, 'M/P'), (1.41, 'UC'), (2.24, 'PAHB'), (2.24, 'PHYS'), (2.24, 'PUP'), (3.16, 'LIB'), (5.0, 'TRC')], [(0.0, 'AD'), (0.0, 'ITE'), (0.0, 'SOND'), (1.0, 'BIO'), (1.0, 'CHEM'), (1.0, 'ENGR'), (1.0, 'FA'), (1.0, 'M/P'), (1.0, 'RAC'), (1.0, 'UC'), (1.41, 'ILSB'), (1.41, 'LH1'), (1.41, 'PAHB'), (2.83, 'PHYS'), (2.83, 'PUP'), (3.0, 'LIB'), (5.83, 'TRC')], [(0.0, 'AD'), (0.0, 'ITE'), (0.0, 'SHER'), (1.0, 'BIO'), (1.0, 'CHEM'), (1.0, 'ENGR'), (1.0, 'FA'), (1.0, 'M/P'), (1.0, 'RAC'), (1.0, 'UC'), (1.41, 'ILSB'), (1.41, 'LH1'), (1.41, 'PAHB'), (2.83, 'PHYS'), (2.83, 'PUP'), (3.0, 'LIB'), (5.83, 'TRC')], [(3.16, 'PHYS'), (3.16, 'PUP'), (4.47, 'ILSB'), (4.47, 'LH1'), (5.0, 'LIB'), (5.0, 'RAC'), (5.39, 'BIO'), (5.39, 'CHEM'), (5.39, 'ENGR'), (5.39, 'FA'), (5.39, 'M/P'), (5.39, 'UC'), (5.83, 'AD'), (5.83, 'ITE'), (5.83, 'SHER'), (5.83, 'SOND'), (6.32, 'PAHB')], [(0.0, 'BIO'), (0.0, 'CHEM'), (0.0, 'ENGR'), (0.0, 'FA'), (0.0, 'M/P'), (1.0, 'AD'), (1.0, 'ILSB'), (1.0, 'ITE'), (1.0, 'LH1'), (1.0, 'PAHB'), (1.0, 'SHER'), (1.0, 'SOND'), (1.41, 'RAC'), (2.0, 'LIB'), (2.24, 'PHYS'), (2.24, 'PUP'), (5.39, 'TRC')]]
