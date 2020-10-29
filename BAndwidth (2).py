import csv

departureDict = {}
name = []
Arrival = []
#Getting data from a CSV file
with open('Names.csv', 'r') as csvfile:
    Reader = csv.reader(csvfile, delimiter=',')
    global c
    for row in Reader:
        name.append(row[0])
        Arrival.append(int (row[1]))
        departureDict.update ({int(row[1]): row[0]})


departure = []
time = 0
def Movement():
    global time
    print(Arrival)
    print(departure)
    #Sending the fastest two   ----x---y--->
    Arrival.sort()
    departure.append(Arrival[0])
    print(departureDict[Arrival[0]],'Crossed')
    Arrival.pop(0)
    departure.append(Arrival[0])
    print('and',departureDict[Arrival[0]],'Crossed')
    time += Arrival[0]
    Arrival.pop(0)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Arrival',Arrival)
    print('departure',departure)
    print(time)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    #Sending back the one of the two fastest   <----x---
    Arrival.append(departure[0])
    print(departureDict[departure[0]],'went back')
    time += departure[0]
    Arrival.sort()
    departure.pop(0)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Arrival',Arrival)
    print('departure',departure)
    print(time)

    #sending the slowest two --x----y--->
    Arrival.sort()
    Arrival.reverse()
    departure.append(Arrival[0])
    print(departureDict[Arrival[0]],'Crossed')
    time += Arrival[0]
    Arrival.pop(0)
    departure.append(Arrival[0])
    print('and',departureDict[Arrival[0]],'Crossed')
    Arrival.pop(0)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Arrival',Arrival)
    print('departure',departure)
    print(time)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    #sending back the fastest one  <----x---
    Arrival.append(departure[0])
    print(departureDict[departure[0]],'went back')
    time += departure[0]
    Arrival.sort()
    departure.pop(0)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Arrival',Arrival)
    print('departure',departure)
    print(time)

    #sending the fastest two  ----x---y--->
    Arrival.sort()
    departure.append(Arrival[0])
    print(departureDict[Arrival[0]],'Crossed')
    Arrival.pop(0)
    Arrival.sort()
    departure.append(Arrival[0])
    print('and',departureDict[Arrival[0]],'Crossed')
    time += Arrival[0]
    Arrival.pop(0)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Arrival',Arrival)
    print('departure',departure)
    print('Total time:',time)
    
C = True
while C == True:
    try:
        #checking for error trapping
        if len(Arrival) != 4:
            raise ValueError('There is an error, you are meant to have only 4 records in the csv file. Reconfigure your CSV file')
        while (len(Arrival))>2:
            Answer = input('Would you like to run the program? (y = Yes, n = No)').lower()
            if Answer not in ('y','n'):
                raise ValueError('Correct input is (y or n)')
            if Answer == 'y':
                Movement()
            else:
                print('Thank you for using')
                C = False
            C = False
    except ValueError as err:
        print(err)





