from flask import Flask

app=Flask(__name__)

@app.route('/')
def homePage():
    return('hello d mahila lahari')
if (__name__=="__main__"):
    app.run()