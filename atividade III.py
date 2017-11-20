# coding: utf-8
# Iann Carvalho, 2016 / Introdução à computação
# Atividade III

# Entrada
tipo=raw_input('Qual tipo de código você vai usar? ')
caractere=(raw_input('Qual seu caractere? '))

#conversão
tipo=str.lower(tipo)

# Condição
if tipo==("decimal"):
	caractere=int(caractere)
	binario = bin(caractere)[2:]
	hexadecimal = hex(caractere)[2:]
	print 'O(s) caractere(s) "%s" em %s, corresponde(m) ao(s) caractere(s) "%s" em binário' % (caractere, tipo, binario)
	print 'O(s) caractere(s) "%s" em %s, corresponde(m) ao(s) caractere(s) "%s" em hexadecimal' % (caractere, tipo, hexadecimal)
elif tipo==("binário") or tipo==("binario"):
	decimal=int(caractere, 2)
	print 'O(s) caractere(s) "%s" em %s, corresponde(m) ao(s) caractere(s) "%s" em decimal' % (caractere, tipo, decimal)
	decimal=str(decimal)
	hexadecimal=int(decimal, 16)
	print 'O(s) caractere(s) "%s" em %s, corresponde(m) ao(s) caractere(s) "%s" em hexadecimal' % (caractere, tipo, hexadecimal)
elif tipo==("hexadecimal"):
	decimal=int(caractere, 16)
	print 'O(s) caractere(s) "%s" em %s, corresponde(m) ao(s) caractere(s) "%s" em decimal' % (caractere, tipo, decimal)
	binario=bin(int(caractere, 16))[2:].zfill(8)
	print 'O(s) caractere(s) "%s" em %s, corresponde(m) ao(s) caractere(s) "%s" em binário' % (caractere, tipo, binario)	
else:
	print "Tipo de sistema desconhecido"
