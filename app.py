from flask import Flask, request, jsonify, render_template
import os
import argparse
import random
app = Flask(__name__, template_folder='../flaskk')
from flask import (Flask, render_template, request, redirect, url_for, session)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        body = request.get_json()
        command = body.get("command")
        if command == "details":
            return Details(body)
        elif command == "calculator":
            return Calculator(body)
        elif command == 'lottery':
            return Lottery(body)

    elif request.method == "GET":
        # print(request.args)
        if 'username' in request.args:
            name = request.args['username']
        if 'password' in request.args:
            passs = request.args['password']
            print("Your Email :",name,"\nYour Password :",passs, file=open('C:/Users/USER/Desktop/VSCODE/flaskk/details.txt', 'w'))
            if name == '' or passs == '':
                return render_template('return.html')
            else:  
                return redirect('/menu')

        return render_template('login.html')

@app.route('/home')
def home_page():
    # print(request.args)
    if 'menu' in request.args:
        return redirect('/menu')
    return render_template('home.html')

@app.route('/menu')
def menu():
    # print(request.args)
    if 'home1' in request.args:
        return redirect('/home')
    elif 'home2' in request.args:
        return render_template('home2.html')
    elif 'home3' in request.args:
        return render_template('home3.html')
    elif 'login' in request.args:
        return redirect('/')
    return render_template('menu.html')


def Details(body):
    name = body['name']
    lastname = body['lastname']
    phone = body["phone"]
    return f"---------\nYour name : {name}\nYour Lastname : {lastname}\nYour Phone : {phone}\n-----------"

def Calculator(body):
    number1 = body['number1']
    operator = body['operator']
    number2 = body['number2']
    if operator == '+':
        summ = float(number1) + float(number2)
        return ({f"{number1} + {number2} = ":summ})
    elif operator == '-':
        summ = float(number1) - float(number2)
        return ({f"{number1} - {number2} = ":summ})
    elif operator == '/':
        summ = float(number1) / float(number2)
        return ({f"{number1} / {number2} = ":summ})

def Lottery(body):
    number = body['number']
    num = random.randint(1,10)
    if int(number) == int(num):
        return f"The number Was :{num} \n You Win !"
    else:
        return f"The Number Was :{num} \n You Lose !"

# parser = argparse.ArgumentParser()
# parser.add_argument("name", type= str, help="Enter Ip")
# # parser.add_argument("port", type= int, help="Enter a Port")

if __name__ == '__main__':
    # args = parser.parse_args()
    app.run(host='0.0.0.0', port= 5000, debug= True)