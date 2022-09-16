import random
import time

#zapisuje date i czas gry
mydate = time.asctime()


#poczatek gry


def beginning(): #todo: program niech sprawdzi czy liczba< 100 i niech sprawdzi czy liczba nie jest zmiennoprzecinkowa #wszystko skonczone

    print("Wylosuje dla Ciebie 3 liczby od 1 do 100, sprobuj je zgadnac. (przyklad: 23,36,87)")

    myinput = input("Tutaj wpisz liczby po przecinku. > \n")
    guess = myinput.split(',')

    finallist = []
    try:
        for liczba in guess:
            finallist.append(int(liczba))

    except ValueError:
        return 0

    finallist.sort()
    if max(finallist)>100 or min(finallist)<0 or len(finallist)>3:
        return 0
    return finallist

def randomnumber():
    randomnumbs = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    randomnumbs.sort()
    return randomnumbs


#finalne zapisanie wynikow w liste
myguesses = beginning()
            
#komputer losuje liczby
randomguesses = randomnumber()

#sprawdzam czy moje liczby sa podobne do liczb komputera
if myguesses!= 0:
    print(f'Twoje liczby to {myguesses[0]}, {myguesses[1]}, i {myguesses[2]}')
    print(f'Liczby ktore wylosowalem to {randomguesses[0]}, {randomguesses[1]}, i {randomguesses[2]}')
    if myguesses==randomguesses:
        print("Udalo ci sie zgadnac wszystkie liczby! Gratulacje!")
    else:
        print("Niestety dzisiaj cie pokonalem :/ .")

    #zapisuje wyniki gry do pliku (data i godzina rozpoczecia gry, moje liczby, liczby komputera i aktualny wynik bedzie u samej gory)

    """
    ################################
    Data: 16 09 2022 Godzina: 10:49
    Moje liczby: 12, 23, i 65
    Liczby komputera: 70, 96, i 97
    ################################

    ################################
    Data: 16 09 2022 Godzina: 10:49
    Moje liczby: 12, 23, i 65
    Liczby komputera: 70, 96, i 97
    ################################

    ################################
    Data: 16 09 2022 Godzina: 10:49
    Moje liczby: 12, 23, i 65
    Liczby komputera: 70, 96, i 97
    ################################

    """ #Tak to bedzie wygladalo

    myfile = open("history.txt", "a")
    myfile.write("\n################################\n")
    myfile.write("Data i godzina:" + mydate+ "\n")
    myfile.write("Moje liczby: " + repr(myguesses)+ "\n")
    myfile.write("Liczby komputera: " + repr(randomguesses)+ "\n")
    myfile.write("################################\n\n")
    myfile.close()
else:
    print("Wpisz trzy liczby calkowite,po przecinku i bez spacji.")
    print("Liczby dodatkowo musza miescic sie w przedziale od 1 do 100.")


        



