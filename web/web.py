import json
import re
import sys
from flask import Flask, render_template, request


app = Flask(__name__)

page_title = "JSON Validator"
page_version = "0.2"
base_url = "/"
main_html = "main.html"


def clear_rsyslog_escapes(data):
    return re.sub(r'#\d+', '', data)

def parse_json(json_string):
    parsed = json.loads(json_string)
    return json.dumps(parsed, indent=4, sort_keys=True)

def get_page(json_string="", json_pretty=None, error=None):
    return render_template(
        main_html,
        page_title=page_title,
        page_version=page_version,
        base_url=base_url,
        json_string=json_string,
        json_pretty=json_pretty,
        error_string=error)

@app.route(base_url, methods=['GET', 'POST'])
def handle_req():
    if request.method == 'POST':
        try:
            json_string = request.form['jsondata']
            json_pretty = parse_json(json_string=clear_rsyslog_escapes(json_string))
            return get_page(json_string=json_string, json_pretty=json_pretty)

        except ValueError as e:
            return get_page(json_string=json_string, error="Error: {err}".format(err=e))

    return get_page()

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
