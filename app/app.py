"""Main application module for the app."""

from flask import Flask, render_template, request

from .calculator import add, divide, multiply, subtract

app = Flask(__name__, template_folder="templates")


# Basic web routes.
@app.route("/", methods=["GET", "POST"])
def index():
    """Basically handlea GET and POST requests for the web interface."""
    result = None
    error = None
    a = ""
    b = ""
    op = "add"
    # To handle form submission.
    if request.method == "POST":
        a = request.form.get("a", "0")
        b = request.form.get("b", "0")
        op = request.form.get("op", "add")
        try:
            x = float(a)
            y = float(b)
            # Lines to perform the operation based on user input.
            if op == "add":
                result = add(x, y)
            elif op == "subtract":
                result = subtract(x, y)
            elif op == "multiply":
                result = multiply(x, y)
            elif op == "divide":
                result = divide(x, y)
            else:
                error = "Invalid operation."
        except ValueError as e:
            error = f"Invalid input: {e} Please check your request."
    # To render the template with results.
    return render_template(
        "index.html",
        result=result,
        error=error,
        a=a,
        b=b,
        op=op,
    )


# Run the Flask server for the application.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
