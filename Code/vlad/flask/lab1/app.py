# to run flask I need to enter the following in the terminal each time:  python3 -m flask run
# I may need to = export FLASK_ENV=development
# this will tell me which servers are running = ps -fA | grep python
# to change the port= export FLASK_RUN_PORT=5500
# I have the following error when trying to control z in the terminal = OSError: [Errno 48] Address already in use


from flask import Flask, render_template, request # I need to enter after the coma render_template to be able 
#connect index html to the browser
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] ) # localhost:5000/
def rotc13():
        # Lab 15: ROT Cipher Version 2
    #Allow the user to input the amount of rotation used in the encryption. (ROTN)
    word = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        index =    ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
        rot13 =    ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
        rotation = int(request.form['rotation'])
        print(request.form)
        print(user_input,rotation)
    
        # user_input = 'hello' #input('Enter any word: ')
        
        # print(alphabet.index('c'))
        # print(rot13[4])
        for letter in user_input: 
            x = (alphabet.index(letter) + rotation) % 26 #
            # print(alphabet[x])
            print(x)  
            word += alphabet[x]
            # print(index_letter)
            # print(rot13[index_letter])
        print(word)
    return render_template('index.html', word = word) # this is setting my key word argument
    
