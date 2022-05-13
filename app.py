from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import eng_to_ipa as p

app = Flask(__name__)

@app.route('/engToIpa/<text>', methods=['GET'])
def translateEngToIpa(text):
    return p.convert(text)

if __name__ == '__main__':
   app.run()
