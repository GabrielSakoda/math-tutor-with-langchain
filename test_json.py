from math_tutor import virtual_math_teacher
import json

entry_json = json.dumps({"pergunta": "Resolva a equação 2x+3=7"})

answer_json = virtual_math_teacher(entry_json)

print(json.loads(answer_json)) 