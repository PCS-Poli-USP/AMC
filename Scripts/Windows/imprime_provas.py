#####
# Imprime provas do PCS - Windows
# Autor: Fabio Levy Siqueira
# Data: 03/12/2015
#
# Programas necessarios
#   Ghostscript: http://ghostscript.com/download/
#   Gsview: http://pages.cs.wisc.edu/~ghost/gsview/
#
# Procedimento:
# 1) Instale o Ghostscript e o Gsview
# 2) Configure o driver da impressora para imprimir frente e verso e grampear
# 3) Chame o separa_provas.py para separar os arquivos
# 4) Execute este script
#####

# http://stackoverflow.com/questions/4469629/print-a-pdf-and-delete-the-file-when-printing-has-finished

import sys
import subprocess
import time
import os.path
import glob, os

print("")
print("Imprimindo provas")
print("---------------------------")
print("  Aperte Ctrl+C para pausar")
print("")

# Definicoes
IMPRESSORA = "Canon iR3235/iR3245 UFR II"
TEMPO_DE_ESPERA = 15 # 10 segundos
DIRETORIO_FINALIZADO = "impresso"

# Procurando o Gsview
locais = {"C:\\Program Files\\Ghostgum\\gsview\\gsprint.exe", "C:\\Program Files x86\\Ghostgum\\gsview\\gsprint.exe",  "C:\\Ghostgum\\gsview\\gsprint.exe"}
gsview = ""

for path in locais:
	if os.path.isfile(path):
		gsview = path
		break
if gsview == "":
	print("GSView nao encontrado.")
	print("Certifique-se que o Ghostscript e o Gsview estao instalados")
	sys.exit(1)

while True: # Necessario para usar o CTRL+C para pausar
	try:
		os.chdir(".")
		arquivosParaImprimir = sorted(glob.glob("sheet-[0-9][0-9][0-9][0-9].pdf")) # Formato xxxx.pdf
		if not arquivosParaImprimir:
			print("Sem arquivos para imprimir")
			input("Aperte ENTER para sair")
			sys.exit(1)
		else:
			# Criando a pasta para mover os arquivos
			if not os.path.exists(DIRETORIO_FINALIZADO):
				os.makedirs(DIRETORIO_FINALIZADO)
			
			for arquivo in arquivosParaImprimir:
				# Imprimindo
				p = subprocess.Popen([gsview, "-printer", IMPRESSORA, arquivo], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
				stdout, stderr = p.communicate() # espera o processo do gs terminar
				print(arquivo)
				os.rename(arquivo, DIRETORIO_FINALIZADO + "/" + arquivo)
				time.sleep(TEMPO_DE_ESPERA)
			print("")
			print("Finalizado com sucesso! Apague a pasta " + DIRETORIO_FINALIZADO)
			input("Aperte ENTER para sair")
			sys.exit(1)
	except KeyboardInterrupt:
		print("\nPausado (aperte ENTER para continuar ou 'q' para sair.)")
		try:
			response = input()
			if response == 'q':
				break
			print("Continuando...")
		except KeyboardInterrupt:
			print("Continuando")
			continue