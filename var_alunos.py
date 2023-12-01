import foosball_alunos

def le_replay(nome_ficheiro):
    '''
    Função que recebe o nome de um ficheiro contendo um replay, e que deverá 
    retornar um dicionário com as seguintes chaves:
    bola - lista contendo tuplos com as coordenadas xx e yy da bola
    jogador_vermelho - lista contendo tuplos com as coordenadas xx e yy da do jogador\_vermelho
    jogador_azul - lista contendo tuplos com as coordenadas xx e yy da do jogador\_azul
    '''
    replay = {
        "bola": None,
        "jogador_vermelho": None,
        "jogador_azul": None 
    }
    
    with open(nome_ficheiro, "r") as file:
        for key in replay.keys():
            line = file.readline()
            pares = line.split(";")[:-1]
            lista_de_pares = list()
            for par in pares:
                aux = par.split(",")
                lista_de_pares.append((float(aux[0]), float(aux[1])))
            replay[key] = lista_de_pares
    return replay
        


def main():
    estado_jogo = foosball_alunos.init_state()
    foosball_alunos.setup(estado_jogo, False)
    replay = le_replay('replay_golo_jv_0_ja_1.txt')
    for i in range(len(replay['bola'])):
        estado_jogo['janela'].update()
        estado_jogo['jogador_vermelho'].setpos(replay['jogador_vermelho'][i])
        estado_jogo['jogador_azul'].setpos(replay['jogador_azul'][i])
        estado_jogo['bola']['objecto'].setpos(replay['bola'][i])
    estado_jogo['janela'].exitonclick()


if __name__ == '__main__':
    main()