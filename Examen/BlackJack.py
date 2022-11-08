from distutils.command.clean import clean
from MijnSpelers import Spelers
from Kaarten import Decks
import random



blackjack = False;
dealer_beurt = False;
eerste_kaartenverdeling = True;
all_players_played = False;
huidig_speler_id = 0
dealer_id = 99
huidig_speler_kaarten = {};
totaal_speler_kaarten = {};
kaarten = range(13)
tafel_spelers = []

def is_nummer(nummer):
    try:
        x = int(nummer);
        return True;
    except:
        return False;
    
def registreer_spelers():
    players = input("Hoeveel spelers aan tafel ?")
    #bots = input("Hoeveel bots wil je aan tafel ?")
    total_registered_players = 0
    if(is_nummer(players)):     
        while total_registered_players != int(players):
            print("please register by putting your Name, Age, TotalAmount");
            id = total_registered_players;
            name = input("Naam: ")
            age = input("Leeftijd: ")
            bet = 50
            total_registered_players += 1;
            tafel_spelers.append(Spelers(id, name, age, 50, 0))
            huidig_speler_kaarten.update({id: []})
    tafel_spelers.append(Spelers(99, "Dealer", 99, 32000,0))
    huidig_speler_kaarten.update({99: []})
    start_spel();
            


    
def start_spel():

    print("Spel Begint geef uw/Jullie gok inzet in");
    plaats_inzet();
    
    deel_kaarten()
    print("Dit ze spelers en hun inzet");
    bekijk_spelers();
    for speler in tafel_spelers:
        huidig_speler_id = speler.id;
        opties();
    toon_resultaat();
    

def toon_resultaat():
    totaal_computer_kaarten = sum(huidig_speler_kaarten[99])
    print(f"Dealer heeft: totaal_computer_kaarten");
    
    for speler in tafel_spelers:
        if(speler.naam == "Dealer"):
            return;
        totaal_speler_kaarten = sum(huidig_speler_kaarten[speler.id])
        if (totaal_speler_kaarten == 21):
            tafel_spelers[huidig_speler_id].inzet = int(tafel_spelers[huidig_speler_id].bet) * 2.5
            tafel_spelers[huidig_speler_id].bet = 0
            print(f"{speler.naam} you won 1.5 from your bet you now have {tafel_spelers[huidig_speler_id].inzet}")
        elif(totaal_speler_kaarten < 21 and totaal_speler_kaarten > totaal_computer_kaarten):
            tafel_spelers[huidig_speler_id].inzet = int(tafel_spelers[huidig_speler_id].bet) * 2
            tafel_spelers[huidig_speler_id].bet = 0
            print(f"{speler.naam} you won 1 times from your bet you now have {tafel_spelers[huidig_speler_id].inzet}")
        else:

            print(f"{speler.naam} you lost ! Dealer won")
            tafel_spelers[huidig_speler_id].bet = 0
    bekijk_spelers();
            
            

        


def bekijk_spelers():
    for speler in tafel_spelers:
        print(f"Name: {speler.naam}, Bet: {speler.inzet}")
        print(huidig_speler_kaarten[speler.id])
        
def plaats_inzet():
    player_id = 0;
    while player_id != len(tafel_spelers) - 1:
        bet = input(f"your total balance is {tafel_spelers[player_id].inzet} hoeveel wil je inzetten")
        if(is_nummer(bet) == False or int(bet) > tafel_spelers[player_id].inzet):
            print("dit is niet mogelijk uw inzet is groter dan uw vermogen");
        else:
            tafel_spelers[player_id].bet = bet;
            tafel_spelers[player_id].inzet = int(bet) - tafel_spelers[player_id].inzet;
            player_id += 1;
            
def opties():
    print(f"Speler: {tafel_spelers[huidig_speler_id].naam}, {huidig_speler_kaarten[huidig_speler_id]}\nkies uit een volgende opties: ");
    gebruikers_keuze = input("1: PASSEN \n2: KOPEN/HIT \n3: SPLITSEN \n4: VERDUBBELEN \n5: OPGEVEN\n")
    kaart = random.randint(1,13);
    if(is_nummer(gebruikers_keuze) and gebruikers_keuze <= "5"):
        if(gebruikers_keuze == "1"):
            #ga naar vvolgende speler of toon kaarten van computer
            pass
        elif(gebruikers_keuze == "2"):
            huidig_speler_kaarten[huidig_speler_id].append(kaart)
            opties();
        elif(gebruikers_keuze == "3"):
            
            pass
        elif(gebruikers_keuze == "4"):
            #check_balance()
            if(int(tafel_spelers[huidig_speler_id].inzet) >= int(tafel_spelers[huidig_speler_id].bet)):
                huidig_speler_kaarten[huidig_speler_id].append(kaart)
            else:
                print("you don't have enough balance to double please pass\ buy or exit");
                opties();
        elif(gebruikers_keuze == "5"):
            tafel_spelers[huidig_speler_id].bet = 0
        
    else:
        opties();
        
def deel_kaarten():
    #geef elk speler een kaart daarna een kaart aan de computer
  
    for x in range(2):
        for speler in tafel_spelers:
            kaart = random.randint(1, len(kaarten))
            huidig_speler_kaarten[speler.id].append(kaart)

registreer_spelers()