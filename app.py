from flask import Flask

app = Flask(**name**)

@app.route('/')
def hello():
return "Hello from Manimozhi Python Docker Application!"

if **name** == "**main**":
app.run(host='0.0.0.0', port=5000)
