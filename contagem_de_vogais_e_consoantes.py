palavaras = ('python', 'programar', 'linguagem', 'python')

for p in palavaras:
  print(f'\nNa palavra {p} temos ', end='')
  for letra in p:
    if letra.lower() in 'aeiou':
      print(letra, end=' ')