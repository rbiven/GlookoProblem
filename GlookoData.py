# Import libraries
import numpy as np
import pandas as pd
from time import time
import matplotlib.pyplot as plt
import datetime

#########################################################################
# FreeStyle
#########################################################################
print "---------------------------------------------------------------------"
# Read CSV
company = pd.read_csv("FreeStyle.csv")
print "FreeStyle data read successfully!"

# Convert Date of Tweet column to datetime
company['Date of Tweet'] = pd.to_datetime(company['Date of Tweet'])

# Find data within the month of November
Novem = company['Date of Tweet'].between(datetime.datetime(2016,11,1), datetime.datetime(2016,12,1), inclusive=False)

index = []
for x in range(len(Novem)):
    if Novem[x] == False:
        index.append(x)
        x += 1
    else:
        x += 1

company = company.drop(company.index[index])

# Calculate number of readings
n_readings = len(company['Date of Tweet'])

# Calculate number of features
n_features = len(company.keys())

# Print the results
print "Total number of readings: {}".format(n_readings)
#print "Number of features: {}".format(n_features)

avgRetw   = company['Number of Retweets'].mean()        # Average number of retweets
DecFav    = company['Number of Favorites'][1]           # Number of Favorites at end of Campaign
NovFav    = company['Number of Favorites'][n_readings]  # Number of Favorites at beginning of Campaign
AddFav    = DecFav - NovFav                             # Increase or decrease in Favorites at end Campaign
TRetw     = company['Number of Retweets'].sum()         # Total number of retweets 
MaxFol    = company['Number of Followers'].max()        # Max number of retweets 
MinFol    = company['Number of Followers'].min()        # Min number of retweets 
DecFol    = company['Number of Followers'][1]           # Number of followers at end of Campaign
NovFol    = company['Number of Followers'][n_readings]  # Number of followers at beginning of Campaign
Range     = MaxFol - MinFol                             # Increase or decrease in followers at end Campaign
PerCapRT  = float(TRetw) / DecFol                       # Total retweets / total follower
PerCapFav = float(AddFav) / DecFol                      # Additional favorite / total follower
PerCapT   = float(n_readings) / DecFol                  # Number of tweets / total follower 

print "Total Number of Retweets in November =",TRetw
print "Total Number of New Favorited Tweets in Nov =",AddFav
print "Average Number of Retweets =",avgRetw
print "Followers at the Beginning of Campaign =",NovFol
print "Followers at the End of Campaign =",DecFol
print "Range (+ additional followers / - reduction in followers) =",Range
print "Per Cap Tweet and Retweets =", PerCapT, PerCapRT
print "---------------------------------------------------------------------"


#########################################################################
# Accucheck_us
#########################################################################
print "---------------------------------------------------------------------"
# Read CSV data
company1 = pd.read_csv("accucheck_us.csv")
print "AccuCheck data read successfully!"

# Convert Date of Tweet column to datetime
company1['Date of Tweet'] = pd.to_datetime(company1['Date of Tweet'])

# Find data within the month of November
Novem1 = company1['Date of Tweet'].between(datetime.datetime(2016,11,1), datetime.datetime(2016,12,1), inclusive=False)

index = []
for x in range(len(Novem1)):
    if Novem1[x] == False:
        index.append(x)
        x += 1
    else:
        x += 1

company1 = company1.drop(company1.index[index])

# Calculate number of readings
n_readings = len(company1['Date of Tweet'])

# Calculate number of features
n_features = len(company1.keys())

# Print the results
print "Total number of readings: {}".format(n_readings)

avgRetw1   = company1['Number of Retweets'].mean()
DecFav1    = company1['Number of Favorites'][0]
NovFav1    = company1['Number of Favorites'][n_readings-1]
AddFav1    = DecFav1 - NovFav1
TRetw1     = company1['Number of Retweets'].sum()
MaxFol1    = company1['Number of Followers'].max()
MinFol1    = company1['Number of Followers'].min()
DecFol1    = company1['Number of Followers'][0]
NovFol1    = company1['Number of Followers'][n_readings-1]
Range1     = MaxFol1 - MinFol1
PerCapRT1  = float(TRetw1) / DecFol1
PerCapFav1 = float(AddFav1) / DecFol1
PerCapT1   = float(n_readings) / DecFol1

print "Total Number of Retweets in November =",TRetw1
print "Total Number of New Favorited Tweets in Nov =",AddFav1
print "Average Number of Retweets =",avgRetw1
print "Followers at the Beginning of Campaign =",NovFol1
print "Followers at the End of Campaign =",DecFol1
print "Range (+ additional followers / - reduction in followers) =",Range1
print "Per Cap Tweet and Retweets =", PerCapT1, PerCapRT1
print "---------------------------------------------------------------------"

#########################################################################
# OneTouch
#########################################################################
print "---------------------------------------------------------------------"
# Read CSV data
company2 = pd.read_csv("onetouch.csv")
print "OneTouch data read successfully!"

# Convert date of Tweet column to datetime
company2['Date of Tweet'] = pd.to_datetime(company2['Date of Tweet'])

# Find Data within the month of November
Novem2 = company2['Date of Tweet'].between(datetime.datetime(2016,11,1), datetime.datetime(2016,12,1), inclusive=False)

index = []
for x in range(len(Novem2)):
    if Novem2[x] == False:
        index.append(x)
        x += 1
    else:
        x += 1

company2 = company2.drop(company2.index[index])

# Calculate number of readings
n_readings = len(company2['Date of Tweet'])

# Calculate number of features
n_features = len(company2.keys())

# Print the results
print "Total number of readings: {}".format(n_readings)

avgRetw2   = company2['Number of Retweets'].mean()
DecFav2    = company2['Number of Favorites'][0]
NovFav2    = company2['Number of Favorites'][n_readings-1]
AddFav2    = DecFav2 - NovFav2
TRetw2     = company2['Number of Retweets'].sum()
MaxFol2    = company2['Number of Followers'].max()
MinFol2    = company2['Number of Followers'].min()
DecFol2    = company2['Number of Followers'][0]
NovFol2    = company2['Number of Followers'][n_readings-1]
Range2     = MaxFol2 - MinFol2
PerCapRT2  = float(TRetw2) / DecFol2
PerCapFav2 = float(AddFav2) / DecFol2
PerCapT2   = float(n_readings) / DecFol2

print "Total Number of Retweets in November =",TRetw2
print "Total Number of New Favorited Tweets in Nov =",AddFav2
print "Average Number of Retweets =",avgRetw2
print "Followers at the Beginning of Campaign =",NovFol2
print "Followers at the End of Campaign =",DecFol2
print "Range (+ additional followers / - reduction in followers) =",Range2
print "Per Cap Tweet and Retweets =", PerCapT2, PerCapRT2
print "---------------------------------------------------------------------"


#########################################################################
# MyOmnipod
#########################################################################
print "---------------------------------------------------------------------"
# Read CSV data
company3 = pd.read_csv("OP.csv")
print "MyOmnipod data read successfully!"

# Convert Date of Tweet column to datetime
company3['Date of Tweet'] = pd.to_datetime(company3['Date of Tweet'])

# Find data within the month of November
Novem3 = company3['Date of Tweet'].between(datetime.datetime(2016,11,1), datetime.datetime(2016,12,1), inclusive=False)

index = []
for x in range(len(Novem3)):
    if Novem3[x] == False:
        index.append(x)
        x += 1
    else:
        x += 1

company3 = company3.drop(company3.index[index])

# Calculate number of readings
n_readings = len(company3['Date of Tweet'])

# Calculate number of features
n_features = len(company3.keys())

# Print the results
print "Total number of readings: {}".format(n_readings)

avgRetw3   = company3['Number of Retweets'].mean()
DecFav3    = company3['Number of Favorites'][0]
NovFav3    = company3['Number of Favorites'][n_readings-1]
AddFav3    = DecFav3 - NovFav3
TRetw3     = company3['Number of Retweets'].sum()
MaxFol3    = company3['Number of Followers'].max()
MinFol3    = company3['Number of Followers'].min()
DecFol3    = company3['Number of Followers'][0]
NovFol3    = company3['Number of Followers'][n_readings-1]
Range3     = MaxFol3 - MinFol3
PerCapRT3  = float(TRetw3) / DecFol3
PerCapFav3 = float(AddFav3) / DecFol3
PerCapT3   = float(n_readings) / DecFol3

print "Total Number of Retweets in November =",TRetw3
print "Total Number of New Favorited Tweets in Nov =",AddFav3
print "Average Number of Retweets =",avgRetw3
print "Followers at the Beginning of Campaign =",NovFol3
print "Followers at the End of Campaign =",DecFol3
print "Range (+ additional followers / - reduction in followers) =",Range3
print "Per Cap Tweet and Retweets =", PerCapT3, PerCapRT3
print "---------------------------------------------------------------------"

#########################################################################
# Tandem Diabetes Care
#########################################################################
print "---------------------------------------------------------------------"
# Read CSV data
company4 = pd.read_csv("tandem.csv")
print "Tandem Diabetes Care data read successfully!"

# Convert Date of Tweet column to datetime
company4['Date of Tweet'] = pd.to_datetime(company4['Date of Tweet'])

# Find data within the month of November
Novem4 = company4['Date of Tweet'].between(datetime.datetime(2016,11,1), datetime.datetime(2016,12,1), inclusive=False)

index = []
for x in range(len(Novem4)):
    if Novem4[x] == False:
        index.append(x)
        x += 1
    else:
        x += 1

company4 = company4.drop(company4.index[index])

# Calculate number of readings
n_readings = len(company4['Date of Tweet'])

# Calculate number of features
n_features = len(company4.keys())

# Print the results
print "Total number of readings: {}".format(n_readings)

avgRetw4   = company4['Number of Retweets'].mean()          
DecFav4    = company4['Number of Favorites'][0]             
NovFav4    = company4['Number of Favorites'][n_readings-1]
AddFav4    = DecFav4 - NovFav4
TRetw4     = company4['Number of Retweets'].sum()
MaxFol4    = company4['Number of Followers'].max()
MinFol4    = company4['Number of Followers'].min()
DecFol4    = company4['Number of Followers'][0]
NovFol4    = company4['Number of Followers'][n_readings-1]
Range4     = MaxFol4 - MinFol4
PerCapRT4  = float(TRetw4) / DecFol4
PerCapFav4 = float(AddFav4) / DecFol4
PerCapT4   = float(n_readings) / DecFol4

print "Total Number of Retweets in November =",TRetw4
print "Total Number of New Favorited Tweets in Nov =",AddFav4
print "Average Number of Retweets =",avgRetw4
print "Followers at the Beginning of Campaign =",NovFol4
print "Followers at the End of Campaign =",DecFol4
print "Range (+ additional followers / - reduction in followers) =",Range4
print "Per Cap Tweet and Retweets =", PerCapT4, PerCapRT4
print "---------------------------------------------------------------------"

#########################################################################
# Medtronic Diabetes
#########################################################################
print "---------------------------------------------------------------------"
# Read CSV data
company5 = pd.read_csv("Medt.csv")
print "Medtronic Diabetes data read successfully!"

# Convert Date of Tweet column to datetime
company5['Date of Tweet'] = pd.to_datetime(company5['Date of Tweet'])

# Find data within the month of November
Novem5 = company5['Date of Tweet'].between(datetime.datetime(2016,11,1), datetime.datetime(2016,12,1), inclusive=False)

index = []
for x in range(len(Novem5)):
    if Novem5[x] == False:
        index.append(x)
        x += 1
    else:
        x += 1

company5 = company5.drop(company5.index[index])

# Calculate number of readings
n_readings = len(company5['Date of Tweet'])

# Calculate number of features
n_features = len(company5.keys())

# Print the results
print "Total number of readings: {}".format(n_readings)

avgRetw5   = company5['Number of Retweets'].mean()
DecFav5    = company5['Number of Favorites'][0]
NovFav5    = company5['Number of Favorites'][n_readings-1]
AddFav5    = DecFav5 - NovFav5
TRetw5     = company5['Number of Retweets'].sum()
MaxFol5    = company5['Number of Followers'].max()
MinFol5    = company5['Number of Followers'].min()
DecFol5    = company5['Number of Followers'][0]
NovFol5    = company5['Number of Followers'][n_readings-1]
Range5     = MaxFol5 - MinFol5
PerCapRT5  = float(TRetw5) / DecFol5
PerCapFav5 = float(AddFav5) / DecFol5
PerCapT5   = float(n_readings) / DecFol5

print "Total Number of Retweets in November =",TRetw5
print "Total Number of New Favorited Tweets in Nov =",AddFav5
print "Average Number of Retweets =",avgRetw5
print "Followers at the Beginning of Campaign =",NovFol5
print "Followers at the End of Campaign =",DecFol5
print "Range (+ additional followers / - reduction in followers) =",Range5
print "Per Cap Tweet and Retweets =", PerCapT5, PerCapRT5
print "---------------------------------------------------------------------"

#########################################################################
# Read Company data - this data is used for current information.
Comp_data = pd.read_csv("comp.csv")
print "Company present data read successfully!"
#########################################################################

#########################################################################
# Below will build bar graph
#########################################################################

CompTweets = [PerCapT,PerCapT1,PerCapT2,PerCapT3,PerCapT4,PerCapT5]
CompRetweetsPC = [PerCapRT,PerCapRT1,PerCapRT2,PerCapRT3,PerCapRT4,PerCapRT5]
CompFollower = [DecFol,DecFol1,DecFol2,DecFol3,DecFol4,DecFol5]


fig, ax = plt.subplots()

x = np.arange(len(CompTweets))
bar_width = 0.35

rects1 = plt.bar(x, CompTweets, bar_width,
                 color='b',
                 label='Number of Tweets / Total Followers')

rects2 = plt.bar(x + bar_width,CompRetweetsPC, bar_width,
                 color='r',
                 label='Number of Retweets / Total Followers')


plt.xlabel('Companies')
plt.ylabel('Average Scores')
plt.title('Proportional Amounts of Tweets & ReTweets')
plt.xticks(x + bar_width / 2, ('FreeStyle', 'AccuCheck', 'OneTouch', 'Omnipod', 'Tandem', 'Medtronic'))
plt.legend()

plt.tight_layout()
plt.show()

