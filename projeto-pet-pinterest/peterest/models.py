# criaçao do banco de dados

from peterest import database, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin

# processo padrao de uma funçao  que carrega o id do usuario apartir do id
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

#classe usuario que recebe id database . column armazenando como um inteiro e tendo uma key primaria ou seja: numero unico 
# user name armazena o n ome do usuario como uma string !nao pode ser vazio.
# email tbm e armazenado como str e nao pode ser vazio porem tem um diferencial ele tem que ser unico um email por usuario.
# senha e o mesmo do user name
# fotos nao vai ser coluna ela vai receber valor da referncia entre usuario e foto lazy= true e para otimizar a organizaçao do banco de dados
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    user_name = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)
    
# assim como o id do usuario e um inteiro e unico
# img receberar um valor str e defalt.png para ser utilizado somente os caminhos da imagen urls que vao ser armazenadas em uma pasta para q nao sobrecarregue o servidor
#data foi uma das mais complicadas anteriormente estava utilizando o metodo datetime.utcflow porem o py estava inforrmando q era um metodo ultrapassado entao dei uma pesquisada e substitui ele pelo metodo lambda (segubndo o gpt utcflow faria todas as imagens terem as mesmas quantidades de tempo apartir do inicio do site algo semelhante nao compreendi muito bem
class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    img = database.Column(database.String, default="default.png")
    data_criaçao = database.Column(database.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

#lembrar das letras altas sql e muito raparigo se por uma em baixa ele reclama