from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'AAA'
    message = "Absolute Awesome App"
    description = "This is an absolute awesome app for awesome people"
    return render_template('index.html', title=title, message=message, description=description)


if __name__ == "__main__":
    app.run(debug=True)