import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
screen.fill('white')


pygame.display.update()


subwaysurfer=pygame.image.load('subwaysurfers.png')
screen.blit(subwaysurfer,(150,50))

templerun=pygame.image.load('templerun.png')
screen.blit(templerun,(150,200))

ludo=pygame.image.load('ludo.png')
screen.blit(ludo,(150,350))

candycrush=pygame.image.load('candycrush.jpg')
screen.blit(candycrush,(150,500))


font=pygame.font.SysFont('Times New Roman',36)

text1=font.render("Ludo",True,(0,0,0))
screen.blit(text1,(350,70))

text2=font.render("Subway Surfers",True,(0,0,0))
screen.blit(text2,(350,220))

text3=font.render("Candy Crush",True,(0,0,0))
screen.blit(text3,(350,370))

text4=font.render("Temple Run",True,(0,0,0))
screen.blit(text4,(350,490))


while True:

    pygame.display.update()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,(0,0,0),pos,10,0)

            pygame.display.update()

        if event.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            pygame.draw.line(screen,(0,0,0),pos,pos2,5)
            pygame.draw.circle(screen,(0,0,0),pos2,10,0)

            pygame.display.update()