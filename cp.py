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
import docker
import pexpect


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
12 = Kill imagem
13 = Lista processos no container
14 = Entra dentro do container para obter dados
15 = Ping""")
solucao = int(input("\nAção que deseja: "))

# Executa o comando no shell
# Verifica se a execução foi bem-sucedida

if 1<= solucao <= 15:                                                                    # Para limitar o número que pode ser inserido
    if solucao==1:                                                                       # Define o que será feito a partir de cada número
        c_lista ="docker ps -a"                                                          # Comando que será executado no docker
        listagem = subprocess.run(c_lista, shell=True, capture_output=True, text=True)   # Executa o comando no bash e retorna a resposta
        if listagem.returncode == 0:
            print("Saída do comando:")
            print(listagem.stdout)
        else:
            print("Erro ao executar o comando:")
            print(listagem.stderr)


    if solucao==2:                                                                       # Define o que será feito a partir de cada número
        nm_con_c=str(input("Nome do container: "))                                       # Define o nome do container
        nm_image=str(input("Nome da imagem: "))                                          # Para escolher a imagem que vai rodar(ex. Ubuntu, nginx)
        c_criar = "sudo docker run --name {} -d -p 2375 {}".format(nm_con_c, nm_image)   # Comando que será executado no docker
        criacao = subprocess.run(c_criar, shell=True, capture_output=True, text=True)    # Executa o comando no bash e retorna a resposta
        if criacao.returncode == 0:
            print("Saída do comando: ")
            print(criacao.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(criacao.stderr)

    if solucao==3:                                                                       # Define o que será feito a partir de cada número
        nm_con_r=str(input("Nome do container: "))                                       # Define o container que será apagado
        c_remover = "sudo docker rm {}".format(nm_con_r)                                 # Comando que será executado no docker
        remover = subprocess.run(c_remover, shell=True, capture_output=True, text=True)  # Executa o comando no bash e retorna a resposta
        if remover.returncode == 0:
            print("Saída do comando: ")
            print(remover.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(remover.stderr)

    if solucao==4:                                                                       # Define o que será feito a partir de cada número
        nm_con_s=str(input("Nome do container: "))                                       # Define o container que será iniciado
        c_start="sudo docker start {}".format(nm_con_s)                                  # Comando que será executado no docker
        start = subprocess.run(c_start, shell=True, capture_output=True, text=True)      # Executa o comando no bash e retorna a resposta
        if start.returncode == 0:
            print("Saída do comando: ")
            print(start.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(start.stderr)

    if solucao==5:                                                                       # Define o que será feito a partir de cada número
        nm_con_stop=str(input("Nome do container: "))                                    # Define o container que será parado
        c_stop="sudo docker stop {}".format(nm_con_stop)                                 # Comando que será executado no docker
        stop = subprocess.run(c_stop, shell=True, capture_output=True, text=True)        # Executa o comando no bash e retorna a resposta
        if stop.returncode == 0:
            print("Saída do comando: ")
            print(stop.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(stop.stderr)

    if solucao==6:                                                                       # Define o que será feito a partir de cada número
        nm_con_restart=str(input("Nome do container: "))                                 # Define o container que será 'restartado'
        c_restart="sudo docker restart {}".format(nm_con_restart)                        # Comando que será executado no docker
        restart = subprocess.run(c_restart, shell=True, capture_output=True, text=True)  # Executa o comando no bash e retorna a resposta
        if restart.returncode == 0:
            print("Saída do comando: ")
            print(restart.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(restart.stderr)

    if solucao==7:                                                                       # Define o que será feito a partir de cada número
        nm_con_logs=str(input("Nome do container: "))                                    # Define o container que pegará os logs
        c_logs="sudo docker logs {}".format(nm_con_logs)                                 # Comando que será executado no docker
        logs = subprocess.run(c_logs, shell=True, capture_output=True, text=True)        # Executa o comando no bash e retorna a resposta
        if logs.returncode == 0:
            print("Saída do comando: ")
            print(logs.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(logs.stderr)

    if solucao==8:                                                                       # Define o que será feito a partir de cada número
        nm_con_kill=str(input("Nome do container: "))                                    # Define o container que será morto
        c_kill="sudo docker kill {}".format(nm_con_kill)                                 # Comando que será executado no docker
        kill = subprocess.run(c_kill, shell=True, capture_output=True, text=True)        # Executa o comando no bash e retorna a resposta
        if kill.returncode == 0:
            print("Saída do comando: ")
            print(kill.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(kill.stderr)

    if solucao==9:                                                                       # Define o que será feito a partir de cada número
        c_images="sudo docker images"                                                    # Comando que será executado no docker
        images = subprocess.run(c_images, shell=True, capture_output=True, text=True)    # Executa o comando no bash e retorna a resposta
        if images.returncode == 0:
            print("Saída do comando: ")
            print(images.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(images.stderr)

    if solucao==10:                                                                       # Define o que será feito a partir de cada número
        c_info="sudo docker info"                                                         # Comando que será executado no docker
        info = subprocess.run(c_info, shell=True, capture_output=True, text=True)         # Executa o comando no bash e retorna a resposta
        if info.returncode == 0:
            print("Saída do comando: ")
            print(info.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(info.stderr)

    if solucao==11:                                                                       # Define o que será feito a partir de cada número
        c_version="sudo docker version"                                                   # Comando que será executado no docker
        version = subprocess.run(c_version, shell=True, capture_output=True, text=True)   # Executa o comando no bash e retorna a resposta
        if version.returncode == 0:
            print("Saída do comando: ")
            print(version.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(version.stderr)

    if solucao==12:                                                                       # Define o que será feito a partir de cada número
        nm_con_kimg=str(input("Nome da imagem: "))                                        # Define a imagem que será morta
        c_kimg="sudo docker rmi {}".format(nm_con_kimg)                                   # Comando que será executado no docker
        kimg = subprocess.run(c_kimg, shell=True, capture_output=True, text=True)         # Executa o comando no bash e retorna a resposta
        if kimg.returncode == 0:
            print("Saída do comando: ")
            print(kimg.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(kimg.stderr)
    
    if solucao==13:                                                                       # Define o que será feito a partir de cada número
        nm_con_proc=str(input("Nome do container: "))                                     # Define o container que terá seus processos listados 
        c_proc="sudo docker top {}".format(nm_con_proc)                                   # Comando que será executado no docker
        proc = subprocess.run(c_proc, shell=True, capture_output=True, text=True)         # Executa o comando no bash e retorna a resposta
        if proc.returncode == 0:
            print("Saída do comando: ")
            print(proc.stdout)
        else:
            print("Erro ao executar o comando: ")
            print(proc.stderr)            


    if solucao == 14:                                                                       # Define o que será feito a partir de cada número
        nm_con_entrar = str(input("Nome do container: "))                                   # Nome do container que quer entrar
        c_entrar = "sudo docker exec -it {} /bin/bash".format(nm_con_entrar)                # Executa o comando no bash e permite o acesso ao container

        try:
            child = pexpect.spawn(c_entrar)
            child.interact()
        except pexpect.exceptions.ExceptionPexpect as e:
            print("Erro ao executar o comando:")
            print(str(e))

    if solucao == 15:                                                                       # Define o que será feito a partir de cada número
        nm_con_ping = str(input("Nome do container: "))                                     # Nome do container que deseja 'pingar'
        c_ip_ping = "docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' " + nm_con_ping
        c_ip_ping_output = subprocess.check_output(c_ip_ping, shell=True, text=True               # Aqui são executados dois comandos no bash
        c_ip_ping_output = c_ip_ping_output.strip()                                               # o primeiro pega o IP do container
        c_ping = "docker exec -it {} curl {}".format(nm_con_ping, c_ip_ping_output)               # o segundo usa o curl, para verificar a conexão
        try:
            ping = subprocess.run(c_ping, shell=True, capture_output=True, text=True, check=True)
            print("Saída do comando:")
            print(ping.stdout)

        except subprocess.CalledProcessError as e:
            print("Erro ao executar o comando:")
            print(e.stderr)


else:
    print('Por favor insira uma opção válida')
