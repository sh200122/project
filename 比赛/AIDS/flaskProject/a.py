from flask import Flask, render_template, request, redirect, url_for, session

import bankdata as ba
import function as func

app = Flask(__name__)



a=ba.updata.idlst()
print(a,type(a))