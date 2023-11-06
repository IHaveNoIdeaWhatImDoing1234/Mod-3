currentTime = int(input("Please enter the current time(24 hour clock): ")) #Get current time from user
alarmSetHours = int(input("Please enter in how many hours you would like your alamr to go off: ")) #get number of hours from user until alarm goes off
alarmGoesOff = currentTime+(alarmSetHours % 24) #Mod the previously inputted number by 24 to determine the number of hours that need to be added to the current time for the alarm to be accurate
if (alarmGoesOff < 24):
    print("The alarm will go off at:" ,alarmGoesOff, "Hours") #if the calulated number is less than 24, print the value
else:
    print("The alarm will of off at:" ,alarmGoesOff - 24, "Hours") #if the calulated number is greater or equal to 24, subtract 24, then print teh value
