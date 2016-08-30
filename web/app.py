#!/usr/bin/env python2

import sys
import json
from flask import Flask, render_template, request


app = Flask(__name__)

page_title = "JSON"
base_url = "/json"


def parse_json(json_string):
    parsed = json.loads(json_string)
    return json.dumps(parsed, indent=4, sort_keys=True)

@app.route(base_url, methods=['GET', 'POST'])
def handle_req():
    if request.method == 'POST':
        try:
            json_string = request.form['jsondata']
            json_pretty = parse_json(json_string=json_string)

            return render_template('main.html', page_title=page_title, base_url=base_url, json_string=json_string, json_pretty=json_pretty)
        except ValueError as e:
            return render_template('main.html', page_title=page_title, base_url=base_url, json_string=json_string, error="Error: {err}".format(err=e))

    return render_template('main.html', page_title=page_title, base_url=base_url)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=5000)

