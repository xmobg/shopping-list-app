from flask import Flask, render_template, request, redirect, session
from models import db, User,ShoppingList,Item
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
with app.app_context():
    db.create_all()

app.secret_key = 'somethink_secret'
@app.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', lists=user.lists)
@app.route('/register', methods=["GET",'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)
        user = User(username=username,name=name, email=email, password=password_hash)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return redirect('/login')
        session['user_id'] = user.id
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')
@app.route('/create-list', methods=['POST'])
def create_list():
    if 'user_id' not in session:
        return redirect('/login')
    name = request.form['name']
    new_list = ShoppingList(name=name, user_id=session['user_id'])
    db.session.add(new_list)
    db.session.commit()
    return redirect('/')
@app.route('/list/<int:list_id>')
def view_list(list_id):
    if 'user_id' not in session:
        return redirect('/login')
    shopping_list = ShoppingList.query.get_or_404(list_id)
    return render_template('list.html', shopping_list=shopping_list)
@app.route('/list/<int:list_id>/add-item', methods=['POST'])
def add_item(list_id):
    name = request.form['name']
    quantity = request.form['quantity']
    category = request.form['category']
    new_item = Item(name=name, quantity=quantity, category=category, list_id=list_id)
    db.session.add(new_item)
    db.session.commit()
    return redirect(f'/list/{list_id}')
@app.route('/item/<int:item_id>/toggle', methods=['POST'])
def toggle_item(item_id):
    item = Item.query.get_or_404(item_id)
    item.is_bought = not item.is_bought
    db.session.commit()
    return redirect(f'/list/{item.list_id}')
@app.route('/item/<int:item_id>/delete', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    list_id = item.list_id
    db.session.delete(item)
    db.session.commit()
    return redirect(f'/list/{list_id}')
@app.route('/list/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    shopping_list = ShoppingList.query.get_or_404(list_id)
    for item in shopping_list.items:
        db.session.delete(item)
    db.session.delete(shopping_list)
    db.session.commit()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)