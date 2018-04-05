from flask import Flask, render_template


app = Flask(__name__)

COUNTS = 0


@app.route('/request_counter')
def request_counter():
    global COUNTS
    COUNTS += 1
    return render_template("request_counter.html", counts=COUNTS)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
