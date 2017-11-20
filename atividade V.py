# coding: utf-8

print "---------------------------------Passo 1----------------------------------------"
print "Primeiramente para que consigamos fazer isso temos que ter um número grande na faixa de 2 ^ 512 e 2 ^ 1023, para que não haja overflow."
while True:
	exp1 = float(raw_input('Digite o número do expoente que esteja entre 512 e 1023: '))
	if (512)<=exp1<=(1023):
		break

print "---------------------------------Passo 2----------------------------------------"

print "Depois para que consigamos fazer isso temos que ter um número pequeno na faixa de 2 ^ -512 e 2 ^ -1074."
while True:
	exp2 = float(raw_input('Digite o número do expoente que esteja entre -512 e -1074: '))
	if (-512)>=exp2>=(-1023):
		break
		
print "---------------------------------Passo 3----------------------------------------"
numero1 = 2 ** exp1
numero2 = 2 ** exp2
print "Seu primeiro número 1 é 2 ^ %d" % exp1
print "Seu primeiro número 1 é 2 ^ %d" % exp2

print "---------------------------------Passo 4----------------------------------------"
print "A)  (2 ^ %d) / (2 ^ %d) = %.f" % (exp1, exp2, numero1/numero2)
print "B)  -(2 ^ %d) / (2 ^ %d) = %.f" % (exp1, exp2, (-numero1)/numero2)
print "C)  ( (2 ^ %d) / (2 ^ %d) ) / ( (2 ^ %d) / (2 ^ %d) ) = %.f" % (exp1, exp2, exp1, exp2, (numero1/numero2)/(numero1/numero2))

print "--------------------------------EXPLICAÇÃO--------------------------------------"
print "Em A: Conclui-se que é possível chegar ao infinito pela divisão de um número muito grande e outro muito pequeno."
print "Em B: Conclui-se que é possível chegar ao infinito negativo pela divisão de um número muito grande e outro muito pequeno, um dos dois sendo negativo."
print "Em C: Conclui-se que é possível chegar a uma ideterminção através da divisão de dois infinitos."
