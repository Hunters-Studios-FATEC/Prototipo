from classes import *

lvl = 1
xp = 0
to_next_lvl = 25

j_level = 1
j_xp = 0
j_to_next_lvl = 25
j_vida = jacob.vida
j_mel = jacob.dano_m
j_ran = jacob.dano_r

b_vida = barbara.vida
b_mel = barbara.dano_m
b_ran = barbara.dano_r

ka_vida = kazi.vida
ka_mel = kazi.dano_m
ka_ran = kazi.dano_r

ke_vida = kenji.vida
ke_mel = kenji.dano_m
ke_ran = kenji.dano_r

while True:
    print(j_level, j_xp, j_to_next_lvl, j_mel, j_ran, j_vida)

    xp = int(input("quanto xp? "))

    j_xp = xp

    if j_xp >= j_to_next_lvl:
        j_level += 1
        j_xp = j_xp - j_to_next_lvl
        j_to_next_lvl = round(j_to_next_lvl * 1.5)

        j_vida += 20
        j_mel += 2
        j_ran += 3

        print(j_level, j_xp, j_to_next_lvl, j_mel, j_ran, j_vida)