from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="post">
        <p>Rotate by:
        <input name="rot" type="text" value=0></p>
        <textarea name="text" rows="10" cols="30"></textarea>
        <br>
        <button type="button" onclick=encrypt()>Submit Query</button>
      </form>
    </body>
</html>

"""

@app.route("/")

def index():
    return form

@app.route("/", methods=['POST'])

def encrypt():

    text = request.form.text
    rot = int(request.form.rot)

    encrypt_string = rotate_string(text, rot)

    return encrypt_string

app.run()