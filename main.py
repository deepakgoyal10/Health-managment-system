# Health managment system
while True:
    print("press 1 to add and press 2 for retrieve")
    n1 = int(input())
    print("press 1 for Harry and press 2 for Rohan and press 3 for Hammad")
    n2 = int(input())
    print("Enter 1 for exersice 2 for food")
    n3 = int(input())


    def getdate():
        import datetime
        return datetime.datetime.now()


    if n1 == 1:
        if n2 == 1:
            if n3 == 1:
                f = open("Harry's Exercise.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input(" Enter the name of your exercise: "))
                f.write("\n")
                print("item added successfully")
                f.close()
            if n3 == 2:
                f = open("Harry's food.txt", "a")
                f.write("\n")
                f.write(str([str(getdate())]))
                f.write(input("Enter your meal: "))
                print("item added successfully")
                f.close()
        if n2 == 2:
            if n3 == 1:
                f = open("rohan's exercise.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input("Enter the name of exercise: "))
                f.write("\n")
                print("item added successfully")
                f.close()
            if n3 == 2:
                f = open("rohan's food.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input("Enter your meal: "))
                f.write("\n")
                print("item added successfully")
                f.close()
        if n2 == 3:
            if n3 == 1:
                f = open("Hammad's exercise.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input("Enter your exercise: "))
                f.write("\n")
                print("item added successfully")
                f.close()
            if n3 == 2:
                f = open("Hammad's food.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input("Enter your meal: "))
                f.write("\n")
                print("item added successfully")
                f.close()
    if n1 == 2:
        if n2 == 1:
            if n3 == 1:
                f = open("Harry's Exercise.txt")
                content = f.read()
                print(content)
                f.close()
            if n3 == 2:
                f = open("Harry's food.txt")
                content = f.read()
                print(content)
                f.close()
        if n2 == 2:
            if n3 == 1:
                f = open("rohan's exercise.txt")
                content = f.read()
                print(content)
                f.close()
            if n3 == 2:
                f = open("rohan's food.txt")
                content = f.read()
                print(content)
                f.close()
        if n2 == 3:
            if n3 == 1:
                f = open("Hammad's exercise.txt")
                content = f.read()
                print(content)
                f.close()
            if n3 == 2:
                f = open("Hammad's food.txt")
                content = f.read()
                print(content)
                f.close()
