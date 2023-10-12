# import pygame
# x=640
# y=310
# x2 = 300
# y2 = 310
# gravidade=0

# class Corpo:
#     def __init__(self,massa,surface,color,position,raio,largura) -> None:
#         self.massa=massa
#         self.surface=surface
#         self.color=color
#         self.position=position
#         self.raio=raio 
#         self.larfura=largura
#     def desenhar(self,surface,color,position,raio,largura):
#         pygame.draw.circle(surface,color,position,raio,largura)


# def gravidade(m1,m2,d):
#     gravidade=(m1*m2)/d
#     return gravidade


    
    
# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# running = True

# while running:
     
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     planeta1=Corpo (massa=10,surface=screen,color=(0, 255, 0), 
#                    position=[x,y],raio= 170,largura= 0)
    
#     planeta2=Corpo(massa=10,surface=screen,color=(0, 0, 255), 
#                    position=[x,y],raio= 170,largura= 0)
#     d=x-x2
#     g=(planeta1.massa*planeta2.massa)/d
#     gravidade=d - g
#     screen.fill("black")
    
   
    

    
#     planeta1.desenhar(screen,(0, 255, 0), 
#                    [x , y], 70, 0)
    
#     planeta2.desenhar(screen,(0, 0, 255), 
#                    [x2, y2], 70, 0)
    

#     pygame.display.update()
    
    
    
    
# pygame.quit()

import pygame

def gravidade(m1,m2,d):
    gravidade=(m1*m2)/d
    return gravidade

class Corpo:
    def __init__(self,massa,surface,color,position,raio,largura) -> None:
        self.massa=massa
        self.surface=surface
        self.color=color
        self.position=position
        self.raio=raio 
        self.larfura=largura
    def desenhar(self,surface,color,position,raio,largura):
        pygame.draw.circle(surface,color,position,raio,largura)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

# Create planet objects
planeta1 = Corpo(massa=10,surface=screen,color=(0, 255, 0), 
                  position=[640, 310],raio=170,largura=0)
planeta2 = Corpo(massa=10,surface=screen,color=(0, 0, 255), 
                  position=[300, 310],raio=170,largura=0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    d = abs(planeta1.position[0] - planeta2.position[0])
    g = gravidade(planeta1.massa, planeta2.massa, d)

   
    if planeta1.position[0] < planeta2.position[0]:
        planeta1.position[0] += g / planeta1.massa
        planeta2.position[0] -= g / planeta2.massa
    else:
        planeta1.position[0] -= g / planeta1.massa
        planeta2.position[0] += g / planeta2.massa

    
    screen.fill("black")
    planeta1.desenhar(screen,(0, 255, 0), 
                   planeta1.position, 70, 0)
    planeta2.desenhar(screen,(0, 0, 255), 
                   planeta2.position, 70, 0)

    pygame.display.update()

pygame.quit()

