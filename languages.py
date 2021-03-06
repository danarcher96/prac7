
from programminglanguage import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    list = []
    list.append(ruby)
    list.append(python)
    list.append(vb)

    print("The dynamically typed languages are:")
    for rows in list:
        if rows.is_dynamic(rows.typing) == True:
            print(rows.name)



main()




