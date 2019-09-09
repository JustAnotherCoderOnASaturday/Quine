count = 0

func0 = """
def foo():
    global count
    count = 10     # Modifies the global variable count
    return 100
"""

func1 = """
def main():
    file = open("temp2.py", 'w+')
    file.write("count = 0\\n")
    for num in range(0, 2):       
        fnc_name = eval("func" + str(num)) 
        file.write("func" + str(num) + " = \\"\\"\\"")

        for c in fnc_name:
            if c == "\\\\":
                file.write("\\\\")
            file.write(c)
        file.write("\\"\\"\\"\\n")

    file.write(func1)
    file.close()
    exec(func0)
    eval("foo()")
main()
"""

def main():
    file = open("temp2.py", 'w+')
    file.write("count = 0\n")
    for num in range(0, 2):                 # Since there are 2 functions to write
        fnc_name = eval("func" + str(num))  # Sets the variable to the string
        file.write("func" + str(num) + " = \"\"\"")

        for c in fnc_name:
            if c == "\\":
                file.write("\\") # An additional "\"
            file.write(c)
        file.write("\"\"\"\n")

    file.write(func1)
    file.close()
    exec(func0)
    eval("foo()")

main()