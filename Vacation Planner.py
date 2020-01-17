#Emmanuel Roy
import datetime
import random
import math
options = ("Snorkling","Scuba Diving","Fishing","Sunbathing","Shopping","Helicopter Ride","Sleeping")
prices  = (10.00, 150.00, 25.00, 0.00, 200.00, 450.00, 0.00)
# get and parse vacation starting and ending dates
startDateString = input("Enter the starting date of your vacation (MM/DD/YYYY):")
startDate= datetime.datetime.strptime(startDateString,"%m/%d/%Y")
stopDateString = input("Enter the ending date of your vacation (MM/DD/YYYY):")
stopDate = datetime.datetime.strptime(stopDateString,"%m/%d/%Y")
delta =stopDate-startDate
print("Your vacation is {} days long.".format(delta.days))
costs=[]
for i in range(0, delta.days):
    activityIndex=random.randrange(0, len(options))
    activity=options[activityIndex]
    cost=prices[activityIndex]
    thisDate=startDate+datetime.timedelta(days=i)
    thisDateString = datetime.datetime.strftime(thisDate,"%m-%d-%Y")
    print(str.format("On {}, {} costs ${:.2f}",thisDateString,activity,cost))
    costs.append(cost)
print(str.format("The most expensive day cost ${}",max(costs)))
print(str.format("The least expensive day costs ${}",min(costs)))
total=sum(costs)
print(str.format("Your total trip cost is ${}",total))
average=total/delta.days
print(str.format("Your average cost per day is ${}",average))
