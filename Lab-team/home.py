from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('Login_interface.html')

@app.route('/information', methods=['GET', 'POST'])
def information():
    return render_template('All_information.html')

@app.route('/Last_page', methods=['GET', 'POST'])
def Last_page():
    return render_template('Last_page.html')

if __name__ == '__main__':
    app.run(host = '222.195.93.47',port = 5345)




