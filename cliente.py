import pygame
from random import randint
from _thread import start_new_thread
import socket


def upload_data(scr):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 55000

    print('Waiting for connection')
    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(str(e))

    client_socket.sendall(str(scr).encode('ascii'))
    while True:
        try:
            data = client_socket.recv(1024)
        except socket.error as e:
            print(str(e))
            break
        else:
            info = data.decode('ascii')

            scores_list = list()
            scr_info = info[1:-1]
            start_point = 0
            end_point = 0
            avaiable_info = True
            while avaiable_info:
                start = scr_info.find('(', start_point)
                start_point = start + 1
                if start == -1:
                    avaiable_info = False
                if avaiable_info:
                    end = scr_info.find(')', end_point)
                    end_point = end + 1
                    converted_info = scr_info[start + 1:end].split(', ')
                    converted_info[0] = converted_info[0][1:-1]
                    scores_list.append(converted_info)
            scores_list.sort(key=lambda scr_data: scr_data[1], reverse=True)

            pos = 1
            scoreboard.clear()
            for score in range(len(scores_list)):
                text = f'{pos}º lugar: {scores_list[score][0]} - {scores_list[score][1]} pontos'
                scoreboard.append(font.render(text, True, (255, 255, 255)))
                pos += 1
            print(scoreboard)
    client_socket.close()


points = list()
clientes = list()

pygame.init()

largura = 500
altura = 500
screen = pygame.display.set_mode((largura, altura))

name = 'AAA'
result = randint(100, 500)
uploading = True

font = pygame.font.SysFont('', 38)

scoreboard = list()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if uploading:
        start_new_thread(upload_data, ((name, result), ))
        uploading = False

    screen.fill((0, 0, 0))

    y = 0
    for info in scoreboard:
        screen.blit(info, (screen.get_width() // 2 - info.get_width() // 2, 100 + 80 * y))
        y += 1

    pygame.display.update()
