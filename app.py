from flask import Flask

app=Flask(__name__)

@app.route('/Hola')

def hola():
    return "Hola a todos"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5006, debug=True)