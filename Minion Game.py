# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
        
    vowels = ['A', 'E', 'I', 'O', 'U']
    s, k = 0, 0
    for index, value in enumerate(string):
        score = len(string) - index
        if value in vowels:
            k += score
        else: 
            s += score
            
    if s == k:
        print("Draw")
    elif s > k:
        print(f"Stuart {s}")
    else:
        print(f"Kevin {k}")
  
    
if __name__ == '__main__':
