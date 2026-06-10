import json
import os
import sys
from datetime import datetime
from pathlib import Path


json_file = Path("database.json")

json_exist = json_file.exists()


def add():

    criar_tarefa = {
    "id": "",
    "description": "".join(sys.argv[3:]),
    "status": "todo",
    "createdAt": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "updatedAt": "",
}

    if not json_exist:
        with open(file=json_file, mode="w", encoding="utf-8") as f:
            criar_tarefa["id"] = 1

            dados_novos_criar = [criar_tarefa]

            json.dump(dados_novos_criar, f, indent=5, ensure_ascii=False)

            print("Task added successfully (ID: 1)")
    else:
        with open(file=json_file, mode="r", encoding="utf-8") as f:
            dados_json = json.load(f)

        todos_ids = []
        
        for task in dados_json:
            todos_ids.append(task["id"])

        ultimo_id = max(todos_ids) + 1
            
        criar_tarefa["id"] = ultimo_id

        dados_json.append(criar_tarefa)

        with open(file=json_file, mode="w", encoding="utf-8") as f:
            json.dump(dados_json, f, indent=5, ensure_ascii=False)
        print(f"Task added successfully (ID: {ultimo_id})")

def update():
    ref_id = int(sys.argv[3])

    new_description = "".join(sys.argv[4:])

    with open(file=json_file, mode="r", encoding="utf-8") as f:
        dados_json = json.load(f)
    
    for task in dados_json:   
        if task["id"] == ref_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            break
    else:
        print("Erro! O id digitado não existe.")

    with open(file = json_file, mode = "w", encoding = "utf-8") as f:
        json.dump(dados_json, f, indent = 5, ensure_ascii = False)


def delete():
    ref_id = int(sys.argv[3])

    with open(file=json_file, mode="r", encoding="utf-8") as f:
        dados_json = json.load(f)
    
    for task in dados_json:   
        if task["id"] == ref_id:
            dados_json.remove(task)
            break
    else:
        print("Erro! O id digitado não existe.")

    if len(dados_json) == 0:
        json_file.unlink()

    else:   
        with open(file = json_file, mode = "w", encoding = "utf-8") as f:
            json.dump(dados_json, f, indent = 5, ensure_ascii = False)

    
def change_task_status():
    ref_id = int(sys.argv[3])

    transalate = { "mark-in-progress":"in-progress",
                  "mark-done":"done"}
    








    

  
    new_status = transalate[sys.argv[2]]

   

    with open(file=json_file, mode="r", encoding="utf-8") as f:
        dados_json = json.load(f)
    
    for task in dados_json:   
        if task["id"] == ref_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            break
    else:
        print("Erro! O id digitado não existe.")

    with open(file = json_file, mode = "w", encoding = "utf-8") as f:
        json.dump(dados_json, f, indent = 5, ensure_ascii = False)


def list():
    if len(sys.argv) < 4:
        with open(file = json_file, mode = "r", encoding = "utf-8") as f:
            dados_json = json.load(f)
        print(json.dumps(dados_json, indent = 5, ensure_ascii = False))
        

    else:
        lista_parametros_aceitos = ["done", "todo", "in-progress"]

        list_type = sys.argv[3]

        specific_tasks = []     

        if list_type in lista_parametros_aceitos:

            with open(file = json_file, mode = "r", encoding = "utf-8") as f:
                dados_json = json.load(f)
        
            for task in dados_json:   
                if task["status"] == sys.argv[3]:
                    specific_tasks.append(task)
                
            if len(specific_tasks) > 0:
                print(json.dumps(specific_tasks, indent = 5, ensure_ascii = False))
            else:
                print("nao tem tasks com esse status")
        else:
            print("Erro! Comando list inexistente.")









def main():

    if sys.argv[2] == "add":
        add()
    else:
        if not json_exist:
            print("Erro! o arquivo database_json não existe.")

        else:
            if sys.argv[2] == "mark-in-progress" or sys.argv[2] ==  "mark-done":
                change_task_status()

            elif sys.argv[2] == "list":
                list()
        
        
            elif len(sys.argv) < 4:
                print("Erro, faltou incluir o id da task.")
            
            elif sys.argv[2] == "update":
                if len(sys.argv) < 5:
                    print("Erro, faltou incluir a descrição.")
                else:
                    update()

            elif sys.argv[2] == "delete":
                delete()







def verificar_argumentos():

    comandos_existentes = ["add","update","delete","mark-in-progress", "mark-done", "list" ]

    task_id_required = ["update","delete","mark-in-progress", "mark-done"]



    if len(sys.argv) < 2:
        print("Para rodar o programa, inclua o termo 'task-cli'. junto de 1 comando valido")
              
    elif sys.argv[1] != "task-cli":
         print("task-cli escrito errado")
        
    elif len(sys.argv) < 3:
        print("falta especificar um comando apos task-cli")
        
    elif sys.argv[2] not in comandos_existentes:
        print("Comando nao reconhecido, tente utilizar esses: 'add','update','delete','mark-in-progress', 'mark-done', 'list'")
    
    elif sys.argv[2] in task_id_required:
        if len(sys.argv) < 4:
            print("faltou indicar o id da task")

        elif not sys.argv[3].isdigit():
            print("id nao existe, digite um numero inteiro")
        
        else:
            main()
    
    
    
    
    
    
    
    
    
    else:
        main()
 
verificar_argumentos()