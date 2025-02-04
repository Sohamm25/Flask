from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
items = []
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form.get("item")
        if item:
            items.append(item)
            return redirect(url_for("index"))
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>To-Do List App</title>
    </head>
    <body>
        <h1>To-Do List</h1>

        <form method="POST">
            <input type="text" name="item" placeholder="Enter an item">
            <button type="submit">Add</button>
        </form>

        <ul>
            {''.join(f'<li>{item}</li>' for item in items)}
        </ul>

        <form method="POST" action="/clear">
            <button type="submit">Clear List</button>
        </form>

    </body>
    </html>
    """
    return html


@app.route("/clear", methods=["POST"])
def clear():
    items.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
