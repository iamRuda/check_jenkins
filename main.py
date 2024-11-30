from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route('/')
def main():
    return render_template('index.html')

# Страница списка
@app.route('/list')
def list_page():
    # Для примера, просто передаем список
    items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
    return render_template('list.html', items=items)

# Страница контактов
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
