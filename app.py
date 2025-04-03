from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def decimal_to_binary(n):
    return bin(n)[2:]

@app.route('/')
def home():

    return ''' "DECIMAL TO BINARY"
    <form action="/convert" method="get">
        <input type="number" name="decimal" required>
        <button type="submit">Convert</button>
    </form>
    '''

@app.route('/convert')
def convert():
    decimal = request.args.get('decimal', type=int)
    if decimal is None:
        return "Please provide a valid decimal number.", 400
    binary = decimal_to_binary(decimal)
    return f"Binary equivalent: {binary}"

if __name__ == "__main__":
    app.run(debug=True)
