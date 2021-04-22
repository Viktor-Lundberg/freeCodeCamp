def add_time(start, duration, day = None):
    inputstart = start.split(' ')
    inputstarttime = start.split(':')
    weekdayslist = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Tar fram am/pm samt starttimmar och startminuter på input och gör om till int
    ampm = inputstart[1]
    starthour = int(inputstarttime[0])
    startmins = int(inputstarttime[1].strip(' PMAM'))

    # Tar fram hur många timmar och minuter som ska läggas på den ursprungliga tiden och gör om till int
    inputduration = duration.split(':')
    durationhour = int(inputduration[0])
    durationmins = int(inputduration[1])

    # Om startperioden är "PM" läggs 12 timmar på starttimmarna för 24-timmarsklocka
    if ampm == 'PM':
        starthour = starthour + 12


    # Räknar ihop startminuter och minuter som ska läggas på
    resultminits = startmins + durationmins
    # Kollar om det blir en extratimme eller inte och gör om till str och lägger på en 0:a ifall minuter blir under 10.
    extrahour = resultminits // 60
    if extrahour == 1:
        resultminits = resultminits - 60
        resultminits = str(resultminits).zfill(2)
    else:
        resultminits = str(resultminits).zfill(2)


    # Räknar ihop starttimmarna med timmar som ska läggas på samt eventuella extratimmar
    result = starthour + durationhour + extrahour


    # Räknar ut hur många dagar timmarna blir
    days = (result // 24)

    # Om användaren matat in day görs strängen in till lowercase.
    if day != None:
        inputday = day.lower()
        # Räknar ut vilken dag resultatet landar på genom att använda index i weekdaylist + days % 7
        daycalculation = int(weekdayslist.index(inputday)) + days % 7
        # Om daycalculation blir 7 görs den om till 0 för att undvika out off range error och ange "Monday" i output.
        if daycalculation == 7:
            daycalculation = 0
        newday = weekdayslist[daycalculation].capitalize()

    # Tar fram text för dagar om 0 dagar ingen annars (next day) eller (x dagar senare).
    if days == 0:
        days = ""
    elif days == 1:
        days = ' (next day)'
    else:
        days = f' ({days} days later)'

    # Gör om timmarna till en tolvtimmarsklocka igen
    calculation = result % 12

    # Kollar vad den nya timmarna blir på en 24-timmarsklocka
    ampmcalculation = result % 24

    # Kollar om det är AM eller PM baserat på 24 timmarsklockan
    if ampmcalculation >= 12:
        ampm = 'PM'
    else:
        ampm = 'AM'

    # Om nya 12-timmars timmen blir 0 lägger skriptet till 12 för att få rätt format på tiden
    if (calculation == 0):
        calculation = 12

    # Slår ihop resultatet i variabeln new_time om det finns "day" från användaren läggs den till annars inte.
    if day != None:
        new_time = f'{calculation}:{resultminits} {ampm}, {newday}{days}'
    else:
        new_time = f'{calculation}:{resultminits} {ampm}{days}'

    return new_time