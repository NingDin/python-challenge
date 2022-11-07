import os 
import csv
# build path
csvpath=os.path.join('budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
    header=next(csvreader)
    print(f"this is header prcossed: {header}")
    L=list(csvreader)
    changetracker=[]
    #print(L)
    mounthcount=1
    # now switch to index loop
    profitloss=0
    culmulativechange=0
    for i in range(0,len(L)-1):
        row=L[i]
        #print(row)
        profitloss+=int(row[1])
        #print(f"{row[1]}")

        timeaggregagte=row[0].split('-')
        month=timeaggregagte[0]
        #print(month)
        rownext=L[i+1]
        timeaggregagtenext=rownext[0].split('-')
        monthnext=timeaggregagtenext[0]
        #print(monthnext)
        if month !=monthnext:
            mounthcount+=1
        thismonthProfitloss=int(row[1])
        nextmontProfitloss=int(rownext[1])
        change=nextmontProfitloss-thismonthProfitloss
        culmulativechange=culmulativechange+change
        changetracker.append(change)
Lastrow=L[len(L)-1]
lastprofitloss=Lastrow[1]
#print(type(lastprofitloss))
finalprofitloss=profitloss+int(lastprofitloss)
#print(mounthcount)
#print(finalprofitloss)
avgChange=culmulativechange/(int(mounthcount)-1)
#print(avgChange)
#print(changetracker)
largest=max(changetracker)
minvalue=min(changetracker)
#print(largest)
largestincreasechangeset=L[changetracker.index(largest)+1]
yearLargestincreasehappened=largestincreasechangeset[0]
#print(yearLargestincreasehappened)
#print(minvalue)
largestDecreaseChangeset=L[changetracker.index(minvalue)+1]
yearLargestDecreasehappend=largestDecreaseChangeset[0]
#print(yearLargestDecreasehappend)

print("Financial Analysis")
print("-----------------------------------")
print(f"Total:{mounthcount}")
print(f'Total: ${finalprofitloss}')
print(f"Average Count: ${round((avgChange),2)}")
print(f"Greatest Increasse in Profits: {yearLargestincreasehappened} (${largest})")
print(f"Greatest Decreasse in Profits: {yearLargestDecreasehappend} (${minvalue})")