def count_lowercase_and_uppercase(string):
    uppercase= 0
    lowercase= 0


    for letter in string:
        if letter.isupper():
            uppercase+=1
        elif letter.islower():
            lowercase+=1

    print(f"mayusculas:{uppercase}")
    print(f"minusculas:{lowercase}") 

string = "coMO Estas"
count_lowercase_and_uppercase(string)

