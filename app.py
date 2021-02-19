from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        What toppings?<br/>
        <input type="text" name="toppings">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get("toppings")
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings, { users_froyo_toppings}!'

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        What is your favorite animal ?<br/>
        <input type="text" name="animal"><br/>
        What is your favorite color ?<br/>
        <input type="text" name="color">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    user_fav_color = request.args.get('color')
    user_fav_animal = request.args.get('animal')
    user_fav_city = request.args.get('city')
    return f"Wow, I didn't know {user_fav_color} {user_fav_animal} lived in {user_fav_city}!"





@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
    
        Write your secret message!<br/>
        <input type="text" name="message">
        <input type="submit" value="Submit!">
    </form>
    """
    

@app.route('/message_results', methods=['POST'])
def message_results():
    user_message = request.args.get("message")

    sort = sort_letters( user_message)

    """Shows the user their message, with the letters in sorted order."""
    return f"Here is your secret message! {user_message} {sort}"






@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    num1 = request.args.get("operand1")
    operation = request.args.get("operation")
    num2 = request.args.get("operand2")

    if operation == 'add':
        result = int(num1) + int(num2)
        return f"You chose to {operation} {num1} and {num2}. Your result is: {result}"
    if operation == 'subtract':
        result = int(num1) - int(num2)
        return f"You chose to {operation} {num1} and {num2}. Your result is: {result}"
    if operation == 'multiply':
        result = int(num1) * int(num2)
        return f"You chose to {operation} {num1} and {num2}. Your result is: {result}"
    if operation == 'divide':
        result = int(num1) / int(num2)
        return f"You chose to {operation} {num1} and {num2}. Your result is: {result}"





    
    """Shows the user the result of their calculation."""
    return f"You chose to {operation} {num1} and {num2}. Your result is: 7"


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = ''

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = ''

    # TODO: Generate a random number from 1 to 99
    lucky_number = 0

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
