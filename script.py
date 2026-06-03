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


def update():
    if not json_exist:
         print("Erro! o arquivo database_json não existe.")

    else:
        ref_id = int(sys.argv[3])

        new_description = "".join(sys.argv[4:])

        with open(file=json_file, mode="r", encoding="utf-8") as f:
            dados_json = json.load(f)
        
        
        
        
        #"elemento" representa cada dicionario dentro da lista dados_json.
        #vai checar o "id" de cada um e se o id for = ao ref_id, vai atualizar alguns dados
        # e depois o break vai fazer com que pare a iteracao e ao mesmo tempo evite com que o
        #bloco else rode.   For + Else é algo compativel.

        #
        
        for elemento in dados_json:   
            if elemento["id"] == ref_id:
                elemento["description"] = new_description
                elemento["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                break
        else:
            print("Erro! O id digitado não existe.")

        with open(file = json_file, mode = "w", encoding = "utf-8") as f:
            json.dump(dados_json, f, indent = 5, ensure_ascii = False)

































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
        if len(sys.argv) < 4:
            print("Erro, faltou incluir a descrição.")
        else:
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