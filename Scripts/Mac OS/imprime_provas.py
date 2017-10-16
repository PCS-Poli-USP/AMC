#####
# Imprime provas do PCS - Mac OS
# Autor: Fabio Levy Siqueira
#####
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
IMPRESSORA = "Canon_iR3235_PPD"
COMANDO = 'lpr -P'
OPCOES = '-o sides=two-sided-long-edge -o Staple=1PLU'

TEMPO_DE_ESPERA = 15 # 10 segundos
DIRETORIO_FINALIZADO = "impresso"

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
				p = subprocess.Popen(COMANDO + IMPRESSORA + OPCOES + " " + arquivo, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
				stdout, stderr = p.communicate() # espera o processo terminar
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