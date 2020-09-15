'''
Task 2. https://repl.it/@zhukov/WindingRoughApi#main.py
'''

import requests as req
r = req.get('http://api.openweathermap.org/data/2.5/weather?q={Saint-Petersburg,ru}&appid={bf3e830b2046f4f7ef63ff2ca100c632}')
print(r.json())