from datetime import datetime
# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.


from datetime import datetime

nome = input('Qual o seu nome? ').title()
ano_corrente = datetime.now().year
linkedIn_ano = int(input('Qual o nao que conheceu o linkedIn? '))
cursos_input = input('Quais cursos realizados?(separe por virgula) ')
cursos = cursos_input.split(',') #separa a string em partes usando virgula como separador
cursos = [cursos.strip().title() for cursos in cursos] #strip - remove espaços em branco 
total_anos = ano_corrente - linkedIn_ano
total_cursos = ()
primeiro_curso = cursos[0]
ultimo_curso = cursos[-1] 

estudante = {
  'nome': nome,
  'linkedIn_ano': linkedIn_ano,
  'cursos': cursos,
  'total_anos': total_anos,
  'total_curso': len(cursos),
  'primeiro_curso': primeiro_curso,
  'ultimo_curso': ultimo_curso
}
print(estudante)


