from flask import Flask, render_template, request


app = Flask(__name__)

COUNTS = {'GET': 0, 'POST': 0, 'DELETE': 0, 'PUT': 0}


@app.route('/request_counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def request_counter():
    global COUNTS
    for key in COUNTS.keys():
        if request.method == key:
            COUNTS[key] += 1
    return render_template("request_counter.html", counts=COUNTS)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
