peso = float(input('qual e seu peso? (kG) '))
altura = float(input('Qual e sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa e de {:.1f}'.format(imc))

if imc < 18.5:
  print('Voce esta abaixo do peso normal')
elif 18.5 <= imc <25:
 print('parabens, você esta na faixa de peso normal')
elif 25 <= imc < 30:
  print('Você esta em sobrepeso')
elif 30 <= imc <40:
  print('Você esta em obesidade!')
elif imc >= 40:
  print('Você esta em obesidade grave')

