import time
hours = int(time.strftime('%H'))

if(hours>3 and hours<12):
    print('Good morning, sir')
elif(hours>=12 and hours<17):
    print('Good afternoon, sir')
elif(hours>=17 and hours<21):
    print('Good evening, sir')
else:
    print('Good night, sir')

