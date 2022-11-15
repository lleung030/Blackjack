
import random

dealer_lst = []
player_1_lst = []
class Blackjack:
    def __init__(self, name):
        self.name = name
    
    def deal_1st(self):
        print('Dealer\'s first card dealt is:')
        a = random.randint(1,13)
        print(a)
        dealer_lst.append(a)
        
    
    def deal_2nd(self):
        print('Dealer\'s second card dealt is...')
        b = random.randint(1,13)
        dealer_lst.append(b)
        
    
    def hit(self):
        choice = input('Keep going? ')
        if choice == 'yes':
            c = random.randint(1,13)
            player_1_lst.append(c)
            print(f'You were dealt a(n) {c}')
            print(player_1_lst)
        elif choice == 'no':
            print('I stand!')
            print(f'{player_1_lst} so my total is {sum(player_1_lst)}')
        
          
            
class Player_1(Blackjack):
    def __init__(self, name):
        super().__init__(name)
    
    
    def deal(self):
        print('First Card dealt is:')
        a = random.randint(1,13)
        print(a)
        print('Second Card dealt is:')
        b = random.randint(1,13)
        print(b)
        player_1_lst.append(a)
        player_1_lst.append(b)
        print(player_1_lst)
        print(f'So far I have a(n) {a+b}...')
        if a + b > 21:
            print('Bust!')

        elif a + b == 21:
            print('BlackJack!')
            
        elif a + b < 21:
            print('Should I keep playing?')      
    
    
class Dealer(Blackjack):
    def __init__(self, name):
        super().__init__(name)
        
    
    def hit(self):
        a = random.randint(1,13)
        dealer_lst.append(a)
        

black = Blackjack('')

dealer = Dealer('Jack')
player_1 = Player_1('Bob')

def main():
    while True:
        dealer.deal_1st()
        dealer.deal_2nd()
        print('Dealer\'s second card is hidden from view...')
        if sum(dealer_lst) == 21:
            print('BLACKJACK: Dealer wins!')
            print(f'Dealer\'s cards are {dealer_lst}')
            break
        elif sum(dealer_lst) > 21:
            print('Bust: Dealer lost!')
            print(f'{dealer_lst} total: {sum(dealer_lst)}')
            break
        elif sum(dealer_lst)<16 and sum(dealer_lst)>2:
            dealer.hit()
            print('Dealer is delt another card...')
            
            if sum(dealer_lst) == 21:    
                print('21! Dealer wins!')
                print(f'Dealer\'s cards are {dealer_lst}')
                break
            elif sum(dealer_lst) > 21:
                print('Bust: Dealer lost!')
                print(f'{dealer_lst} total: {sum(dealer_lst)}') 
                break
            elif sum(dealer_lst)<16 and sum(dealer_lst)>2:
                dealer.hit()
                print('Dealer is delt another card...')
            
                if sum(dealer_lst) == 21:    
                    print('21! Dealer wins!')
                    print(f'Dealer\'s cards are {dealer_lst}')
                    break
                elif sum(dealer_lst) > 21:
                    print('Bust: Dealer lost!')
                    print(f'{dealer_lst} total: {sum(dealer_lst)}') 
                    break
            
        choice = input("Would you like to play?: ")
        if choice == 'yes':
            player_1.deal()
            player_1.hit()
            if sum(player_1_lst)>21:
                print('Darn a bust!')
                break
            elif sum(player_1_lst)==21:
                print('YES I WIN!')
                break
            if sum(player_1_lst)<21:
                print('Hmm...')
                player_1.hit()
                if sum(player_1_lst)>21:
                    print('Darn a bust!')
                    break
                elif sum(player_1_lst)==21:
                    print('YES I WIN!')
                    break
                if sum(player_1_lst)<21:
                    print('Hmm...')
                    player_1.hit()
                    if sum(player_1_lst)>21:
                        print('Darn a bust!')
                        break
                    elif sum(player_1_lst)==21:
                        print('YES I WIN!')
                        break
                    if sum(player_1_lst)<21:
                        print('Hmm...')
                        print(f'My total is: {sum(player_1_lst)}')
                        
                        if sum(player_1_lst)>sum(dealer_lst): 
                            print(f'Dealer\'s total: {sum(dealer_lst)}')
                            print('I win!')
                        elif sum(player_1_lst)==sum(dealer_lst):
                            print(f'Dealer\'s total: {sum(dealer_lst)}')
                            print('Tie!')
                        elif sum(player_1_lst)<sum(dealer_lst):
                            print(f'Dealer\'s total: {sum(dealer_lst)}')
                            print('I lost...')
                        
            
            break
        elif choice == 'no':
            print('I Quit')
            break
            
main()