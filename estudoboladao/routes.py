from flask import render_template, url_for, redirect, flash, request
from estudoboladao import app, database, bcrypt
from estudoboladao.forms import FormLogin, FormCriarConta, FormCriarViagem
from estudoboladao.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required
lista_usuarios = ['Lira', 'João', 'Alon', 'Alessandra', 'Amanda']
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no email {form_login.email.data}', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash(f'Email ou senha incorretos, tente novamente', 'alert-danger')

    if form_criar_conta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        usuario = Usuario(username=form_criar_conta.username.data,email=form_criar_conta.email.data,senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso no email {form_criar_conta.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)

@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Logout feito com sucesso!', 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

@app.route('/viagem/criar')
@login_required
def criar_viagem():
    form_criarViagem = FormCriarViagem()
    return render_template('criarviagem.html', form_criarViagem=form_criarViagem)