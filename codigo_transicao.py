def transicao(battle=False, cutscene=False, level=0, room=0):
    """
    Transição entre telas.

    param battle: True = transição para tela de batalha
    param cutscene: True = transição para tela de cutscene
    param level: número inteiro indicando a fase atual
    param room: número inteiro indicando a sala atual
    """
    if battle:
        return 'batalha'
    else:
        if cutscene:
            return 'cutscene'
        else:
            return 'fora de batalha', level, room
