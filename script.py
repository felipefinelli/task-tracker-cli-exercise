import os
import sys
import json
from pathlib import Path
from datetime import datetime




json_file = Path("database.json") #definindo o caminho pro python checar



hora_atual = datetime.now()  #pega valor atual


dados_novos = {      # dados a ser lançados, note que o id está vazio e ainda nao é uma lista.
        "id": "",            
        "description": "".join(sys.argv[3:]),
        "status": "todo",
        "createdAt":hora_atual.strftime("%d/%m/%Y %H:%M"),
        "updatedAt": ""
        }





def add():

        #se o arquivo json nao existir.
        if not json_file.exists():  
                
                
                #abre no modo "w" de write, para escrever/criar o arquivo json.
                with open(file = json_file, mode = "w", encoding = "utf-8") as f:

                        #muda o id para 1 ja que sera a primeira tarefa.
                        dados_novos["id"] = 1      
                        
                        # cria a lista que vai abrigar os dicionarios
                        dados_novos_criar = [dados_novos]   

                        #deposita a primeira task.
                        json.dump(dados_novos_criar, f, indent = 5, ensure_ascii = False)
        
        
        
        
        
        

        #se o arquivo json já existir. Nesse caso vamos precisar "refazer" o json todo.
        else:
                
                #abrimos no modo "r" de read, para pegarmos os dados do json atual para carregar no python.
                #nao da pra escrevermos direto no arquivo sem estragar a estrutura de 
                #dicionario e lista do nosso arquivo json.
                with open(file = json_file, mode = "r", encoding = "utf-8") as f:
                        
                        #criando variavel que vai representar os dados carregados no python.
                        json_carregado = json.load(f)
                        
                        #vendo a quantidade de tasks existentes para saber qual vai ser o id da task atual.
                        ultimo_id = len(json_carregado) + 1

                        #inserindo o id correto da task que sera lançada
                        dados_novos["id"] = ultimo_id

                        #adicionando nossa nova task nos dados carregados do json.
                        json_carregado.append(dados_novos)

                        #por fim vamos utilizar o "w" de write para sobreescrever o arquivo json atual
                        #com nossa nova task ja inclusa.
                        with open(file = json_file, mode = "w", encoding = "utf-8") as f:
                                json.dump(json_carregado, f, indent = 5, ensure_ascii = False)








def update():
    print("dummy")
def delete():
    print("dummy")
def loop():
    print("dummy")
def list():
    print("dummy")
def mark_in_progress():
    print("dummy")
def mark_done():
    print("dummy")







def main():
    
    if sys.argv[2] == "add":
        add()
   
    elif sys.argv[2] == "update":
        update()
    
    elif sys.argv[2] == "delete":
        delete()
   
    elif sys.argv[2] == "mark-in-progress":
        mark_in_progress()
    
    elif sys.argv[2] == "mark-done":
        mark_done()
   
    elif sys.argv[2] == "list":
        list()
    
    else:
        loop()

main()