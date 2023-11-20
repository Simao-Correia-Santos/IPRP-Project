import foosball_alunos

def le_replay(nome_ficheiro):
    '''
    Função que recebe o nome de um ficheiro contendo um replay, e que deverá 
    retornar um dicionário com as seguintes chaves:
    bola - lista contendo tuplos com as coordenadas xx e yy da bola
    jogador_vermelho - lista contendo tuplos com as coordenadas xx e yy da do jogador\_vermelho
    jogador_azul - lista contendo tuplos com as coordenadas xx e yy da do jogador\_azul
    '''
    pass
        


def main():
    estado_jogo = foosball_alunos.init_state()
    foosball_alunos.setup(estado_jogo, False)
    replay = le_replay('replay_jogo_n_17.txt')
    for i in range(len(replay['bola'])):
        estado_jogo['janela'].update()
        estado_jogo['jogador_vermelho'].setpos(replay['jogador_vermelho'][i])
        estado_jogo['jogador_azul'].setpos(replay['jogador_azul'][i])
        estado_jogo['bola']['objecto'].setpos(replay['bola'][i])
    estado_jogo['janela'].exitonclick()


if __name__ == '__main__':
    main()