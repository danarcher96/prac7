from guitars import Guitars

def main():

    list = []

    while True:
        guitar_name = input("Name")
        if guitar_name =="":
            False
        guitar_age = input("Age")
        guitar_cost = input("Cost")
        list.append(Guitars(guitar_name, guitar_age, guitar_cost))

    print("These are my guitars")



    for rows in list:
        if rows.is_vintage(rows.year) is True:
            print("Guitar {}: {} {}, worth ${:10.2f} (vintage)".format(i, rows.name, rows.year, rows.cost))
        else:
            print("Guitar {}: {} {}, worth ${:10.2f} ".format(i, rows.name, rows.year, rows.cost))








main()