import random
#list of possible weather conditions
weather = ['thunderstorms', 'tornado watch', 'hot and humid', 'rainy', 'blizzard', 'windy', 'sunny and 65', 'wintery mix', 'cold and dry', 'sweater weather']
#provides a greeting and then asks a question, any answer to question provides output here    
print("Welcome to the wild Midwest weather predictor!")
input("Ask me how the weather is gonna be tomorrow, I'll bet you I get it right! ")
#if user enters anything except "done", loops back to this point
alt_weather = True
while alt_weather:
#random weather condition outputs here
    print("Tomorrow the weather will be:")
    print(random.choice(weather))
#entering done breaks loop 
    other_weather = input("Not satified with my prediction? Ask again or say 'done' if satisfied: ").lower()
    if other_weather == 'done':
        print('Have a great day!')
        break