from builders.json import buildFromJson

def buildUniversalStruct(body, fromType):
    if fromType == 'json':
        univeral, err = buildFromJson(body)
        if err != None:
            return None, err
        else:
            return univeral, None
        
    return None, "from type not identified"