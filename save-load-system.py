import pygame

pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))


def save_game(**dados):
    """
    Inicializa a tela de salvamento de progresso.

    Parâmetros a serem passados:
    stats -> status dos personagens (exemplo: vida, balas, etc)
    lvl_room -> nível e sala
    """
    font_2 = pygame.font.SysFont("arial", 50)

    save_text = font_2.render('Escolha um slot:', True, (255, 255, 255))
    X = font_2.render("X", True, (255, 255, 255))
    slots = (font_2.render('Slot 1', True, (255, 255, 255)), font_2.render('Slot 2', True, (255, 255, 255)),
             font_2.render('Slot 3', True, (255, 255, 255)))

    save_screen = True
    slot_select = 0

    while save_screen:
        screen.fill((0, 0, 0))

        # slots
        screen.blit(save_text, (screen.get_width() // 2 - save_text.get_rect().width // 2, 100))
        for pos, slt in enumerate(slots):
            screen.blit(slt, (screen.get_width() // 2 - slt.get_rect().width // 2, 300 + 80 * pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_screen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if slot_select < 2:
                        slot_select += 1
                    else:
                        slot_select = 0
                if event.key == pygame.K_UP:
                    if slot_select > 0:
                        slot_select -= 1
                    else:
                        slot_select = 2
                if event.key == pygame.K_ESCAPE:
                    save_screen = False
                if event.key == pygame.K_RETURN:
                    save = open(f'save0{slot_select}.txt', 'w')
                    for data in dados:
                        save.write(str(dados[f'{data}']) + '\n')
                    save.close()
                    save_screen = False

        # X mark
        screen.blit(X, (screen.get_width() // 2 - slots[0].get_rect().width // 2
                        - X.get_rect().width, 300 + 80 * slot_select))

        pygame.display.update()


def load_game():
    """
    Inicializa a tela de load file do jogo.
    Retorna uma lista com todas as informações continudas no arquivo txt escolhido.
    Cada linha do arquivo é uma string da lista.
    """
    font_2 = pygame.font.SysFont("arial", 50)

    load_text = font_2.render('Escolha um slot para carregar:', True, (255, 255, 255))
    X = font_2.render("X", True, (255, 255, 255))
    slots = (font_2.render('Slot 1', True, (255, 255, 255)), font_2.render('Slot 2', True, (255, 255, 255)),
             font_2.render('Slot 3', True, (255, 255, 255)))

    load_screen = True
    slot_select = 0

    info = list()

    while load_screen:
        screen.fill((0, 0, 0))

        # slots
        screen.blit(load_text, (screen.get_width() // 2 - load_text.get_rect().width // 2, 100))
        for pos, slt in enumerate(slots):
            screen.blit(slt, (screen.get_width() // 2 - slt.get_rect().width // 2, 300 + 80 * pos))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                load_screen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if slot_select < 2:
                        slot_select += 1
                    else:
                        slot_select = 0
                if event.key == pygame.K_UP:
                    if slot_select > 0:
                        slot_select -= 1
                    else:
                        slot_select = 2
                if event.key == pygame.K_RETURN:
                    save = open(f'save0{slot_select}.txt', 'r')
                    for linha in save:
                        info.append(linha[:-1])
                    return info

        # X mark
        screen.blit(X, (screen.get_width() // 2 - slots[0].get_rect().width // 2
                        - X.get_rect().width, 300 + 80 * slot_select))

        pygame.display.update()


def string_converter(info):
    """
    Converte todos os dados de string coletados ao carregar um arquivo de save.
    Retorna um dicionário com os dados convertidos.

    Parâmetro a ser passado:
    info -> lista com os dados carregados do arquivo txt
    """
    data = info[0][1:-1]
    stats = list()

    avaiable_tuples = True
    start_point = 0
    end_point = 0

    while avaiable_tuples:
        start = data.find('(', start_point)
        start_point = start + 1

        fim = data.find(')', end_point)
        end_point = fim + 1

        if start == -1:
            avaiable_tuples = False
        else:
            valores = data[start + 1:fim]
            stats.append(tuple(map(int, valores.split(', '))))
    stats = tuple(stats)

    data = info[1][1:-1]
    lvl_room = tuple(map(int, data.split(', ')))

    converted_data = dict()

    converted_data['stats'] = stats
    converted_data['lvl_room'] = lvl_room
    return converted_data


save_game(stats=((100, 50, 1), (82, 30, 2)), lvl_room=(1, 1))
