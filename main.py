import pgzrun
import math

# Configurando a janela
WIDTH = 800
HEIGHT = 600
TITLE = "Sistema Solar - Rotação, Translação e Escala"

# Define o centro da tela (onde o Sol ficará), nosso ponto de partida (origem).
CENTRO_X = WIDTH / 2
CENTRO_Y = HEIGHT / 2

# Define as cores e tamanho do sol
COR_SOL = (255, 165, 0)
COR_ORBITA = (60, 60, 60)
RAIO_SOL = 34 # Define o tamanho do Sol (EXEMPLO DE ESCALA).

# Contador de tempo que usamos para calcular o movimento (ângulo).
tempo_atual = 0.0

# Os dados de cada planeta definem as transformações aplicadas:
# - raio: Define o tamanho na tela (ESCALA).
# - orbita: Define a distância do Sol (TRANSLAÇÃO).
# - vel_orbita: Define a velocidade do movimento ao redor do Sol (TRANSLAÇÃO).
# - vel_rot: Define a velocidade de giro em torno do próprio eixo (ROTAÇÃO).
planetas = [
    {"nome": "Mercúrio", "cor": (180, 180, 180), "raio": 4,  "orbita": 60,  "vel_orbita": 0.04, "vel_rot": 0.5},
    {"nome": "Vênus",   "cor": (220, 180, 140), "raio": 6,  "orbita": 100, "vel_orbita": 0.03, "vel_rot": 0.3},
    {"nome": "Terra",   "cor": (0, 120, 255),   "raio": 9,  "orbita": 140, "vel_orbita": 0.02, "vel_rot": 1.0},
    {"nome": "Marte",   "cor": (200, 80, 40),   "raio": 6,  "orbita": 180, "vel_orbita": 0.018, "vel_rot": 0.8},
    {"nome": "Júpiter", "cor": (210, 160, 110), "raio": 18, "orbita": 230, "vel_orbita": 0.01, "vel_rot": 1.5},
    {"nome": "Saturno", "cor": (210, 200, 150), "raio": 16, "orbita": 270, "vel_orbita": 0.008, "vel_rot": 1.2},
    {"nome": "Urano",   "cor": (150, 210, 230), "raio": 12, "orbita": 310, "vel_orbita": 0.006, "vel_rot": 0.9},
    {"nome": "Netuno",  "cor": (50, 90, 200),   "raio": 12, "orbita": 350, "vel_orbita": 0.005, "vel_rot": 0.9},
]
# a lua demonstra a composicao de translacoes (orbita em torno de um objeto que ja se move)
lua = {"cor": (192, 192, 192), "raio": 3, "orbita": 20, "vel_orbita": 0.09}

# logica do tempo
def update(dt):
    # soma o tempo que passou para que a animação continue a rodar
    global tempo_atual
    tempo_atual += dt


# funcoes de desenho (aplicacao das transformacoes)
def draw():
    # desenha todos os objetos na tela em suas posicoes atualizadas
    screen.fill((0, 0, 0))
    desenhar_sol()
    desenhar_sistema()


def desenhar_sol():
    # escala: O tamanho do sol eh determinado pela variavel RAIO_SOL
    screen.draw.filled_circle((CENTRO_X, CENTRO_Y), RAIO_SOL, COR_SOL)

    # rotacao: calculamos um angulo para fazer um marcador girar no sol
    ang = tempo_atual * 0.6
    
    # rotacao + translacao: o marcador eh desenhado em uma nova posicao (mx, my),
    # que foi girada ao redor do centro do sol
    mx = CENTRO_X + (RAIO_SOL * 0.7) * math.cos(ang)
    my = CENTRO_Y + (RAIO_SOL * 0.7) * math.sin(ang)
    screen.draw.filled_circle((mx, my), 4, (255, 50, 0))


def desenhar_sistema():
    # aplica translacao, escala e rotacao aos planetas
    for p in planetas:
        orb = p["orbita"]

        # desenha a linha/traço da órbita do planeta ao redor do Sol
        screen.draw.circle((int(CENTRO_X), int(CENTRO_Y)), int(orb), COR_ORBITA)

        # translacao (orbita)
        ang = tempo_atual * p["vel_orbita"] 
        
        # a nova posicao (x, y) eh calculada usando seno e cosseno a partir do
        # centro (CENTRO_X, CENTRO_Y). Isso move o planeta no plano (translacao)
        x = CENTRO_X + orb * math.cos(ang)
        y = CENTRO_Y + orb * math.sin(ang)

        # escala: o planeta eh desenhado com o tamanho (raio) definido nos dados
        screen.draw.filled_circle((x, y), p["raio"], p["cor"])

        # rotacao (propria): faz o planeta girar em torno de si mesmo
        desenhar_rotacao_planeta(x, y, p["raio"], tempo_atual * p["vel_rot"])

        # escala dos aneis de saturno tem que ser maior que o planeta pra ficar rodeando ele
        if p["nome"] == "Saturno":
            screen.draw.circle((x, y), int(p["raio"] * 1.8), (200, 180, 140))

        # composicao de translacoes da lua
        if p["nome"] == "Terra":
            # desenha a órbita da Lua ao redor da Terra
            screen.draw.circle((int(x), int(y)), int(lua["orbita"]), COR_ORBITA)

            ang_lua = tempo_atual * lua["vel_orbita"]
            
            # a posicao da lua (lx, ly) eh calculada a partir da posicao da terra (x, y)
            # eh a soma da translacao da terra + a translacao da lua
            lx = x + lua["orbita"] * math.cos(ang_lua)
            ly = y + lua["orbita"] * math.sin(ang_lua)
            
            # desenha a lua com seu fator de escala
            screen.draw.filled_circle((lx, ly), lua["raio"], lua["cor"])
            
        # translacao simples: move o texto para perto do planeta (nome do planeta para os leigos)
        label_x = x + p["raio"] + 6
        label_y = y - p["raio"] - 6
        screen.draw.text(p["nome"], (label_x, label_y), color=(250, 250, 250))


def desenhar_rotacao_planeta(centro_x, centro_y, raio, angulo):
    # funcao auxiliar que aplica rotacao em torno do centro do planeta e translacao
    
    # escala: a distancia do marcador eh definida pelo raio do planeta
    distancia = raio * 0.7
    
    # rotacao e translacao: move o marcador girado para a posicao final na tela
    mx = centro_x + distancia * math.cos(angulo)
    my = centro_y + distancia * math.sin(angulo)
    screen.draw.filled_circle((mx, my), 2, (255, 255, 255))


# inicia o programa
pgzrun.go()