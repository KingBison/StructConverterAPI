from flask import request

def convert():
    TO = request.args.get('from')
    FROM = request.args.get('to')
    if TO == None or FROM == None:
        return "missing parameters"

    return "converted"