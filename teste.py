    count = 2
    rest_count = True
    find_bullet = True
    enemy_list.clear()
    global xpos, salas, gerenciador, trans_state, mov_log_text, loaded_content, rest_cnt, bullet_cnt, direction, walk_timer
    if loaded_content:
        rest_count = rest_c
        find_bullet = find_b
        loaded_content = False
    if trans_state == "fase3":
        salas = 0
        trans_state = "standby"
    mov_log_text = ""
    xchange = 0
    salas += 1
    print(trans_state)

    while True:
        music(count)

        if walk_timer > 0:
            walk_timer -= 1

        if salas == 5:
            cutscene(cutscene18, "fase3")

        if salas == 9:
            cutscene(cutscene19, "fase3")

        # key events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    xchange = + 7
                    jacob.animate()
                    direction = "R"
                if event.key == K_a:
                    xchange = - 7
                    jacob.animate()
                    direction = "L"
                if event.key == K_SPACE:
                    for i in range(len(party)):
                        print(party[i].xp, party[i].to_next_lvl)
                if event.key == K_v:
                    if find_bullet:
                        bullet_cnt += 1
                        for i in range(len(party)):
                            party[i].procurar()
                        find_bullet = False
                        mov_log_text = "o grupo recuperou 5 balas cada"
                if event.key == K_s:
                    # (self, vida, dano_m, dano_r, cor, nome, lvl, xp, ammo, inc_mel, inc_ran, inc_vida)
                    save_game(stats=[(chr_list[stats].vida, chr_list[stats].dano_m, chr_list[stats].dano_r,
                                      stats, chr_list[stats].level, chr_list[stats].xp, chr_list[stats].ammo,
                                      chr_list[stats].inc_mel, chr_list[stats].inc_ran, chr_list[stats].inc_vida)
                                     for stats in range(len(chr_list))], party=[character.nome for character in party],
                              lvl_room=(3, salas - 1), x_pos=xpos, rest_count=rest_count, find_bullet=find_bullet,
                              score_conds=(save_cnt + 1, rest_cnt, bullet_cnt, death_cnt))
                if rest_count:
                    rest_cnt += 1
                    if event.key == K_c:
                        for i in range(len(party)):
                            party[i].rest()
                        rest_count = False
                        mov_log_text = "o grupo recuperou 50 de vida"
            if event.type == KEYUP:
                if event.key == K_a or K_d:
                    xchange = 0
                    jacob.stop("assets/sprites/jacob/jacob parado.png", direction)

        if xchange != 0:
            if walk_timer == 0:
                walk_timer = 28
                ch1.play(walk)

        # player movement
        if xpos >= 1230:
            xpos = 1
            trans("fase3")
        if xpos <= 0:
            xpos = 0

        xpos += xchange

        # random encounter
        if ((xpos / 10) % 1) == 0 and xpos is not 0:
            chance = random.randint(1, 30)
            if chance == 1:
                pygame.time.wait(1000)
                combate_fase3()

        mov_log = font_menu_3.render(mov_log_text, True, (0, 0, 0))

        # draw
        screen.blit(bg, (0, 0))
        screen.blit(jacob.img, (xpos, SCREEN_H - jacob.img.get_height()))
        jacob.update(0.25, direction)
        screen.blit(mov_log, (0, 0))
        pygame.display.update()