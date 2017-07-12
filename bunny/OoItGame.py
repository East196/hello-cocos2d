# coding=utf-8

# 1 - Import library
import pygame
import math
import random

class Hero:
    def __init__(self,game):
        self.game=game
        self.screen = game.screen
        self.player = pygame.image.load("resources/images/dude.png")
        self.playerpos=[100,100]
        self.keys =[False, False, False, False]
        self.acc=[0,0]
        self.arrow = pygame.image.load("resources/images/bullet.png")
        self.arrows=[]
        
    def draw(self):
        self.keys[0]=self.keys[0] if self.playerpos[1]>0 else False
        self.keys[1]=self.keys[1] if self.playerpos[0]>0 else False
        self.keys[2]=self.keys[2] if self.playerpos[1]<self.game.height else False
        self.keys[3]=self.keys[3] if self.playerpos[0]<self.game.width else False
        # 9 - Move player
        if self.keys[0]:
            self.playerpos[1]-=5
        elif self.keys[2]:
            self.playerpos[1]+=5
        if self.keys[1]:
            self.playerpos[0]-=5
        elif self.keys[3]:
            self.playerpos[0]+=5
            
        if self.acc[1]!=0:
            self.accuracy=self.acc[0]*1.0/self.acc[1]*100
        else:
            self.accuracy=0
        # 6.1 - Set player position and rotation
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1]-(self.playerpos[1]+32),position[0]-(self.playerpos[0]+26))
        playerrot = pygame.transform.rotate(self.player, 360-angle*57.29)
        self.playerpos1 = (self.playerpos[0]-playerrot.get_rect().width/2, self.playerpos[1]-playerrot.get_rect().height/2)
        self.screen.blit(playerrot, self.playerpos1)
        # 6.2 - Draw arrows
        for bullet in self.arrows:
            index=0
            velx=math.cos(bullet[0])*10
            vely=math.sin(bullet[0])*10
            bullet[1]+=velx
            bullet[2]+=vely
            if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
                self.arrows.pop(index)
            index+=1
            for projectile in self.arrows:
                arrow1 = pygame.transform.rotate(self.arrow, 360-projectile[0]*57.29)
                self.screen.blit(arrow1, (projectile[1], projectile[2]))
        
        
    def action(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                self.keys[0]=True
            elif event.key==pygame.K_a:
                self.keys[1]=True
            elif event.key==pygame.K_s:
                self.keys[2]=True
            elif event.key==pygame.K_d:
                self.keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                self.keys[0]=False
            elif event.key==pygame.K_a:
                self.keys[1]=False
            elif event.key==pygame.K_s:
                self.keys[2]=False
            elif event.key==pygame.K_d:
                self.keys[3]=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            self.acc[1]+=1
            self.arrows.append([math.atan2(position[1]-(self.playerpos1[1]+32),position[0]-(self.playerpos1[0]+26)),self.playerpos1[0]+12,self.playerpos1[1]+52])            
            self.arrows.append([math.atan2(position[1]-(self.playerpos1[1]+32),position[0]-(self.playerpos1[0]+26)),self.playerpos1[0]+32,self.playerpos1[1]+32])             
            self.arrows.append([math.atan2(position[1]-(self.playerpos1[1]+32),position[0]-(self.playerpos1[0]+26)),self.playerpos1[0]+52,self.playerpos1[1]+12]) 
            if  len(self.game.badguy.badguys):
                target=self.game.badguy.badguys[0]
                self.arrows.append([math.atan2(target[1]-(self.playerpos1[1]+32),target[0]-(self.playerpos1[0]+26))-0.1,self.playerpos1[0]+32,self.playerpos1[1]+32])             
                self.arrows.append([math.atan2(target[1]-(self.playerpos1[1]+32),target[0]-(self.playerpos1[0]+26))-0.2,self.playerpos1[0]+32,self.playerpos1[1]+32])             
                self.arrows.append([math.atan2(target[1]-(self.playerpos1[1]+32),target[0]-(self.playerpos1[0]+26))-0.3,self.playerpos1[0]+32,self.playerpos1[1]+32])             
                       

class BadGuy:
    def __init__(self,game):
        self.game=game
        self.screen = game.screen
        self.badguyimg = pygame.image.load("resources/images/badguy.png")
        self.badtimer=100
        self.badtimer1=0
        self.badguys=[[640,100]]        
    def draw(self):
        self.badtimer-=1
        # 6.3 - Draw badgers
        if self.badtimer==0:
            self.badguys.append([640, random.randint(50,430)])
            self.badtimer=100-(self.badtimer1*2)
            if self.badtimer1>=35:
                self.badtimer1=35
            else:
                self.badtimer1+=5
        index=0 
        for badguy in self.badguys:
            if badguy[0]<-64:
                self.badguys.pop(index)
            badguy[0]-=7
            # 6.3.1 - Attack castle
            badrect=pygame.Rect(self.badguyimg.get_rect())
            badrect.top=badguy[1]
            badrect.left=badguy[0]
            if badrect.left<64:
                self.game.health.healthDown()
                self.badguys.pop(index)
            #6.3.2 - Check for collisions
            index1=0
            for bullet in self.game.hero.arrows:
                bullrect=pygame.Rect(self.game.hero.arrow.get_rect())
                bullrect.left=bullet[1]
                bullrect.top=bullet[2]
                if badrect.colliderect(bullrect):
                    self.game.hero.acc[0]+=1
                    self.game.hero.arrows.pop(index1)
                    if len(self.badguys):
                        self.badguys.pop(index)
                index1+=1
            # 6.3.3 - Next bad guy
            index+=1
        for badguy in self.badguys:
            self.screen.blit(self.badguyimg, badguy)

class Bg():
    def __init__(self,screen,width, height):
        self.screen = screen
        self.width=width
        self.height=height
        self.grass =pygame.image.load("resources/images/grass.png")
        self.castle =pygame.image.load("resources/images/castle.png")
    def draw(self):
        # 6 - draw the screen elements
        for x in range(self.width/self.grass.get_width()+1):
            for y in range(self.height/self.grass.get_height()+1):
                self.screen.blit(self.grass,(x*100,y*100))
        self.screen.blit(self.castle,(0,30))
        self.screen.blit(self.castle,(0,135))
        self.screen.blit(self.castle,(0,240))
        self.screen.blit(self.castle,(0,345))
        
class Lose():
    def __init__(self,screen):
        self.screen = screen
        self.gameover = pygame.image.load("resources/images/gameover.png")
    def display(self,accuracy):
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = self.screen.get_rect().centerx
        textRect.centery = self.screen.get_rect().centery+24
        self.screen.blit(self.gameover, (0,0))
        self.screen.blit(text, textRect)      
        
class Win():
    def __init__(self,screen):
        self.screen = screen
        self.youwin = pygame.image.load("resources/images/youwin.png")
    def display(self,accuracy):
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
        textRect = text.get_rect()
        textRect.centerx = self.screen.get_rect().centerx
        textRect.centery = self.screen.get_rect().centery+24
        self.screen.blit(self.youwin, (0,0))
        self.screen.blit(text, textRect)
        
class Health():
    def __init__(self,screen):
        self.screen = screen
        self.healthbar = pygame.image.load("resources/images/healthbar.png")
        self.health = pygame.image.load("resources/images/health.png")
        self.healthvalue=194
    def display(self):
        self.screen.blit(self.healthbar, (5,5))
        for health1 in range(self.healthvalue):
            self.screen.blit(self.health, (health1+8,8))
    def healthDown(self):
        self.healthvalue -= random.randint(5,20)
    def isDie(self):
        return self.healthvalue<=0
    
class Clock():
    def __init__(self,screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 24)
    def display(self):
        survivedtext = self.font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
        textRect = survivedtext.get_rect()
        textRect.topright=[635,5]
        self.screen.blit(survivedtext, textRect)
        
        
class OoItGame:
    def __init__(self):
        # 2 - Initialize the game
        pygame.init()
        self.width, self.height = 640, 480
        self.screen=pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Rabbit")
        
        # 3 - Initialize the sprites
        self.bg=Bg(self.screen,self.width, self.height)
        self.hero = Hero(self)
        self.badguy=BadGuy(self)
        self.health = Health(self.screen)
        self.clock = Clock(self.screen)
        self.win=Win(self.screen)
        self.lose=Lose(self.screen)
        
    def start(self):
        # 4 - keep looping through
        self.running = 1
        self.exitcode = 0
        while self.running:
            self.draw()
        self.wait()
        
    def draw(self):
        # 5 - clear the screen before drawing it again
        self.screen.fill(0)
        
        self.bg.draw()
        self.hero.draw()
        self.badguy.draw()
        self.clock.display()
        self.health.display()
        
        pygame.display.flip()
        
        # 8 - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type==pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)
            self.hero.action(event)
        
        #10 - Win/Lose check
        if pygame.time.get_ticks()>=90000:
            self.running=0
            self.exitcode=1
        if self.health.isDie():
            self.running=0
            self.exitcode=0
        
    def wait(self):
        # 11 - Win/lose display       
        if self.exitcode==0:
            self.lose.display(self.hero.accuracy)
        else:
            self.win.display(self.hero.accuracy)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.flip()
        
if __name__ == "__main__":
    ooItGame=OoItGame()
    ooItGame.start()
  



