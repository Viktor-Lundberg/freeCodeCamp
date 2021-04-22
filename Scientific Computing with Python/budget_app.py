class Category:

    def __init__(self, name):
        self.ledger = []
        self.category = name
        self.balance = 0

    # Funktion för att återge objektet vid print
    def __str__(self):
        # Skapar rubrikrad på 30 tecken och centrerar rubriken. Sätter * på vardera sida av kategorinamnet
        rubrik = self.category.center(30,'*')
        linelist = []
        total = 0
        # loopar igenom dictsen i self.ledger för objektet
        for dicts in self.ledger:
            # Hämtar description och förkortar dessa till max 23 tecken
            description = dicts.get("description")
            limiteddescription = '{:.23s}'.format(description)
            # Hämtar amounts och gör om dessa till värden med två decimaler
            amount = dicts.get("amount")
            amountfloat = '{0:.2f}'.format(amount)
            # Räknar ut totalen genom att hela tiden lägga till varje amountvärde i variablen total
            total = total + float(amountfloat)
            # Sätter maxantal på amount till 7 siffror vid print
            amountfloat2 = '{:.7s}'.format(amountfloat)
            # Räknar ut whitespace för varje rad genom att ta längden på description - längden på amountvärdet
            whitespace = len(limiteddescription) + len(amountfloat2)
            whitespace = 30 - whitespace
            # Lägger till varje rad med rätt whitespace och teckenlängd till listan linelist
            line = limiteddescription + ' ' * whitespace + amountfloat2
            linelist.append(line)
        # Returnerar raden
        return rubrik + '\n' + '\n'.join(linelist) + '\n' + 'Total: ' + str(total)

    def deposit(self, amount, description=None):
        if description == None:
            description = ''
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=None):
        if description == None:
            description = ''
        if self.check_funds(amount) == False:
            return False
        self.balance = self.balance - amount
        negativeamount = 0 - amount
        self.ledger.append({"amount": negativeamount, "description": description})
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, anothercategory):
        if self.withdraw(amount, "Transfer to " + anothercategory.category):
            anothercategory.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False


    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True


def create_spend_chart(categories):
    # Skapar rubriken för diagramet samt variabel för summan av whitdrawals i alla kategorier samt en lista att lägga prcentvärdena i
    header = 'Percentage spent by category'
    totalforcategorys = 0
    percentlist = []
    # FEL PROCENTEN SKA RÄKNAS ALLA UTGIFTER I ALLA KATEGORIER / UTGIFTEN I KATEGIORIEN

    # Loopar igenom kategoriernas ledger och fångar upp alla negativa värden (whitrawals) och gör till positiva och lägger till totalforcategorys
    for category in categories:
        for item in category.ledger:
            amount = item.get('amount')
            if amount < 0:
                totalforcategorys = totalforcategorys + abs(amount)

    # Loopar igenom kategoriernas ledger igen för att skapa en variabel med den enskilda kategoriens whitrawals
    for category in categories:
        categoryspend = 0
        for item in category.ledger:
            amount = item.get('amount')
            if amount < 0:
                categoryspend = categoryspend + abs(amount)
        # Räknar ut procenten av kategorins whitrawals i förhållande till alla uttag och lägger till procentlistan
        percent = categoryspend / totalforcategorys * 100
        percentlist.append(percent)
    # Börjar skapa diagramet genom att skapa en tom sträng och en variabel att iterera mot
    table = ''
    axisnumber = 100

    # Skapar Y-axeln och sätter ut procentvärden
    while axisnumber >= 0:
        if axisnumber == 100:
            table = f'{axisnumber}| '
        elif axisnumber >= 10:
            table = table + f' {axisnumber}| '
        else:
            table = table + f'  {axisnumber}| '
        # Jämför värdena i procentlistan mot axisnumret varje tiotal om värdet är större eller lika med skrivs 'o  ' annars '  '
        for value in percentlist:
            if value >= axisnumber:
                table = table +'o  '
            else:
                table = table +'   '
        axisnumber = axisnumber - 10
        # fyller hela tiden på table med nya strängar genom itereringen
        table = table + '\n'
    # Kontrollerar hur lång X-axeln ska vara genom att kontrollera hur många kategorier som finns
    underlinelength = len(categories)
    # Skapar sträng för x -axeln
    underline = '    '+'---'* underlinelength + '-'

    # Skapar en tom lista och en variabel för att mäta längden på kategorierna
    categorylist = []
    categorylen = 0

    # Loopar igenom kategorierna
    for cn in categories:
        # Lägger namnet på kategorien i en variabel
        lettername = cn.category
        # Kontrollerar om kategorinamnet är längre än categorylen om så är fallet blir längden på kategorinamnet nya categorylen
        if len(lettername) > categorylen:
            categorylen = len(lettername)
        # Skapar lista för att lägga till varje bokstav i kategorinamnet i.
        letterlist = []
        # Lägger till varje bokstav i kategorinamnet i listan letterlist för att slutligen lägga till letterlist som en lista i categorylist
        for letter in lettername:
            letterlist.append(letter)
        categorylist.append(letterlist)

    # Kontrollerar om en lista i categorylist är kortare än den längsta listan i listan. Om så är fallet lägger loopen till så många ' ' så att listan blir lika lång som den längsta
    for l in categorylist:
        if len(l) != categorylen:
            for x in range(categorylen - len(l)):
                l.append(' ')

    # Skapar en tom sträng för kategorierna och använder zip för att printa listorna vertikalt och lägga till nödvändig spacing och tar bort den sista '\n'
    categoryrow =''
    for x, y , z in zip(*categorylist):
        categoryrow = categoryrow +'     ' + x + " "*2 + y +" "*2 + z + " " *2 + '\n'
    categoryrow = categoryrow[:-1]

    # Returnerar de olika delarna i en sträng
    return header + '\n' + table + underline + '\n' + categoryrow



