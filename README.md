# Space Miner: Asteroid Protocol

`Tecnologia em Análise e Desenvolvimento de Sistemas`

`Projeto de Aplicação Distribuida -- Space Miner`

`Graduado` -- `2025`

Este projeto é um jogo 2D em Python com Pygame, inspirado no clássico Asteroids, com evolução para um simulador espacial de mineração, defesa automatizada e economia digital. O jogador pilota uma nave que coleta recursos, destrói asteroides e retorna à Terra para converter ouro em Bitcoin.

## Integrantes

* Felipe Corrêa Carneiro
 _ (demais nomes conforme o projeto for evoluindo em coletivo ou individual mesmo)_

## Orientadores

* Boot.Dev
* Copilot Code
* Copilot Assistence
* Ai Google Studio

## Instruções de utilização

1. Instale o Python 3.10+
2. Instale o Pygame:
```python
pip install pygame
```
_No terminal_

3. Execute o jogo

_Ainda no terminal, vá até o diretório do jogo e digite_

```python
python main.py
```


# Documentação

<ol>
<li><a href="docs/01-Documentação de Contexto.md"> Documentação de Contexto</a></li>
<li><a href="docs/02-Especificação do Projeto.md"> Especificação do Projeto</a></li>
<li><a href="docs/03-Metodologia.md"> Metodologia</a></li>
<li><a href="docs/04-Projeto de Interface.md"> Projeto de Interface</a></li>
<li><a href="docs/05-Arquitetura da Solução.md"> Arquitetura da Solução</a></li>
<li><a href="docs/06-Template Padrão da Aplicação.md"> Template Padrão da Aplicação</a></li>
<li><a href="docs/07-Programação de Funcionalidades.md"> Programação de Funcionalidades</a></li>
<li><a href="docs/08-Plano de Testes de Software.md"> Plano de Testes de Software</a></li>
<li><a href="docs/09-Registro de Testes de Software.md"> Registro de Testes de Software</a></li>
<li><a href="docs/10-Plano de Testes de Usabilidade.md"> Plano de Testes de Usabilidade</a></li>
<li><a href="docs/11-Registro de Testes de Usabilidade.md"> Registro de Testes de Usabilidade</a></li>
<li><a href="docs/12-Apresentação do Projeto.md"> Apresentação do Projeto</a></li>
<li><a href="docs/13-Referências.md"> Referências</a></li>
</ol>

# Código

<li><a href="src/README.md"> Código Fonte</a></li>

# Apresentação

<li><a href="presentation/README.md"> Apresentação da solução</a></li>


🚀 Roadmap de Evolução do Jogo
🧩 Fase 1: Finalizar o núcleo do jogo
• 	[x] Movimento da nave
• 	[x] Asteroides com colisão e divisão
• 	[x] Tiros com cooldown e destruição
• 	[ ] Pontuação por destruição
• 	[ ] Tela de Game Over

💰 Fase 2: Mineração espacial
• 	[ ] Criar sprite  (pepitas de ouro)
• 	[ ] Sistema de coleta ao colidir com pepitas
• 	[ ] Variável  para rastrear progresso
• 	[ ] Estação espacial para “voltar à Terra”
• 	[ ] Conversão de ouro em Bitcoin (pontuação ou moeda)

🛰️ Fase 3: Detecção e defesa automatizada
• 	[ ] Implementar  para asteroides próximos
• 	[ ] Sistema de alerta visual ou sonoro
• 	[ ] Cálculo automático de direção do asteroide
• 	[ ] Disparo de raio laser automático
• 	[ ] Criar sprite  com alta velocidade e precisão

🧠 Fase 4: Inteligência e upgrades
• 	[ ] Sistema de upgrades (alcance, velocidade, dano)
• 	[ ] Interface de compra com Bitcoin acumulado
• 	[ ] Asteroides com comportamento inteligente (desviar, perseguir)
• 	[ ] Radar ou minimapa com objetos detectados

🌌 Fase 5: Mundo aberto e narrativa
• 	[ ] Múltiplos setores espaciais com transição
• 	[ ] Missões: minerar, defender, negociar
• 	[ ] História: nave em busca de recursos para salvar a Terra
• 	[ ] Sistema de reputação ou facções
