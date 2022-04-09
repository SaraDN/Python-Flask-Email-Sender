from urllib import request
from flask import Flask, render_template
import smtplib

app = Flask(__name__)

@app.route('/')
def returnHome():
    work_exp =  { "position": "Java Developer", "company": "Oracle", "period": "Jun 2020 - Oct 2020" }
    education = { "college": "Automatica si Calcularoare, CTI, UPB", "high school":"CNITV"}
    projects = {"project1":"CV Python Flask", "project2":"Spring Boot cu Thymeleaf website", "project3":"Site-uri pentru membrii familiei, diverse"}
    lenguages ={"limba1":"italiana", "limba2":"engleza", "limba3":"germana"}
    tech = {"tech1":"Java", "tech2":"HTML, CSS, JS, Bootstrap", "tech3":"C/C++", "tech4":"Python"}
    return render_template('Home.html', work_exp=work_exp, education=education, projects=projects, lenguages=lenguages, tech=tech)


@app.route('/Contact')
def returnContact():
    return render_template('Contact.html', title='Contact')


# @app.route('/Contact', methods=['POST', 'GET'])
# def form():
#     nume = request.form.get("nume")
#     email = request.form.get("email")
#     mesaj = request.form.get("mesaj")
#     message = "Ai trimis email"
#     server = smtplib.SMT("smtp.gmail.com", 587)
#     server.starttls()
#     server.login("sara.nucuta@gmail.com", "***")
#     server.sendmail("sara.nucuta@gmail.com", email, message)
#     return render_template('form.html', title='succes')


if __name__ == '__main__':
    app.run()
