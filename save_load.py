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
                if event.key == pygame.K_s:
                    if slot_select < 2:
                        slot_select += 1
                    else:
                        slot_select = 0
                if event.key == pygame.K_w:
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


def load_file():
    """
    Inicializa a tela de load file do jogo.
    Retorna uma lista com todas as informações contidas no arquivo txt escolhido.
    Cada linha do arquivo é uma string da lista.
    """

    font_2 = pygame.font.SysFont("arial", 50)

    load_text = font_2.render('Escolha um slot para carregar:', True, (255, 255, 255))
    X = font_2.render("X", True, (255, 255, 255))
    slots = (font_2.render('Slot 1', True, (255, 255, 255)), font_2.render('Slot 2', True, (255, 255, 255)),
             font_2.render('Slot 3', True, (255, 255, 255)))
    empty_slot = font_2.render(' -> Vazio', True, (255, 255, 255))

    load_screen = True
    slot_select = 0
    show_text = False

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
                if event.key == pygame.K_s:
                    if slot_select < 2:
                        slot_select += 1
                    else:
                        slot_select = 0
                    if show_text:
                        show_text = False
                if event.key == pygame.K_w:
                    if slot_select > 0:
                        slot_select -= 1
                    else:
                        slot_select = 2
                    if show_text:
                        show_text = False
                if event.key == pygame.K_RETURN:
                    try:
                        save = open(f'save0{slot_select}.txt', 'r')
                    except FileNotFoundError:
                        show_text = True
                    else:
                        for linha in save:
                            info.append(linha[:-1])
                        return string_converter(info)

        # X mark
        screen.blit(X, (screen.get_width() // 2 - slots[0].get_rect().width // 2
                        - X.get_rect().width, 300 + 80 * slot_select))
        if show_text:
            screen.blit(empty_slot, (screen.get_width() // 2 + slots[0].get_rect().width // 2, 300 + 80 * slot_select))

        pygame.display.update()


def string_converter(info):
    """
    Converte todos os dados de string coletados ao carregar um arquivo de save.
    Retorna um dicionário com os dados convertidos.

    Parâmetro a ser passado:
    info -> lista com os dados carregados do arquivo txt
    """

    # Converte a primeira linha do arquivo txt
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
            stats.append(list(map(int, valores.split(', '))))

    # Converte a segunda linha do arquivo txt
    data = info[1][1:-1]
    party_chrs = list(data.split(', '))
    for name in range(len(party_chrs)):
        party_chrs[name] = party_chrs[name][1:-1]

    # Converte a terceira linha do arquivo txt
    data = info[2][1:-1]
    lvl_room = list(map(int, data.split(', ')))
    if lvl_room[0] == 0:
        lvl_room[0] = 'tutorial'
    elif lvl_room[0] == 1:
        lvl_room[0] = 'fase1'
    lvl_room = tuple(lvl_room)

    # Converte a quarta linha do arquivo txt
    data = info[3]
    x_position = int(data)

    # Converte a quinta linha do arquivo txt
    data = info[4]
    if data == 'True':
        rest_c = True
    else:
        rest_c = False

    converted_data = dict()

    converted_data['stats'] = stats
    converted_data['lvl_room'] = lvl_room
    converted_data['party'] = party_chrs
    converted_data['x_pos'] = x_position
    converted_data['rest_counter'] = rest_c
    return converted_data


# (self, vida, dano_m, dano_r, cor, nome, lvl, xp, inc_mel, inc_ran, inc_vida)
