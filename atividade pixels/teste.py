# coding: utf-8
# Atividade Complementar
# Iann Carvalho, 2016 / Introdução à computação

from PIL import Image
import sys
print """
==================PRECAUÇÕES INICIAIS====================
01. Caso o PIL não esteja instalado no seu computador,
instale-o com o comando "sudo pip install pillow" no 
terminal do linux.
02. A imagem deve estar na mesma pasta que o arquivo.py
03. O arquivo deve ser descrito na entrada com o seu nome
e seu formato, a exemplo: "nomedoarquivo.png"
=========================================================
"""
img = raw_input('Qual o nome da imagem que você deseja negativar? ')
image = Image.open(img)

w, h = image.size

for i in range(w):
  for j in range(h):
    cor = image.getpixel((i, j))
    if cor == (0, 0, 0):
      cor = (255, 255, 255)
    elif cor == (255, 255, 255):
      cor = (0, 0, 0)
    image.putpixel((i, j), cor)

image.show()
