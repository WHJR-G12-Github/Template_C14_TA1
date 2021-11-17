# Importing neat library
import pygame,random,neat
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
images["invertedpipe"]=pygame.transform.flip(images["pipe"], False, True)

speed=0
# Create a variable 'gen' and initialize it to 0

class Bird:
    bird=pygame.Rect(100,250,30,30)
    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
    def moveup(self):
        global speed
        speed-=10
    def display(self):
        screen.blit(images["bird"],self.bird)

class Pipe:
    def __init__(self,x):
        self.height=random.randint(150,400)
        self.tpipe=pygame.Rect(x,self.height-400,40,300)
        self.bpipe=pygame.Rect(x,self.height+150,40,300)
    def display(self):
      screen.blit(images["pipe"],self.bpipe)
      screen.blit(images["invertedpipe"],self.tpipe)
    def move(self):
        self.tpipe.x-=4
        self.bpipe.x-=4
        if self.tpipe.x<-40:
            self.tpipe.x=450
            self.bpipe.x=450
            self.height=random.randint(150,400)
            self.tpipe.y=self.height-400
            self.bpipe.y=self.height+150
            
# Define a function 'eval_fitness()' and passing 'generation' and 'config' as parameters

    # Create a variable 'birdcount' and assigning 1 to it
    
    # Declare 'gen' as global
    
    # Increment 'gen'
   
    # Creating a font of style 'freesansbold.ttf' and size 20 and naming it 'font1'
    font1=pygame.font.Font('freesansbold.ttf', 20) 
    # Create a "for" loop to execute the game code for every 'genome' in the 'generation'
    
        # Entire game code is moved inside the for loop in the function
        bird1=Bird()
        pipe1=Pipe(250)
        bird1.bird.y=200
        groundx=0
        state="play"
        while True:  
          screen.blit(images["bg"],[0,0])
          for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and state=="play":
                    bird1.moveup()  
          pipe1.display()          
          bird1.display()
          bird1.movedown()          
          
          if state=="play":
              groundx-=5
              if groundx<-450:
               groundx=0
              pipe1.move() 
                        
          screen.blit(images["ground"],[groundx,550])
          # Creating text to be displayed and naming it 'text'
          text=font1.render("Gen:"+str(gen)+" Genome:"+str(birdcount),True,(0,0,255)) 
          # Display the 'text' on the screen at [10,10]
          
          if bird1.bird.colliderect(pipe1.bpipe) or bird1.bird.colliderect(pipe1.tpipe) or bird1.bird.y>600 or bird1.bird.y<0:
              state="over"
              
         
          pygame.display.update()
          
          pygame.time.Clock().tick(30)
# Loading the 'config-feedforward.txt' file and naming it 'config'
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,'config-feedforward.txt')  
# Create initial population abd passing 'config' as an argument

# Run the 'eval_fitness()' function for the population created
