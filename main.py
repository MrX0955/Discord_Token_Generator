try:
    import random as KT
    import os
    import sys
    import time
    from colorama import Fore, init
except Exception:
    print(" ~ [♥] Görünüşe Göre Modülleriniz Eksik. Acaba Hangisi, Söylemem. :)")

init()

chars = "-abcdefghijklmnopq_rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

logo = f"""
{Fore.LIGHTYELLOW_EX}     __  __ _____  __   __ {Fore.LIGHTCYAN_EX}
{Fore.LIGHTYELLOW_EX}    |  \/  |  __ \ \ \ / / {Fore.LIGHTCYAN_EX}
{Fore.LIGHTYELLOW_EX}    | \  / | |__) | \ V /  {Fore.LIGHTCYAN_EX}
{Fore.LIGHTYELLOW_EX}    | |\/| |  _  /   > <   {Fore.LIGHTCYAN_EX}
{Fore.LIGHTYELLOW_EX}    | |  | | | \ \  / . \  {Fore.LIGHTCYAN_EX}
{Fore.LIGHTYELLOW_EX}    |_|  |_|_|  \_\/_/ \_\ {Fore.LIGHTCYAN_EX}
                                                                                 """
print("\n" + logo + "\n")

ilosc = input(" Kaç tane token üreteyim sana cnm [1=3 Token]: ")
ilosc = int(ilosc)
os.system('cls')

print(f"{Fore.LIGHTRED_EX} [-] Programa bir şeyler oluyor...")
time.sleep(2)
print(f" {Fore.LIGHTGREEN_EX} [?] Şaka lan şaka gül diye")

working = '[WORK] '
err = '[ERROR] '

for i in range(ilosc):
    token1 = ""
    token2 = ""
    token3 = ""
    token4 = ""
    token5 = ""
    token6 = ""
    token7 = ""
    token8 = ""
    token9 = ""

    for c in range(89):
        token1 += KT.choice(chars)

    for x in range(23):
        token3 += KT.choice(chars)
    for f in range(5):
        token4 += KT.choice(chars)
    for z in range(28):
        token6 += KT.choice(chars)

    for a in range(24):
        token7 += KT.choice(chars)
    for v in range(6):
        token8 += KT.choice(chars)
    for b in range(27):
        token9 += KT.choice(chars)


    token2 = 'mfa.' + token1 #Mfa token
    token5 = 'OD' + token3 + '.Y' + token4 + '.' + token6 #OD Tek başınadır
    token6= token7 + "." + token8 + "." + token9 #Normal Token

    token1 = str(token1)
    token2 = str(token2)
    token3 = str(token3)
    token4 = str(token4)
    token5 = str(token5)
    token6 = str(token6)
    token7 = str(token7)
    token8 = str(token8)
    token9 = str(token9)



    token = token2
    tokenn = token5
    tokennn = token6

    Tokens = open("Karisik_Tokenler.txt","a+")
    Tokens.writelines("{}\n{}\n{}\n".format(token, tokenn, tokennn))

print("\n")
sys.stdout.write("\033[1;31m")
print('     Y a p ı m c ı ')
print("-->>     [Defacer]MrX ..! <<--")
sys.stdout.write("\033[0;0m")
input("")
