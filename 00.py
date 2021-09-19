import pygame, sys

def ball_ani():
    global speedx, speedy
    ball.x += speedx
    ball.y += speedy

    if ball.top <= 0 or ball.bottom >= h:
        speedy *= -1
    if ball.left <= 0 or ball.right >= w:
        speedx *= -1
    
    if ball.colliderect(player) or ball.colliderect(player2):
        speedx *= -1

def player_ani():
    player.y += pspeed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= h:
        player.bottom = h


pygame.init()
clock = pygame.time.Clock()

w, h = 1000, 500

pygame.display.set_caption('Fut Pong')
win = pygame.display.set_mode((w, h))
win.fill("black")


ball = pygame.Rect(w//2 - 10, h//2 - 10, 20, 20)
player = pygame.Rect(w - 13, h//2 - 50, 10, 100)
player2 = pygame.Rect(2, h//2 - 50, 10, 100)

speedx, speedy = 7, 7
pspeed = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pspeed +=7
            if event.key == pygame.K_UP:
                pspeed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pspeed -=7
            if event.key == pygame.K_UP:
                pspeed +=7

    ball_ani()
    player_ani()

    win.fill("black")
    pygame.draw.ellipse(win, "green", ball, 8)
    pygame.draw.aaline(win, "white", (w//2, 0), (w//2, h))  
    pygame.draw.rect(win, "white", player)
    pygame.draw.rect(win, "white", player2)

    pygame.display.update()
    clock.tick(60)
