#!/usr/bin/env python

import pprint
import sys
import yaml
import json

List1 = []

for item in range(3):
	List1.append(item)

dic1 = {'test':range(5), 'booger':['snot', 'nose']}
List1.append(dic1)

with open('test.yml', 'w') as file:
	file.write(yaml.dump(List1, default_flow_style=False))

with open('test.json', 'w') as file:
	json.dump(List1, file)
