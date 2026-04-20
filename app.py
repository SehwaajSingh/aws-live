from flask import Flask, request

app = Flask(__name__)

products = []

USERNAME = "admin"
PASSWORD = "1234"

# COMMON STYLE
style = """
<style>
body {
    font-family: 'Segoe UI', Arial;
    background: linear-gradient(to right, #74ebd5, #acb6e5);
    margin: 0;
    text-align: center;
}

.navbar {
    background: #2c3e50;
    padding: 15px;
}

.navbar a {
    color: white;
    margin: 10px;
    text-decoration: none;
    font-weight: bold;
}

.navbar a:hover {
    color: #1abc9c;
}

.card {
    background: white;
    padding: 20px;
    margin: 40px auto;
    width: 350px;
    border-radius: 10px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

input {
    padding: 10px;
    margin: 8px;
    width: 80%;
    border-radius: 5px;
    border: 1px solid #ccc;
}

button {
    padding: 10px 20px;
    background: #1abc9c;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #16a085;
}

table {
    margin: auto;
    border-collapse: collapse;
    background: white;
}

th, td {
    padding: 12px;
    border: 1px solid #ddd;
}

th {
    background: #1abc9c;
    color: white;
}
</style>
"""

# NAVBAR
navbar = """
<div class="navbar">
    <a href="/">Home</a>
    <a href="/login">Login</a>
    <a href="/add">Add Product</a>
    <a href="/view">Stock</a>
    <a href="/about">About</a>
</div>
"""

# HOME
@app.route('/')
def home():
    return f"""
    {style}
    {navbar}
    <div class="card">
        <h1>🛒 Grocery System</h1>
        <p>Manage your store easily</p>
    </div>
    """

# LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            return f"{style}{navbar}<h2>✅ Login Successful</h2>"
        else:
            return f"{style}{navbar}<h2>❌ Invalid Login</h2>"

    return f"""
    {style}
    {navbar}
    <div class="card">
        <h2>🔐 Login</h2>
        <form method="POST">
            <input name="username" placeholder="Username"><br>
            <input type="password" name="password" placeholder="Password"><br>
            <button>Login</button>
        </form>
    </div>
    """

# ADD PRODUCT
@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        products.append((
            request.form['name'],
            request.form['price'],
            request.form['qty']
        ))
        return f"{style}{navbar}<h2>✅ Product Added</h2>"

    return f"""
    {style}
    {navbar}
    <div class="card">
        <h2>➕ Add Product</h2>
        <form method="POST">
            <input name="name" placeholder="Product Name"><br>
            <input name="price" placeholder="Price"><br>
            <input name="qty" placeholder="Quantity"><br>
            <button>Add</button>
        </form>
    </div>
    """

# VIEW STOCK
@app.route('/view')
def view():
    rows = ""
    for p in products:
        rows += f"<tr><td>{p[0]}</td><td>₹{p[1]}</td><td>{p[2]}</td></tr>"

    return f"""
    {style}
    {navbar}
    <h2>📦 Stock</h2>
    <table>
        <tr><th>Name</th><th>Price</th><th>Qty</th></tr>
        {rows}
    </table>
    """

# ABOUT
@app.route('/about')
def about():
    return f"""
    {style}
    {navbar}
    <div class="card">
        <h2>About</h2>
        <p>Cloud-Based Grocery Store Project</p>
        <p>Features: Login, Add, View Stock</p>
    </div>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
