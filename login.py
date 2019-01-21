from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run()


def index():
    print('login info')
# # <<<<<<< HEAD
# sgdg
# =======
#
#
# jingli
# >>>>>>> 2db8e7f8c551a9c6fa767cc99d8243eb368aa80d
