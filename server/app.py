from flask import Flask

app = Flask(__name__)


existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# define a route for the index page that returns a welcome message
@app.route('/')
def index():
    return "Welcome to Flatiron Cars", 200

#  define a route for the model page that takes a model name as a parameter
@app.route('/<model>')
def model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!", 200
    return f"No models called {model} exists in our catalog"

# This checks if this specific file is being run directly
if __name__ == "__main__":
    app.run(debug=True)