import datetime
import pytz


utcTime = datetime.datetime.now(tz=pytz.utc)
print (utcTime)


pacTime = int(utcTime.astimezone(pytz.timezone('US/Pacific')).strftime('%H'))
print ("Pacific Time: ", pacTime)

nycTime = int(utcTime.astimezone(pytz.timezone('US/Eastern')).strftime('%H'))
print ("NYC Time: ", nycTime)

londonTime = int(utcTime.astimezone(pytz.timezone('Europe/London')).strftime('%H'))
print ("London Time: ", londonTime)






if pacTime in range(9, 21): 
    print ("The pacific branch is open!")
else:
    print ("Closed")



if nycTime in range(9, 21): 
    print ("The NYC branch is open!")
else:
    print ("Closed")



if londonTime in range(9, 21): 
    print ("The London branch is open!")
else:
    print ("Closed")



    
    
   




