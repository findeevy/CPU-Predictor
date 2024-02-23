import re
import statistics

#Written by Fin Deevy
#Last updated 2024
#Example data created by ChatGPT, can be replaced with your data (CPU Name, Core Count, Speed (GHz), Cinebench Score).

def readWords(filename='cpu.dat'):
    return([i[0:i.index("\n")].split(", ") for i in list(open(filename))])

#Read in the CPU information database, split the CPU info at each comma.
cpuList = readWords()

#Get user's CPU information.
userCPUName = input("What is your CPU's name?")
userCPUSpeed = float(input("What is your CPU's speed in GHz?"))
userCPUCore = int(input("What is your CPU's core count?"))

#Match the user's CPU core count to a list of similar CPUs.
closestCoreCount=min([float(i[1]) for i in cpuList], key=lambda i:abs(i-userCPUCore))
coreMatch=[i for i in cpuList if float(i[1])==closestCoreCount]

#Match the user's CPU clock speed to CPUs with similar corecount.
closestSpeed=min([float(i[2]) for i in coreMatch], key=lambda i:abs(i-userCPUSpeed))
matchList=[i for i in coreMatch if float(i[2])==closestSpeed]
matchNames=[i[0] for i in coreMatch if float(i[2])==closestSpeed]

#Predict the user's CPU's Cinebench score by averaging the matched CPU(s) scores and calculating the difference in clock speed and core count.
predictedCinebench=statistics.mean([int(i[3]) for i in matchList])*(userCPUSpeed/closestSpeed)*(userCPUCore/closestCoreCount)

#Print the results to the user.
print("Your processor ("+userCPUName+") has a predicted Cinebench R20 Multithreaded score of "+str(int(predictedCinebench))+" and is most similar to the following CPU(s):\n"+"\n".join(matchNames))
