import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
screen.fill('white')


pygame.display.update()


spyschool=pygame.image.load('spyschool.png')
screen.blit(spyschool,(150,50))

theisland=pygame.image.load('theisland.png')
screen.blit(theisland,(150,200))

thetournament=pygame.image.load('thetournament.png')
screen.blit(thetournament,(150,350))

funjungle=pygame.image.load('funjungle.png')
screen.blit(funjungle,(150,500))


pygame.display.update()


font=pygame.font.SysFont('Times New Roman',12)

text1=font.render("Minecraft: The Tournament by DaVaun Sanders",True,(0,0,0))
screen.blit(text1,(350,70))

text2=font.render("Spy School by Stuart Gibbs",True,(0,0,0))
screen.blit(text2,(350,220))

text3=font.render("Belly Up by Stuart Gibbs",True,(0,0,0))
screen.blit(text3,(350,370))

text4=font.render("The Island by Max Brooks",True,(0,0,0))
screen.blit(text4,(350,490))


pygame.display.update()


while True:


    pygame.display.update()


    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,(0,0,0),pos,10,0)

        if event.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            pygame.draw.line(screen,(0,0,0),pos,pos2,5)
            pygame.draw.circle(screen,(0,0,0),pos2,10,0)

        pygame.display.update()