#課題1
import json
with open('data/sensor.json', 'r', encoding='utf-8_sig') as f:
    df=json.load(f)
    print("accel")
    print(df['sensordata']['accel'])
    print("light")
    print(df['sensordata']['light'])
    print("touch")
    print(df['sensordata']['touch'][0]['x'],df['sensordata']['touch'][0]['y'])
    print(df['sensordata']['touch'][1]['x'],df['sensordata']['touch'][1]['y'])
    print(df['timestamp'])