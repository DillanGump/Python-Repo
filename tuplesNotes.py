imelda = "More Mayhem", "Imelda May", 2011, [
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
]



#range variable to iterate through a tuple?
#albumInfo = range(0,3)
for i in imelda[:3] :
    print(i)

trackList = imelda[3]
print("Tracks: {}".format(len(trackList)))
for i in trackList :
    trackNo, trackTitle = i
    print("\t#{0}. {1}".format(trackNo, trackTitle))

imelda[3].append((5, "All For You"))

for i in imelda[:3] :
    print(i)

#extracting trackList from the tuple subsequent times resets update
print("Tracks: {}".format(len(trackList)))
for i in trackList :
    trackNo, trackTitle = i
    print("\t#{0}. {1}".format(trackNo, trackTitle))

trackList.append((6, "Eternity"))

for i in imelda[:3] :
    print(i)

#extracting trackList from the tuple subsequent times resets update
print("Tracks: {}".format(len(trackList)))
for i in trackList :
    trackNo, trackTitle = i
    print("\t#{0}. {1}".format(trackNo, trackTitle))

# tuples are a data structure that are immutable. Their items cannot be updated. 
# tuple items, coming in all types, notable lists, must be extracted and saved 
# as a new variable. The original data goes unchaged, but allows the information
# to be transformed rather than only read. Use of tuples is prudent when sharing
# data and want to preserve the original structure throughout the code. 
# I expect tuples to be useful when taking in data from large silos and 
# transforming raw data into analyzable lists


#this file would be a good one to practice functions on