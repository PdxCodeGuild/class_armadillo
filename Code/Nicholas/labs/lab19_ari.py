#In lab 20 we sorted through a body of text to count sentences, words, and letters.  With this data we calculate the Automated Readability Index(ARI)
import requests
#dictionary for ARI scores and corresponding reading levels
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
#imports text using requewat
response = requests.get('https://www.gutenberg.org/files/25344/25344-0.txt')

text = response.text
#splits lines and chops unnecessary text at beginning and end of text     
lines = text.split('\n')
text = lines[244:8722]

#sentence count
period_count = response.text.count('.') #counts punctuation to count the number of sentences, this is a very crude way to count sentences.
question_count = response.text.count('?')
exclamation_count = response.text.count('!')
sentence_count = int(period_count + question_count + exclamation_count) #adds the punctuation together to total sentences

#filter out special characters once sentences are counted
for char in text:  
    if char in '[]()@$%*-.?!,\'/:1234567890': #if nums and special characters within text:
        text=text.replace(char,' ') #replace with blank space

#word count
words = len(response.text.split()) #gets word count of text split into list

# characters count
chars = 0  
for char in response.text.strip():  
    chars += 1 #counts characters, removes blank space 


ARI_calc = 4.71 * (chars/words) + 0.5 * (words/sentence_count) - 21.43 #ARI formula
if ARI_calc >= 14: #Since ARI score is greater than 14, round down to 14
    ARI_score =14

#print totals here:
print("The Scarlet Letter by Nathaniel Hawthorne contains approximately: ")  
print(f"{sentence_count} sentences")
print(f"{words} words")
print(f"{chars} characters")    
print(f'---------------------------------------------- ')
print(f"The ARI for The Scarlet Letter is {ARI_score}")  #Pulls from rounded ARI score
print(f"This corresponds to a {ari_scale[ARI_score]['grade_level']} level of difficulty.")  #Pulls from ARI scale dictionary key: grade level
print(f"That is suitable for an average person {ari_scale[ARI_score]['ages']} years old.")  #Pulls from ARI scale dictionary key: ages