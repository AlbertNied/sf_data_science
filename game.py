'''Erraten Sie die Zahl'''

import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count +=1
    predict_number = int(input('Errate die Zahl von 1 bis 100: 50'))
    
    if predict_number > number:
        print('Die Zahl ist zu groß')
        
    elif predict_number < number:
        print('Die Zahl ist zu klein')
        
    else:
        print(f'Sie haben die Zahl = {number} in {count} Versuche erraten')
        break # Das Spiel endet hier
        