# Sukurkite terminalo programą, kuri bankui leis apdoroti gaunamas užklausas. Bankas gali gauti trijų tipų užklausas:

# - transfer i j sum: prašymas pervesti pinigų sumą iš i-osios sąskaitos į j-ąją;
# - deposit i sum: prašymas įnešti pinigų sumą į i-ąją sąskaitą;
# - withdraw i sum: prašymas išsiimti pinigų sumą iš i-osios sąskaitos.

# Jūsų programa taip pat turėtų galėti apdoroti netinkamas užklausas. Yra dviejų tipų negaliojančios užklausos:
# - neteisingas sąskaitos numeris prašymuose;
# - didesnės pinigų sumos, nei yra šiuo metu, išėmimas/pervedimas.

# Po kiekvienos operacijos išveskite ar ji pavyko, ar ne ir parodykite sąskaitų balansus ekrane.

######################

# Pvz. Kai duoti pradiniai sąskaitų balansai yra:
# ACCOUNTS = [10, 100, 20, 50, 30]

# Įvestos užklausos į terminalą:
# - "withdraw 2 10"
# - "transfer 5 1 20"
# - "deposit 5 20"
# - "transfer 3 4 15"

# Atitinkamai išvedami rezultatai, po kiekvienos užklausos:
# - Operation was successful; New account balances: [10, 90, 20, 50, 30]
# - Operation was successful; New account balances: [30, 90, 20, 50, 10]
# - Operation was successful; New account balances: [30, 90, 20, 50, 30]
# - Operation was successful; New account balances: [10, 90, 20, 50, 30]
# - Operation was successful; New account balances: [30, 90, 5, 65, 30]

######################

# Pvz. Kai duoti pradiniai sąskaitų balansai yra:
# ACCOUNTS = [20, 1000, 500, 40, 90]

# Įvestos užklausos į terminalą:
# - "deposit 3 400"
# - "transfer 1 10 10"
# - "withdraw 4 50"

# Atitinkamai išvedami rezultatai, po kiekvienos užklausos:
# - Operation was successful; New account balances: [20, 1000, 900, 40, 90]
# - Operation is invalid, such account does not exist; New account balances: [20, 1000, 900, 40, 90]
# - Operation is invalid, not enough balance; New account balances: [20, 1000, 900, 40, 90]

# !!! Pastaba: Papildomas taškas, jeigu panaudosite klases. !!!

ACCOUNTS = [10, 100, 20, 50, 30]

def transfer(account_from, account_to, amount):
    if account_from > len(ACCOUNTS) or account_to > len(ACCOUNTS):
        print("Operation is invalid, such account does not exist; New account balances: ", ACCOUNTS)
    else:
        if amount > ACCOUNTS[account_from - 1]:
            print("Operation is invalid, not enough balance; New account balances: ", ACCOUNTS)
        else:
            ACCOUNTS[account_from - 1] -= amount
            ACCOUNTS[account_to - 1] += amount
            print("Operation was successful; New account balances: ", ACCOUNTS)

def deposit(account, amount):
    if account > len(ACCOUNTS):
        print("Operation is invalid, such account does not exist; New account balances: ", ACCOUNTS)
    else:
        ACCOUNTS[account - 1] += amount
        print("Operation was successful; New account balances: ", ACCOUNTS)
 
def withdraw(account, amount):
    if account > len(ACCOUNTS):
        print("Operation is invalid, such account does not exist; New account balances: ", ACCOUNTS)
    else:
        if amount > ACCOUNTS[account - 1]:
            print("Operation is invalid, not enough balance; New account balances: ", ACCOUNTS)
        else:
            ACCOUNTS[account - 1] -= amount
            print("Operation was successful; New account balances: ", ACCOUNTS)  

transfer(2, 3, 90)
deposit(50, 20)
withdraw(1, 100)
