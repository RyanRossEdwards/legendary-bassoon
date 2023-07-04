from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ex1')
def ex1():
    return render_template('ex1.html')

@app.route('/generate_sentence', methods=['POST'])
def generate_sentence():
    # Retrieve the selected checkboxes from the request
    checkbox1 = request.form.get('checkbox1')
    checkbox2 = request.form.get('checkbox2')
    checkbox3 = request.form.get('checkbox3')
    
    # Generate the sentence based on the selected checkboxes
    sentence = "You have selected boxes:"
    if checkbox1 == 'true':
        sentence += " [1]"
    if checkbox2 == 'true':
        sentence += " [2]"
    if checkbox3 == 'true':
        sentence += " [3]"
    
    # Return the sentence as a JSON response
    return jsonify({'sentence': sentence})
    # response = jsonify({'sentence': sentence})
    # response = jsonify(sentence=sentence)
    # print(response.get_data().decode('utf-8'))
    # return response

if __name__ == '__main__':
    app.run()
