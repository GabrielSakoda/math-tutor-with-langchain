from math_tutor import virtual_math_teacher
import json

entry_json = json.dumps({"pergunta": "Qual é a fórmula de bhaskara?"})

answer_json = virtual_math_teacher(entry_json)

print(json.loads(answer_json)) 