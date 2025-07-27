import random 

my_choice = {
    'r': 'rock', 
    'p': 'paper', 
    's': 'scissor'
}

player1_score = 0
computer_score = 0
player1_name = input("enter your name: ")

while True: 
    player1 = input("enter the choice(r: rock/p: paper/s: scissor) or Q to quit: ").strip().lower()
    if(player1 == 'q'):
        if(player1_score == computer_score):
            print('this battle ends up in a tie!')
        
        elif(player1_score > computer_score):
            print(f'{player1_name} wins this battle!')
        
        else:
            print('computer wins this battle!')

        break
    
    elif(player1 not in my_choice):
        print('Invalid choice! Try again...\n' )
        continue
    
    computer = random.choice(list(my_choice.keys()))
    print(f"\n{player1_name}: {my_choice[player1]}")
    print(f"computer: {my_choice[computer]}")
    
    if(player1 == computer):
        print("it's a tie guys! Try again...\n")
        
    elif(player1 == 'r' and computer == 's') or (player1 == 's' and computer == 'p') or (player1 == 'p' and computer == 'r'):
        print(f'{player1_name} wins!\n')
        player1_score +=1
        

    else:
        print('computer wins!\n')
        computer_score +=1
    
    print(f"Score -> {player1_name}: {player1_score} | Computer: {computer_score}\n")
