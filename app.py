from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.secret_key = "clef_secrete_moderne"
metrics = PrometheusMetrics(app)
# Optionnel : ajoute des infos statiques sur l'application
metrics.info('app_info', 'Application Flask DevOps', version='1.0.0')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utilisateurs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.create_all()

# Route 1 : Le Formulaire (Accueil)
@app.route('/')
def index():
    return render_template('index.html')

# Route 2 : Enregistrement (Action POST)
@app.route('/register', methods=['POST'])
def register():
    nom = request.form.get('nom')
    email = request.form.get('email')
    if nom and email:
        try:
            nouvel_utilisateur = Utilisateur(nom=nom, email=email)
            db.session.add(nouvel_utilisateur)
            db.session.commit()
            flash("Succès ! Données enregistrées dans la BD.", "success")
        except:
            db.session.rollback()
            flash("Erreur : Cet email existe déjà.", "danger")
    return redirect(url_for('index'))

# Route 3 : Liste des enregistrements (Nouvelle page)
@app.route('/records')
def records():
    utilisateurs = Utilisateur.query.all()
    return render_template('records.html', utilisateurs=utilisateurs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
