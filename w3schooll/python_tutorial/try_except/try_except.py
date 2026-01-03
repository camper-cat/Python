try:
    age = 15
    if age > 18:
        print("Okay")
    else:
        raise Exception("Age must be > 18")
except Exception as error:
    print(error)

