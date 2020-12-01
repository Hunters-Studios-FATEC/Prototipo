def compress_save():
    for i in range(3):
        try:
            decomp_save = open(f'save0{i}.txt', 'r')
        except FileNotFoundError:
            pass
        else:
            info = list()
            for linha in decomp_save:
                info.append(linha[:-1])
            data_dict = str_convert(info)
            decomp_save.close()

            compressed_file = open(f'save0{i}.txt', 'w', encoding='utf8')

            compr_attr = ''
            for attr_list in data_dict['stats']:
                for attribute in attr_list:
                    compr_attr += chr(attribute + 200)
            compressed_file.write(compr_attr + '\n')

            compr_party = ''
            for name in data_dict['party']:
                if name == 'jacob':
                    compr_party += 'a'
                elif name == 'kazi':
                    compr_party += 'b'
                elif name == 'kenji':
                    compr_party += 'c'
                else:
                    compr_party += 'd'
            compressed_file.write(compr_party + '\n')

            compr_lvlroom = ''
            compr_lvlroom += chr(data_dict['lvl_room'][0] + 200)
            compr_lvlroom += chr(data_dict['lvl_room'][1] + 200)
            compressed_file.write(compr_lvlroom + '\n')

            x_pos = chr(int(data_dict['x_pos']) + 200)
            compressed_file.write(str(x_pos) + '\n')

            if data_dict['rest_counter'] is True:
                rest_counter = 't'
            else:
                rest_counter = 'f'
            compressed_file.write(rest_counter + '\n')

            if data_dict['rest_counter'] is True:
                find_bullet = 't'
            else:
                find_bullet = 'f'
            compressed_file.write(find_bullet + '\n')

            compr_conds = ''
            for cond in data_dict['score_conds']:
                compr_conds += chr(cond + 200)
            compressed_file.write(compr_conds + '\n')

            if 'fase4' in data_dict.keys():
                if data_dict['fase4'] is True:
                    fase4 = 't'
                else:
                    fase4 = 'f'
                compressed_file.write(fase4 + '\n')

            compressed_file.close()


def str_convert(info):
    converted_data = dict()

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
    converted_data['stats'] = stats

    data = info[1][1:-1]
    party_chrs = list(data.split(', '))
    for name in range(len(party_chrs)):
        party_chrs[name] = party_chrs[name][1:-1]
    converted_data['party'] = party_chrs

    data = info[2][1:-1]
    lvl_room = list(map(int, data.split(', ')))
    lvl_room = tuple(lvl_room)
    converted_data['lvl_room'] = lvl_room

    data = info[3]
    x_position = float(data)
    converted_data['x_pos'] = x_position

    data = info[4]
    if data == 'True':
        rest_c = True
    else:
        rest_c = False
    converted_data['rest_counter'] = rest_c

    data = info[5]
    if data == 'True':
        find_b = True
    else:
        find_b = False
    converted_data['find_bullet'] = find_b

    data = info[6][1:-1]
    scr_conds = list(map(int, data.split(', ')))
    converted_data['score_conds'] = scr_conds

    if len(info) > 7:
        data = info[7]
        if data == 'True':
            fase_quatro = True
        else:
            fase_quatro = False
        converted_data['fase4'] = fase_quatro

    return converted_data


def decompress_save():
    for i in range(3):
        try:
            compr_save = open(f'save0{i}.txt', 'r', encoding='utf8')
        except FileNotFoundError:
            pass
        else:
            info = list()
            for linha in compr_save:
                info.append(linha[:-1])
            compr_save.close()

            decompr_file = open(f'save0{i}.txt', 'w')

            compr_data = info[0]
            decomp_stats = list()
            for j in range(4):
                decomp_stats.append(list(map(ord, compr_data[10 * j: 10 * j + 10])))
            for pos, decomp_list in enumerate(decomp_stats):
                for num in range(len(decomp_list)):
                    decomp_list[num] -= 200
                decomp_stats[pos] = tuple(decomp_stats[pos])
            decompr_file.write(str(decomp_stats) + '\n')

            compr_data = info[1]
            decomp_party = '['
            for l_pos, letters in enumerate(compr_data):
                if letters == 'a':
                    decomp_party += "'jacob'"
                elif letters == 'b':
                    decomp_party += "'kazi'"
                elif letters == 'c':
                    decomp_party += "'kenji'"
                else:
                    decomp_party += "'barbara'"
                if l_pos < len(compr_data) - 1:
                    decomp_party += ', '
            decomp_party += ']'
            decompr_file.write(decomp_party + '\n')

            level_room = info[2]
            decomp_lvlroom = f'({ord(level_room[0]) - 200}, {ord(level_room[1]) - 200})'
            decompr_file.write(decomp_lvlroom + '\n')

            xpos = info[3]
            decomp_xpos = float(ord(xpos)) - 200
            decompr_file.write(str(decomp_xpos) + '\n')

            rest_c = info[4]
            if rest_c == 't':
                decomp_rest_cnt = 'True'
            else:
                decomp_rest_cnt = 'False'
            decompr_file.write(decomp_rest_cnt + '\n')

            find_b = info[5]
            if find_b == 't':
                decomp_find_b = 'True'
            else:
                decomp_find_b = 'False'
            decompr_file.write(decomp_find_b + '\n')

            score_conds = info[6]
            decomp_score_conds = '('
            for pos, letter in enumerate(score_conds):
                decomp_score_conds += str(ord(letter) - 200)
                if pos < len(score_conds) - 1:
                    decomp_score_conds += ', '
            decomp_score_conds += ')'
            decompr_file.write(decomp_score_conds + '\n')

            if len(info) > 7:
                fase4 = info[5]
                if fase4 == 't':
                    decomp_fase4 = 'True'
                else:
                    decomp_fase4 = 'False'
                decompr_file.write(decomp_fase4 + '\n')

            decompr_file.close()
