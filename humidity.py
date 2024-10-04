import pandas as pd

data={
    'day':[1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14],
    'outlook':['sunny',	'sunny',	'overcast', 	'rain',	'rain',	'rain',	'overcast', 	'sunny',	'sunny',	'rain',	'sunny',	'overcast', 	'overcast', 	'rain'],
    'temp':['hot',	'hot',	'hot',	'mild',	'cool',	'cool',	'cool',	'mild',	'cool',	'mild',	'mild',	'mild',	'hot',	'mild'],
    'humidity':['high',	'high',	'high',	'high',	'high',	'normal',	'normal',	'normal',	'high',	'normal',	'normal',	'high', 	'normal',	'high'],
    'wind':['weak',	'strong',	'weak',	'weak',	'weak',	'strong',	'strong',	'weak',	'weak',	'weak',	'strong',	'strong',	'weak',	'strong'],
    'play':['no',	'no',	'yes',	'yes',	'yes',	'no',	'yes',	'no',	'yes',	'yes',	'yes',	'yes',	'yes',	'no']
}
df=pd.DataFrame(data)


day_counts=df['day'].value_counts()
sunny_counts=df['outlook'].value_counts()
temp_counts=df['temp'].value_counts()
humidity_counts=df['humidity'].value_counts()
wind_counts=df['wind'].value_counts()
play_counts=df['play'].value_counts()
print(day_counts)
print(sunny_counts)
print(temp_counts)
print(humidity_counts)
print(wind_counts)
print(play_counts)
