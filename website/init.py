from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adksdjfnkd'

from website import routes