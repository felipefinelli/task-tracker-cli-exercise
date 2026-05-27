import sys
import json
import os
from pathlib import Path
from datetime import datetime

arquivo_json = Path("database.json")

hora_atual = datetime.now()


if not arquivo_json.exists():
    dados_criar_json = {
        "id":1,
        "description":"",
        "status":"todo",
        "createdAt":hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        ,"updatedAt":""
        }
    with open(arquivo_json, "w", encoding = "utf-8") as f:
        json.dump(dados_criar_json, f, indent = 5, ensure_ascii = False) 














