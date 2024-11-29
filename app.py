import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<center> 
    <img src="https://cdn.jsdelivr.net/gh/wukong-i/static@main/channel%20img.jpg" style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""

if __name__ == "__main__":
    app.run()