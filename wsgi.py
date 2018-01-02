
#The engine of wsgi must be started with variable named application, this variable is initialized by Flask
app = application = Flask(__name__)

#Routing to templates path
@app.route('/')
def accueil():
    return render_template('pages/accueil.html')
