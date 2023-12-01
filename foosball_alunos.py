import turtle as t
import functools
import random
import math

LARGURA_JANELA = 1024
ALTURA_JANELA = 600
DEFAULT_TURTLE_SIZE = 40
DEFAULT_TURTLE_SCALE = 3
RAIO_JOGADOR = DEFAULT_TURTLE_SIZE / DEFAULT_TURTLE_SCALE
RAIO_BOLA = DEFAULT_TURTLE_SIZE / 2
PIXEIS_MOVIMENTO = 90
LADO_MAIOR_AREA = ALTURA_JANELA / 3
LADO_MENOR_AREA = 50
RAIO_MEIO_CAMPO = LADO_MAIOR_AREA / 2
START_POS_BALIZAS = ALTURA_JANELA / 4
BOLA_START_POS = (5,5)
VELOCIDADE_BOLA = 1/1.5


# Funções responsáveis pelo movimento dos jogadores no ambiente. 
# O número de unidades que o jogador se pode movimentar é definida pela constante 
# PIXEIS_MOVIMENTO. As funções recebem um dicionário que contém o estado 
# do jogo e o jogador que se está a movimentar. 

def jogador_cima(estado_jogo, jogador):
    if (estado_jogo['var'][jogador][-1][1] + PIXEIS_MOVIMENTO < ALTURA_JANELA/2):
        estado_jogo[jogador].setheading(90)
        estado_jogo[jogador].up()
        estado_jogo[jogador].fd(PIXEIS_MOVIMENTO)
        guarda_posicoes_para_var(estado_jogo)

def jogador_baixo(estado_jogo, jogador):
    if (estado_jogo['var'][jogador][-1][1] - PIXEIS_MOVIMENTO > -ALTURA_JANELA/2):
        estado_jogo[jogador].setheading(-90)
        estado_jogo[jogador].up()
        estado_jogo[jogador].fd(PIXEIS_MOVIMENTO)
        guarda_posicoes_para_var(estado_jogo)
    
def jogador_direita(estado_jogo, jogador):
    if (estado_jogo['var'][jogador][-1][0] + PIXEIS_MOVIMENTO < LARGURA_JANELA/2):
        estado_jogo[jogador].setheading(0)
        estado_jogo[jogador].up()
        estado_jogo[jogador].fd(PIXEIS_MOVIMENTO)
        guarda_posicoes_para_var(estado_jogo)

def jogador_esquerda(estado_jogo, jogador):
    if (estado_jogo['var'][jogador][-1][0] - PIXEIS_MOVIMENTO > -LARGURA_JANELA/2):
        estado_jogo[jogador].setheading(180)
        estado_jogo[jogador].up()
        estado_jogo[jogador].fd(PIXEIS_MOVIMENTO)
        guarda_posicoes_para_var(estado_jogo)


def desenha_circulo_central(turtle):
    turtle.up()
    turtle.right(90)
    turtle.fd(RAIO_MEIO_CAMPO)
    turtle.left(90)
    turtle.down()
    turtle.circle(RAIO_MEIO_CAMPO)
    turtle.home()

def desenha_linha_meio_campo(turtle):
    turtle.up()
    turtle.right(90)
    turtle.fd(ALTURA_JANELA/2)
    turtle.left(180)
    turtle.down()
    turtle.fd(ALTURA_JANELA)
    turtle.home()

def desenha_baliza(turtle, pos_x, pos_y, orientacao):
    turtle.up()
    turtle.goto(pos_x, pos_y)
    turtle.right(orientacao)
    turtle.down()
    turtle.fd(LADO_MENOR_AREA)
    turtle.left(90)
    turtle.fd(LADO_MAIOR_AREA)
    turtle.left(90)
    turtle.fd(LADO_MENOR_AREA)
    
def desenha_linhas_campo():
    ''' Função responsável por desenhar as linhas do campo, 
    nomeadamente a linha de meio campo, o círculo central, e as balizas. '''
    turtle = t.Turtle()
    turtle.hideturtle()
    turtle.width(10)
    turtle.speed(0)
    turtle.color("white")
    desenha_circulo_central(turtle)
    desenha_linha_meio_campo(turtle)
    desenha_baliza(turtle, LARGURA_JANELA/2, LADO_MAIOR_AREA/2, 180)
    desenha_baliza(turtle, -LARGURA_JANELA/2, -LADO_MAIOR_AREA/2, 0)


def criar_bola():
    '''
    Função responsável pela criação da bola. 
    Deverá considerar que esta tem uma forma redonda, é de cor preta, 
    começa na posição BOLA_START_POS com uma direção aleatória. 
    Deverá ter em conta que a velocidade da bola deverá ser superior à dos jogadores. 
    A função deverá devolver um dicionário contendo 4 elementos: o objeto bola, 
    a sua direção no eixo dos xx, a sua direção no eixo dos yy, 
    e um elemento inicialmente a None que corresponde à posição anterior da mesma.
    '''
    bola = t.Turtle()
    bola.up()
    bola.goto(BOLA_START_POS[0], BOLA_START_POS[1])
    bola.shape("circle")
    bola.shapesize(stretch_wid=RAIO_BOLA/15, stretch_len=RAIO_BOLA/15)
    angulo = random.randint(0, 359) * math.pi/180
    return {'objecto': bola, 'xx': math.cos(angulo) * VELOCIDADE_BOLA, 'yy': math.sin(angulo) * VELOCIDADE_BOLA, 'pos': [None, None]}
    

def cria_jogador(x_pos_inicial, y_pos_inicial, cor):
    ''' Função responsável por criar e devolver o objeto que corresponde a um jogador (um objecto Turtle). 
    A função recebe 3 argumentos que correspondem às coordenadas da posição inicial 
    em xx e yy, e a cor do jogador. A forma dos jogadores deverá ser um círculo, 
    cujo seu tamanho deverá ser definido através da função shapesize
    do módulo \texttt{turtle}, usando os seguintes parâmetros: 
    stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE. '''
    jogador = t.Turtle()
    jogador.color(cor)
    jogador.up()
    jogador.goto(x_pos_inicial, y_pos_inicial)
    jogador.shape("circle")
    jogador.shapesize(stretch_wid=DEFAULT_TURTLE_SCALE, stretch_len=DEFAULT_TURTLE_SCALE)
    return jogador


def init_state():
    estado_jogo = {}
    estado_jogo['bola'] = None
    estado_jogo['jogador_vermelho'] = None
    estado_jogo['jogador_azul'] = None
    estado_jogo['var'] = {
        'bola' : [],
        'jogador_vermelho' : [],
        'jogador_azul' : [],
    }
    estado_jogo['pontuacao_jogador_vermelho'] = 0
    estado_jogo['pontuacao_jogador_azul'] = 0
    return estado_jogo


def cria_janela():
    #create a window and declare a variable called window and call the screen()
    window=t.Screen()
    window.title("Foosball Game")
    window.bgcolor("green")
    window.setup(width = LARGURA_JANELA,height = ALTURA_JANELA)
    window.tracer(0)
    return window


def cria_quadro_resultados():
    #Code for creating pen for scorecard update
    quadro=t.Turtle()
    quadro.speed(0)
    quadro.color("Blue")
    quadro.penup()
    quadro.hideturtle()
    quadro.goto(0,260)
    quadro.write("Player A: 0\t\tPlayer B: 0 ", align="center", font=('Monaco',24,"normal"))
    return quadro


def terminar_jogo(estado_jogo):
    '''
     Função responsável por terminar o jogo. Nesta função, deverá atualizar o ficheiro 
     ''historico_resultados.csv'' com o número total de jogos até ao momento, 
     e o resultado final do jogo. Caso o ficheiro não exista, 
     ele deverá ser criado com o seguinte cabeçalho: 
     NJogo,JogadorVermelho,JogadorAzul.
    '''
    numero_jogo = 1

    with open('historico_resultados.csv', 'a') as file_1:
        if file_1.tell() == 0:
            file_1.write("{},{},{}\n".format("NJogo", "JogadorVermelho", "JogadorAzul"))

        else:
            with open('historico_resultados.csv', 'r') as file:
                linhas = file.readlines()
                ultimo_jogo = linhas[-1].split(",")[:-1]
                numero_jogo = int(ultimo_jogo[0]) + 1

        file_1.write("{},{},{}\n".format(numero_jogo, estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul']))


    print("Adeus")
    estado_jogo['janela'].bye()


def setup(estado_jogo, jogar):
    janela = cria_janela()
    #Assign keys to play
    janela.listen()
    if jogar:
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_vermelho') ,'w')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_vermelho') ,'s')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_vermelho') ,'a')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_vermelho') ,'d')
        janela.onkeypress(functools.partial(jogador_cima, estado_jogo, 'jogador_azul') ,'Up')
        janela.onkeypress(functools.partial(jogador_baixo, estado_jogo, 'jogador_azul') ,'Down')
        janela.onkeypress(functools.partial(jogador_esquerda, estado_jogo, 'jogador_azul') ,'Left')
        janela.onkeypress(functools.partial(jogador_direita, estado_jogo, 'jogador_azul') ,'Right')
        janela.onkeypress(functools.partial(terminar_jogo, estado_jogo) ,'Escape')
        quadro = cria_quadro_resultados()
        estado_jogo['quadro'] = quadro
    desenha_linhas_campo()
    bola = criar_bola()
    jogador_vermelho = cria_jogador(-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "red")
    jogador_azul = cria_jogador(((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0, "blue")
    estado_jogo['janela'] = janela
    estado_jogo['bola'] = bola
    estado_jogo['jogador_vermelho'] = jogador_vermelho
    estado_jogo['jogador_azul'] = jogador_azul
    guarda_posicoes_para_var(estado_jogo)


def update_board(estado_jogo):
    estado_jogo['quadro'].clear()
    estado_jogo['quadro'].write("Player A: {}\t\tPlayer B: {} ".format(estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul']),align="center",font=('Monaco',24,"normal"))
    

def movimenta_bola(estado_jogo):
    '''
    Função responsável pelo movimento da bola que deverá ser feito tendo em conta a
    posição atual da bola e a direção em xx e yy.
    '''
    pos_anterior = estado_jogo['bola']['objecto'].pos()
    estado_jogo['bola']['pos'] = pos_anterior
    estado_jogo['bola']['objecto'].goto(pos_anterior[0] + estado_jogo['bola']['xx'],pos_anterior[1] + estado_jogo['bola']['yy'])
    

def verifica_colisoes_ambiente(estado_jogo):
    '''
    Função responsável por verificar se há colisões com os limites do ambiente, 
    atualizando a direção da bola. Não se esqueça de considerar que nas laterais, 
    fora da zona das balizas, a bola deverá inverter a direção onde atingiu o limite.
    '''
    if estado_jogo['bola']['objecto'].pos()[1] + RAIO_BOLA >= ALTURA_JANELA/2 or estado_jogo['bola']['objecto'].pos()[1] - RAIO_BOLA <= - ALTURA_JANELA/2:
        estado_jogo['bola']['yy'] = -estado_jogo['bola']['yy']
    
    elif estado_jogo['bola']['objecto'].pos()[0] + RAIO_BOLA >= LARGURA_JANELA/2 or estado_jogo['bola']['objecto'].pos()[0] - RAIO_BOLA <= -LARGURA_JANELA/2:
        estado_jogo['bola']['xx'] = -estado_jogo['bola']['xx']


def reposiciona_jogo(estado_jogo):
    estado_jogo['jogador_vermelho'].goto(-((ALTURA_JANELA / 2) + LADO_MENOR_AREA), 0)
    estado_jogo['jogador_azul'].goto((ALTURA_JANELA / 2) + LADO_MENOR_AREA, 0)

    estado_jogo['bola']['objecto'].goto(BOLA_START_POS[0], BOLA_START_POS[1])
    angulo = random.randint(0, 359) * math.pi / 180
    estado_jogo['bola']['xx'] = math.cos(angulo) / 1.5
    estado_jogo['bola']['yy'] = math.sin(angulo) / 1.5
       
def verifica_golo_jogador_vermelho(estado_jogo):
    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]ja[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''
    if estado_jogo['bola']['objecto'].pos()[0] + RAIO_BOLA >= LARGURA_JANELA/2 and estado_jogo['bola']['objecto'].pos()[1] <= ALTURA_JANELA/2 - LADO_MAIOR_AREA and estado_jogo['bola']['objecto'].pos()[1] >=  -ALTURA_JANELA/2 + LADO_MAIOR_AREA:  
        estado_jogo['pontuacao_jogador_vermelho'] += 1
        update_board(estado_jogo)
        estado_jogo['janela'].update()
        
        nome_ficheiro_var = "replay_golo_jv_{}_ja_{}.txt".format(estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul'])
        with open(nome_ficheiro_var, 'w') as file:
            for key in estado_jogo['var'].keys():
                for i in range(len(estado_jogo['var'][key])): 
                    file.write("{},{};".format(estado_jogo['var'][key][i][0], estado_jogo['var'][key][i][1]))
                file.write("\n")
            
        reposiciona_jogo(estado_jogo)

def verifica_golo_jogador_azul(estado_jogo):
    '''
    Função responsável por verificar se um determinado jogador marcou golo. 
    Para fazer esta verificação poderá fazer uso das constantes: 
    LADO_MAIOR_AREA e 
    START_POS_BALIZAS. 
    Note que sempre que há um golo, deverá atualizar a pontuação do jogador, 
    criar um ficheiro que permita fazer a análise da jogada pelo VAR, 
    e reiniciar o jogo com a bola ao centro. 
    O ficheiro para o VAR deverá conter todas as informações necessárias 
    para repetir a jogada, usando as informações disponíveis no objeto 
    estado_jogo['var']. O ficheiro deverá ter o nome 
    
    replay_golo_jv_[TotalGolosJogadorVermelho]ja[TotalGolosJogadorAzul].txt 
    
    onde [TotalGolosJogadorVermelho], [TotalGolosJogadorAzul] 
    deverão ser substituídos pelo número de golos marcados pelo jogador vermelho 
    e azul, respectivamente. Este ficheiro deverá conter 3 linhas, estruturadas 
    da seguinte forma:
    Linha 1 - coordenadas da bola;
    Linha 2 - coordenadas do jogador vermelho;
    Linha 3 - coordenadas do jogador azul;
    
    Em cada linha, os valores de xx e yy das coordenadas são separados por uma 
    ',', e cada coordenada é separada por um ';'.
    '''
    if estado_jogo['bola']['objecto'].pos()[0] - RAIO_BOLA  <= -LARGURA_JANELA/2  and estado_jogo['bola']['objecto'].pos()[1]  <= ALTURA_JANELA/2 - LADO_MAIOR_AREA and estado_jogo['bola']['objecto'].pos()[1]  >=  -ALTURA_JANELA/2 + LADO_MAIOR_AREA:  
        estado_jogo['pontuacao_jogador_azul'] += 1
        update_board(estado_jogo)
        estado_jogo['janela'].update()
        
        nome_ficheiro_var = "replay_golo_jv_{}_ja_{}.txt".format(estado_jogo['pontuacao_jogador_vermelho'], estado_jogo['pontuacao_jogador_azul'])
        with open(nome_ficheiro_var, 'w') as file:
            for key in estado_jogo['var'].keys():
                for i in range(len(estado_jogo['var'][key])): 
                    file.write("{},{};".format(estado_jogo['var'][key][i][0], estado_jogo['var'][key][i][1]))
                file.write("\n")
            
        reposiciona_jogo(estado_jogo)
    
def verifica_golos(estado_jogo):
    verifica_golo_jogador_vermelho(estado_jogo)
    verifica_golo_jogador_azul(estado_jogo)


def verifica_toque_jogador_azul(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    pos_x = (estado_jogo['bola']['objecto'].pos()[0] - estado_jogo['jogador_azul'].pos()[0])**2
    pos_y = (estado_jogo['bola']['objecto'].pos()[1] - estado_jogo['jogador_azul'].pos()[1])**2
    distancia = math.sqrt(pos_x + pos_y)

    if (distancia <= RAIO_BOLA + RAIO_JOGADOR):
        reta = (estado_jogo['bola']['objecto'].pos() - estado_jogo['jogador_azul'].pos())
        reta_perpendicular = (-reta[0], reta[1])

        #Angulo entre a direcao da velocidade da bola e a reta perpendicular a reta dos centros dos objectos
        produto_escalar = reta_perpendicular[0]*estado_jogo['bola']['xx'] + reta_perpendicular[1]*estado_jogo['bola']['yy']
        norma_1 = math.sqrt(reta_perpendicular[0]**2 + reta_perpendicular[1]**2)
        norma_2 = math.sqrt(estado_jogo['bola']['xx']**2 + estado_jogo['bola']['yy']**2)
        angulo = math.acos(produto_escalar / (norma_1 * norma_2)) * 180 / math.pi
        angulo_bola = (180 - 2 * angulo) + estado_jogo['bola']['objecto'].heading()
        estado_jogo['bola']['xx'] = math.cos(angulo_bola) * VELOCIDADE_BOLA
        estado_jogo['bola']['yy'] = math.sin(angulo_bola) * VELOCIDADE_BOLA

def verifica_toque_jogador_vermelho(estado_jogo):
    '''
    Função responsável por verificar se o jogador tocou na bola. 
    Sempre que um jogador toca na bola, deverá mudar a direção desta.
    '''
    pos_x = (estado_jogo['bola']['objecto'].pos()[0] - estado_jogo['jogador_vermelho'].pos()[0])**2
    pos_y = (estado_jogo['bola']['objecto'].pos()[1] - estado_jogo['jogador_vermelho'].pos()[1])**2
    distancia = math.sqrt(pos_x + pos_y)

    if (distancia <= RAIO_BOLA + RAIO_JOGADOR):
        reta = (estado_jogo['bola']['objecto'].pos() - estado_jogo['jogador_vermelho'].pos())
        reta_perpendicular = (-reta[0], reta[1])

        #Angulo entre a direcao da velocidade da bola e a reta perpendicular a reta dos centros dos objectos
        produto_escalar = reta_perpendicular[0]*estado_jogo['bola']['xx'] + reta_perpendicular[1]*estado_jogo['bola']['yy']
        norma_1 = math.sqrt(reta_perpendicular[0]**2 + reta_perpendicular[1]**2)
        norma_2 = math.sqrt(estado_jogo['bola']['xx']**2 + estado_jogo['bola']['yy']**2)
        angulo = math.acos(produto_escalar / (norma_1 * norma_2)) * 180 / math.pi
        angulo_bola = (180 - 2 * angulo) + estado_jogo['bola']['objecto'].heading()
        estado_jogo['bola']['xx'] = math.cos(angulo_bola) * VELOCIDADE_BOLA
        estado_jogo['bola']['yy'] = math.sin(angulo_bola) * VELOCIDADE_BOLA


def guarda_posicoes_para_var(estado_jogo):
    estado_jogo['var']['bola'].append(estado_jogo['bola']['objecto'].pos())
    estado_jogo['var']['jogador_vermelho'].append(estado_jogo['jogador_vermelho'].pos())
    estado_jogo['var']['jogador_azul'].append(estado_jogo['jogador_azul'].pos())


def main():
    estado_jogo = init_state()
    setup(estado_jogo, True)
    while True:
        estado_jogo['janela'].update()
        if estado_jogo['bola'] is not None:
            movimenta_bola(estado_jogo)
        verifica_colisoes_ambiente(estado_jogo)
        verifica_golos(estado_jogo)
        if estado_jogo['jogador_vermelho'] is not None:
            verifica_toque_jogador_azul(estado_jogo)
        if estado_jogo['jogador_azul'] is not None:
            verifica_toque_jogador_vermelho(estado_jogo)

if __name__ == '__main__':
    main()