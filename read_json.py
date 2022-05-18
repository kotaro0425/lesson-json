import json

with open('data/test.json', 'r', encoding='utf-8_sig') as f:
    df = json.load(f)
    print(df)
    #print('---A---')
    #print(df['A'])
    #print(df['A']['i'])
    #print('---B---')
    #print(df['B'])
    #print(df['B'][0])
    #print(df['B'][0]['X'])
    print(df['C'])
    