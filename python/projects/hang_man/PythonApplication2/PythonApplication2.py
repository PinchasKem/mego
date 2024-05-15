#  pygame נסיון עבודה עם 

#  import pygame



# window_width = 700
# window_height = 500

# pygame.init()
# size = (window_width , window_height)
# screen = pygame.display.get_mode(size)
# pygame.display.get_caption("game")

# pygame.quit()



print("welcome to the game hang man")

word= list(input("pleas enter a word :"))
discovery = ["_"]*len(word)

len1= len(word)
i=0
while(i < 7):
    letter= input("pleas enter a letter :")
    b=0
    for u in range(len(word)):        
        if(letter == word[u]):            
            b+=1
            word[u]=0
            len1-=1
            discovery[u] = letter
    print(discovery)              
    if(len1==0):
        print("you win !") 
        break
    if(b==0):
        i+=1
if(i==7):
    print("you lose !")

