import re
import statistics

def readWords(filename='cpu.dat'):
    return([i[0:i.index("\n")].split(", ") for i in list(open(filename))])

#Read in the CPU information database.
cpuList = readWords()

#Get user's CPU information.
userCPUName = input("What is your CPU's name?")
userCPUSpeed = float(input("What is your CPU's speed in GHz?"))
userCPUCore = int(input("What is your CPU's core count?"))

#Match the user's CPU core.
closestCoreCount=min([float(i[1]) for i in cpuList], key=lambda i:abs(i-userCPUCore))
coreMatch=[i for i in cpuList if float(i[1])==closestCoreCount]

#Match the user's CPU speed.
closestSpeed=min([float(i[2]) for i in coreMatch], key=lambda i:abs(i-userCPUSpeed))
matchList=[i for i in coreMatch if float(i[2])==closestSpeed]
matchNames=[i[0] for i in coreMatch if float(i[2])==closestSpeed]

#Predict the user's CPU's Cinebench score by averaging the matched CPU(s) scores.
predictedCinebench=statistics.mean([int(i[3]) for i in matchList])

#Print the results.
print("Your processor ("+userCPUName+") has a predicted Cinebench R20 Multithreaded score of "+str(predictedCinebench)+" and is most similar to the following CPU(s):\n"+"\n".join(matchNames))
