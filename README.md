# Aplicação de Sistema Lineares na Construção Civil

Este projeto tem como objetivo demonstrar a aplicação de sistemas lineares na resolução de problemas  reais na construção civil, utilizando a linguagem python. 

# Descrição

O programa desenvolvido permite calcular o quantitativo demateriais utilizados em uma obra, considerando dois tipos de alvenaria:
- Alvenaria convencional
- Alvenaria estrutural

A partir da área total da construção e da quantidade total de blocos, o sistema linear é utilizado para determinar a distribuição das áreas entre os dois tipos de alvenaria.

# Funcionamento

O modelo matemático utilizado é baseado no seguinte sistema linear:
- x + y = área total
- 13x + 15y = quantidade de blocos

Onde:
- x -> área de alvenaria convencional
- y -> área de alvenaria estrutural

- Após a resolução do sistema, o programa calcula:
- Quantidade de blocos
- Volume de argamassa
- Volume de graute (apenas alvenaria estrutural)

# Classificação do Sistema
  O código também realiza a classificação do sistema em:
  - Sistema Possível e Determinado (SPD)
  - Sistema Possível e Indeterminado (SPI)
  - Sistema Impossível (SI)
 
  Utilizando o determinante e o posto das matrizes.

  # Tecnologias Utilizadas
  - Python
  - Biblioteca Numpy

# Objetivo Acaddêmico
Este projeto foi desenvolvido como atividade da disciplina de Álgebra Linear, com o objetivo de integrar:
- Conceitos matemáticos
- Modelagem de problemas reais

# Aplicação prática
O trabalho demonstra como a matemática pode ser utilizada para:
- Planejamento de materiais
- Redução de desperdícios
- Apoio à tomada de decisão na construção civil

# Autora
projeto desenvolvido por Alessandra Aguiary 
  
