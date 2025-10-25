
# Animação do Sistema Solar

Projeto de computação gráfica que implementa uma animação do Sistema Solar usando as transformações geométricas básicas: translação, rotação e escala. Esta versão é um exemplo didático em Python usando a biblioteca Pygame Zero (pgzero/pgzrun).

## Conteúdo

- `main.py`: código-fonte principal que desenha o Sol, planetas e a Lua, e aplica as transformações (translação, rotação e escala).

## Objetivo

Desenvolver uma animação que demonstre, de forma visual, o uso de transformações geométricas:
- Translação: movimento dos planetas ao redor do Sol (órbitas).
- Rotação: rotação dos planetas sobre si mesmos e rotação de marcadores (por exemplo, um marcador no Sol ou em cada planeta).
- Escala: tamanhos relativos dos corpos (raios) e dos anéis de Saturno.

O projeto atende ao requisito do trabalho (em equipes de até 6 pessoas) para a disciplina: "Animação do Sistema Solar" — entrega e apresentação em 30/10.

## Como o código organiza as transformações

- Translação (órbitas): implementada em `desenhar_sistema()` ao calcular as coordenadas x,y dos planetas com seno e cosseno a partir de um ângulo dependente do tempo (`tempo_atual * vel_orbita`).
- Rotação (própria): implementada em `desenhar_rotacao_planeta()` — um marcador gira em torno do centro do planeta usando uma combinação de seno/cosseno com um ângulo calculado por `tempo_atual * vel_rot`.
- Escala: os tamanhos dos corpos são controlados pelos valores `raio` no dicionário `planetas` e por `RAIO_SOL` para o Sol; os anéis de Saturno são desenhados com raio maior que o planeta (ex.: `p["raio"] * 1.8`).

Funções-chaves em `main.py`:
- `update(dt)`: atualiza o tempo de animação (`tempo_atual`).
- `draw()`: limpa a tela e chama `desenhar_sol()` e `desenhar_sistema()`.
- `desenhar_sol()`: desenha o Sol e um marcador rotativo no seu contorno (rot ação + translação do marcador em relação ao Sol).
- `desenhar_sistema()`: desenha as órbitas, os planetas (translação + escala), chama `desenhar_rotacao_planeta()` para a rotação própria e também desenha a Lua como composição de translacções (a Lua orbita a Terra, que por sua vez orbita o Sol).

## Requisitos

- Python 3.7+ (recomendado 3.8/3.9/3.10)
- Biblioteca: Pygame Zero (pgzero) — fornece `pgzrun`.

## Instalação e execução (Windows PowerShell)

1. (Opcional) criar e ativar um ambiente virtual:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Instalar dependência:

```powershell
pip install pgzero
```

3. Executar a animação:

```powershell
python -m pgzrun main.py
```

Observação: `pgzrun main.py` também funciona se o script `pgzrun` estiver disponível no PATH.
