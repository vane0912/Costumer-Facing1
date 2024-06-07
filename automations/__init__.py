from flask import Flask


if __name__ == "__main__":
    app = Flask(__name__)
    app.run(debug=True)

import automations.homepage
import automations.weekly
import automations.applications
