from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<h2>Advanced Calculator</h2>
<form method="post">
  Number 1: <input name="n1" required><br><br>
  Number 2: <input name="n2" required><br><br>

  <button name="op" value="add">Add</button>
  <button name="op" value="sub">Subtract</button>
  <button name="op" value="mul">Multiply</button>
  <button name="op" value="div">Divide</button>
  <button name="op" value="mod">Modulus</button>
  <button name="op" value="pow">Power</button>
</form>

{% if result is not none %}
<h3>Result: {{result}}</h3>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None

    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        op = request.form['op']

        if op == "add":
            result = n1 + n2
        elif op == "sub":
            result = n1 - n2
        elif op == "mul":
            result = n1 * n2
        elif op == "div":
            result = "Cannot divide by zero" if n2 == 0 else n1 / n2
        elif op == "mod":
            result = n1 % n2
        elif op == "pow":
            result = n1 ** n2

    return render_template_string(html, result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)