obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

def stringifyNumbers(obj):
    obj1 = obj
    for key in obj1:
        if type(obj1[key]) == dict:
            obj1[key] = stringifyNumbers(obj1[key])
        elif type(obj1[key]) == int:
            obj1[key] = str(obj1[key])
    return obj1

    

print(stringifyNumbers(obj1))