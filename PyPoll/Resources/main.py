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
    #find the final non duplicated candidates
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
print("----------------------------------------------")
outputpath=os.path.join('..','analysis','analysisPyPoll.txt')
with open(outputpath,'w') as txt:
    txt.write("Election Result\n")
    txt.write("----------------------------------------------\n")
    txt.write(f"Total Votes: {totalvote}\n")
    txt.write("----------------------------------------------\n")
    for ii in range(len(Finallist)):
        txt.write(f"{Finallist[ii]}: {percentageholder[ii]}% ({counttracker[ii]})\n")
    txt.write("----------------------------------------------\n")
    txt.write(f"Winner: {winner}\n") 
    txt.write("----------------------------------------------\n")
    

        
