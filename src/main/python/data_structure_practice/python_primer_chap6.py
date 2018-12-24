####
####
####
#### Python Pocket Primer -
#### Exercises for chapter six
####
####
####

import sys
import json
from collections import OrderedDict

data = OrderedDict({'one':'1','two':'2','three':'3'})

json_encoded = json.dumps(data, sort_keys=False)
json_decoded = json.loads(json_encoded)

print('encoded', json_encoded)
print('decoded', json_decoded)

print(type(json_decoded['two']))
