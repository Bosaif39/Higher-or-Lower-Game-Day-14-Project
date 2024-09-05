data_list = [
    {'name': 'John Doe', 'number':  4567, 'job': 'Software Engineer'},
    {'name': 'Jane Smith', 'number': 5678, 'job': 'Data Scientist'},
    {'name': 'Emily Johnson', 'number': 6789, 'job': 'Graphic Designer'},
    {'name': 'Michael Brown', 'number': 7890, 'job': 'Marketing Manager'},
    {'name': 'Sarah Davis', 'number': 8901, 'job': 'Product Manager'}
]

import random

cha=random.choice(data_list)
chb=random.choice(data_list)
print("Higher or lower?")

tr=1

while(tr>0):
    print(f" A is {cha['name']}, {cha['job']}")
    print(f" B is {chb['name']}, {chb['job']}")
    i=input(f"who i higher? a or b?:")
    if(i=='a' and cha['number']>chb['number']):
        tr=tr+1
    elif(i=='b' and chb['number']>cha['number']):
        tr=tr+1
    else:
        break
     