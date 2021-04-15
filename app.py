from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html')

@app.route('/test2', methods=['GET', 'POST'])
def test2():
    return render_template('test2.html')

if __name__ == '__main__':
    app.run()