from flask import Flask, render_template, request

app = Flask(__name__)


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("dashboard.html")


# ---------------- TRADE ----------------
@app.route("/trade", methods=["GET", "POST"])
def trade():

    message = ""

    if request.method == "POST":

        symbol = request.form.get("symbol")
        side = request.form.get("side")
        order_type = request.form.get("orderType")
        quantity = request.form.get("quantity")
        price = request.form.get("price")

        message = f"""
        SUCCESS ✅

        Symbol: {symbol}
        Side: {side}
        Type: {order_type}
        Quantity: {quantity}
        Price: {price}
        """

    return render_template("trade.html", message=message)


# ---------------- HISTORY ----------------
@app.route("/history")
def history():
    return render_template("history.html")


# ---------------- SIGNALS ----------------
@app.route("/signals")
def signals():
    return render_template("signals.html")


# ---------------- SETTINGS ----------------
@app.route("/settings")
def settings():
    return render_template("settings.html")


# ---------------- SECURITY ----------------
@app.route("/security")
def security():
    return render_template("security.html")


if __name__ == "__main__":
    app.run(debug=True)