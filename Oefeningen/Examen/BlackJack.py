from distutils.command.clean import clean
from MijnSpelers import Spelers
from Kaarten import Decks
import random



blackjack = False;
dealer_beurt = False;
eerste_kaartenverdeling = True;
all_players_played = False;
huidig_speler_id = 0
huidig_speler_kaarten = {};
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
            huidig_speler_kaarten.update(total_registered_players: [])
    tafel_spelers.append(Spelers(total_registered_players, "Dealer", 99, 32000,0))
    start_spel();
            


    
def start_spel():

    print("Spel Begint geef uw/Jullie gok inzet in");
    plaats_inzet();
    
    print("Dit ze spelers en hun inzet");
    bekijk_spelers();
    

def toon_resultaat():
    pass

def bekijk_spelers():
    for speler in tafel_spelers:
        print(f"Name: {speler.naam}, Bet: {speler.inzet}")
        
        
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
    
    gebruikers_keuze = input("1: PASSEN \n2: KOPEN/HIT \n3: SPLITSEN \n4: VERDUBBELEN \n5: OPGEVEN")
    if(is_nummer(gebruikers_keuze) and gebruikers_keuze < "5"):
        if(gebruikers_keuze == "1"):
            #ga naar vvolgende speler of toon kaarten van computer
            pass
        elif(gebruikers_keuze == "2"):
            pass
        elif(gebruikers_keuze == "3"):
            pass
        elif(gebruikers_keuze == "4"):
            pass
        elif(gebruikers_keuze == "5"):
            pass
    else:
        opties();
        
def deel_kaarten():
    #geef elk speler een kaart daarna een kaart aan de computer

            
        #computer received card

def check_balance(speler):
    #check players balance to see if he has enough to play or to bet
    pass

registreer_spelers()