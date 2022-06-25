obj1 = {
  "outer": 2,
  "obj": {
    "inner": "python",
    "otherObj": {
      "superInner": 'django',
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

def collectStrings(obj):
    arr = []
    for key in obj:
        if type(obj[key]) == dict:
            arr.extend(collectStrings(obj[key]))
        if type(obj[key]) == str:
            arr.append(obj[key])
    return arr

print(collectStrings(obj1))

