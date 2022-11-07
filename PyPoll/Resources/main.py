import os 
import csv
csvpath=os.path.join('election_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
    header=next(csvreader)
    #print(header)
    #print(csvreader)
    L=list(csvreader)
    #print(L)
    totalvote=len(L)
    #print(totalvote)
    count=0
    counttracker=[]
    firstrow=L[0]
    firstcandidate=firstrow[2]
    candidate=[firstcandidate]
    aggragateList=[]
    for i in range(len(L)):
        element=L[i]
        elementname=element[2]
        aggragateList.append(elementname)
        # make a mega list with canndiate name occurance collection of all occurances
        if elementname in candidate:
                pass
        else: 
            candidate.append(elementname)
    Finallist=candidate
    #print(Finallist)
    for indexcounter in range(len(Finallist)):
        counttracker.append(0)
    #create a counter track the index of finalist
    for votedcanndiate in aggragateList:
        locationincountracker=Finallist.index(votedcanndiate)
        count=int(counttracker[locationincountracker])+1
        counttracker[locationincountracker]=count
        count= 0
    percentageholder=[]
    for eachendcount in counttracker:
        elementpercentage=round((eachendcount/totalvote)*100,3)
        percentageholder.append(elementpercentage)
    #print(counttracker)    
print("Election Result") 
print("----------------------------------------------")
print(f"Total Votes: {totalvote}")
print("----------------------------------------------")
for k in range(len(Finallist)):
    print(f"{Finallist[k]}: {percentageholder[k]}% ({counttracker[k]})")
print("----------------------------------------------")
winner=Finallist[percentageholder.index(max(percentageholder))]
print(f"Winner: {winner}")