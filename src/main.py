import pygame, sys
from constants import WIDTH,HEIGHT,WHITE,SQUARE,BLACK
from game import Game
from minmax.algorithm import minimax
 


mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('JUEGO DAMAS M&M')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

 
font = pygame.font.SysFont("arialblack", 40)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE
    col = x // SQUARE
    return row, col 
 
 
def main_menu():
    run = True
    game = Game(screen)
    
    while run:
 
        screen.fill((0,0,0))
        draw_text('Juego damas', font, (255, 255, 0), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                USUARIOvsIA(game)
        if button_2.collidepoint((mx, my)):
            if click:
                usuarioVSusuario()
        if button_3.collidepoint((mx, my)):
            if click:
                iaVSia()        

        pygame.draw.rect(screen, (192, 192, 192), button_1)
        pygame.draw.rect(screen, (192, 192, 192), button_2)
        pygame.draw.rect(screen, (192, 192, 192), button_3)
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                
                if event.button == 1:
                    click = True
                    
        pygame.display.update()
        
    pygame.quit()



def USUARIOvsIA(game):
   
   running = True
   while running:
       
        
        if game.turn == WHITE:
            value, new_board = minimax(game.getBoard(), 4, WHITE, game)
            game.ai_move(new_board)
            pygame.display.update()

#interfaz para ganador 

        if game.winner() is not None:
             
             winner = game.winner(WHITE)
             print(winner)
             running = False
             return winner

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
            
            if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
        game.update()
        pygame.display.update()
        mainClock.tick(60)
 
def usuarioVSusuario():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Usuario VS Usuario', font, (255, 255, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def iaVSia():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('IA VS IA', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()