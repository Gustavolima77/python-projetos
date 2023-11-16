print('=' * 30)
print('{:^30}'.format('Banco'))
print('=' * 30)
valor = int(input('Que valor voce quer sacar? R$'))
total = valor
cedulas = 100
totcéd = 0
while True:
  if total >= cedulas:
    total -= cedulas
    totcéd += 1
  else:
    if totcéd >0:
      print(f'Total de {totcéd} cedulas de R${cedulas}')
    if cedulas == 100:
      cedulas = 20
    elif cedulas == 20:
      cedulas = 10
    elif cedulas == 10:
      cedulas = 1
      totcéd = 0
    if total == 0:
      break
print('=' * 30)
print('Volte sempre ao Banco')