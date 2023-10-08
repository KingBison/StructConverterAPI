from flask import request
from builders.builderSwitch import buildUniversalStruct
from generators.generateOut import generateOut

def convert():
    FROM = request.args.get('from')
    TO = request.args.get('to')
    if TO == None or FROM == None:
        return "missing parameters", 400
    
    if request.is_json:
        try:
            body = request.get_json()
        except Exception as e:
            return f"Error parsing JSON: {str(e)}", 400
    
    # build universal struct from FROM
    UNIVERSAL, err = buildUniversalStruct(body, FROM)
    if err != None:
        return f"Error building universal struct: {err}", 400

    OUT, err = generateOut(UNIVERSAL, TO)
    if err != None:
        return f"Error generating {TO} from universal: {err}", 500
    # convert to TO

    return OUT