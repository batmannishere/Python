import datetime

date= datetime.date(2006,10,20) # year,month,day
today=datetime.date.today()
time= datetime.time(12,30,3)  #hrs,min,sec
timenow=datetime.datetime.now()
timenow=timenow.strftime("%HHour: %M :%S %d-%m-%Y")
print(timenow)