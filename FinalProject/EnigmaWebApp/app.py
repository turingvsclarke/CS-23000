from bottle import route, run, template, request, post, get, error

@get('/')
def EnigmaMenu():
    return template('Menu.html')

# This page will take us to a page that will get input from the user for encrypting the message. Eventually it will also have @post because it will need to know which Enigma to use.
@get('/Encryption')
def Encryption():
    return template('Encryption.html')

# This page will display the results of the Enigma machine decryption
@post('/EncryptionResult')
def EncryptionResult():
    return template('EncryptionResult.html')

# At the end we want to have a login page, so the table page will be dependent upon that page. Eventually, the route will depen
@get('/MachineTable')
def EnigmaTable():
    return template('MachineTable.html')

run(host='localhost',port = 8080,debug = True, reloader = True)

@get('/addMachine')
def Addmachine():
    return template('addMachine.html')

@post('/addingMachine')
def AddingMachine():
    return template('addingMachine.html')