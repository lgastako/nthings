from flask import Flask
import settings

app = Flask("nthings")
app.config.from_object("nthings.settings")

import views
