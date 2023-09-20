'''
Turma 1TDCG
Professor: Fabio Cabrini
Integrantes:
Danilo da Gama Campos, RM99680
Eduardo do Nascimento Silva, RM99225
Gustavo Duarte Bezerra da Silva, RM99774
Henrique Batista de Souza, RM99742
'''

import subprocess

print("""1 = Listagem
2 = Criação
3 = Remoção
4 = Start container
5 = Stop container
6 = Restart container
7 = Logs
8 = Kill container
9 = Imagens
10 = Informações
11 = Versão
12 = Kill imagem""")
solucao = int(input("Ação que deseja: "))

# Executa o comando no shell
# Verifica se a execução foi bem-sucedida

if solucao==1:
    c_lista ="sudo docker ps -a"  
    listagem = subprocess.run(c_lista, shell=True, capture_output=True, text=True)
    if listagem.returncode == 0:
        print("Saída do comando:")
        print(listagem.stdout)
    else:
        print("Erro ao executar o comando:")
        print(listagem.stderr)


if solucao==2:
    nm_con_c=str(input("Nome do container: "))
    nm_image=str(input("Nome da imagem: "))
    c_criar = "sudo docker run --name {} -d -p 2375 {}".format(nm_con_c, nm_image)
    criacao = subprocess.run(c_criar, shell=True, capture_output=True, text=True)
    if criacao.returncode == 0:
        print("Saída do comando: ")
        print(criacao.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(criacao.stderr)

if solucao==3:
    nm_con_r=str(input("Nome do container: "))
    c_remover = "sudo docker rm {}".format(nm_con_r)
    remover = subprocess.run(c_remover, shell=True, capture_output=True, text=True)
    if remover.returncode == 0:
        print("Saída do comando: ")
        print(remover.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(remover.stderr)

if solucao==4:
    nm_con_s=str(input("Nome do container: "))
    c_start="sudo docker start {}".format(nm_con_s)
    start = subprocess.run(c_start, shell=True, capture_output=True, text=True)
    if start.returncode == 0:
        print("Saída do comando: ")
        print(start.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(start.stderr)

if solucao==5:
    nm_con_stop=str(input("Nome do container: "))
    c_stop="sudo docker stop {}".format(nm_con_stop)
    stop = subprocess.run(c_stop, shell=True, capture_output=True, text=True)
    if stop.returncode == 0:
        print("Saída do comando: ")
        print(stop.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(stop.stderr)

if solucao==6:
    nm_con_restart=str(input("Nome do container: "))
    c_restart="sudo docker restart {}".format(nm_con_restart)
    restart = subprocess.run(c_restart, shell=True, capture_output=True, text=True)
    if restart.returncode == 0:
        print("Saída do comando: ")
        print(restart.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(restart.stderr)

if solucao==7:
    nm_con_logs=str(input("Nome do container: "))
    c_logs="sudo docker logs {}".format(nm_con_logs)
    logs = subprocess.run(c_logs, shell=True, capture_output=True, text=True)
    if logs.returncode == 0:
        print("Saída do comando: ")
        print(logs.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(logs.stderr)

if solucao==8:
    nm_con_kill=str(input("Nome do container: "))
    c_kill="sudo docker kill {}".format(nm_con_kill)
    kill = subprocess.run(c_kill, shell=True, capture_output=True, text=True)
    if kill.returncode == 0:
        print("Saída do comando: ")
        print(kill.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(kill.stderr)

if solucao==9:
    c_images="sudo docker images"
    images = subprocess.run(c_images, shell=True, capture_output=True, text=True)
    if images.returncode == 0:
        print("Saída do comando: ")
        print(images.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(images.stderr)

if solucao==10:
    c_info="sudo docker info"
    info = subprocess.run(c_info, shell=True, capture_output=True, text=True)
    if info.returncode == 0:
        print("Saída do comando: ")
        print(info.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(info.stderr)

if solucao==11:
    c_version="sudo docker version"
    version = subprocess.run(c_version, shell=True, capture_output=True, text=True)
    if version.returncode == 0:
        print("Saída do comando: ")
        print(version.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(version.stderr)

if solucao==12:
    nm_con_kimg=str(input("Nome da imagem: "))
    c_kimg="sudo docker rmi {}".format(nm_con_kimg)
    kimg = subprocess.run(c_kimg, shell=True, capture_output=True, text=True)
    if kimg.returncode == 0:
        print("Saída do comando: ")
        print(kimg.stdout)
    else:
        print("Erro ao executar o comando: ")
        print(kimg.stderr)
