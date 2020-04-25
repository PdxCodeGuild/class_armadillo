import json
from Code.bobby import contact_list

# function to add to JSON 
def write_json(data, filename='contact_list.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 
      
      
with open('contact_list.json') as json_file: 
    data = json.load(contact_list.json) 
      
    temp = data['emp_details'] 
  
    # python object to be appended 
    while True:
        command = input("What is Your Command? ")
        if command in ["done", "exit", "quite"]:
            break
        elif command == "create":
            name = input("Name: ")
            age = int(input("Age: "))
            email = input("Email Adress: ")
            fav_color = input("Favorite Color: ")
        contacts = {
            "Name" : name,
            "Age" : age,
            "Email Adress" : email,
            "Favorite Color" : fav_color,

        } 
  
  
    # appending data to emp_details  
    temp.append(contacts) 
      
write_json(data)  