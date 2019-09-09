def main():
    str = "Hello World!"

    quine = [
        "def main():",                    # Line 1
        "   str = \"Hello World!\"",    # 2
        "   quine = [",                 # 3
                                        # The string itself Should Go in Between
        "   ]",
        "   for init in quine[0:3]",
        "       print(init)",
        "   for mid in quine:",
        "       print(\"     \\\"\", end='')",
        "       for ch in mid:",
        "           if ch in [\"\\\\\", \"\\\"\"]:",
        "               print(\"\\\\\", end='')",
        "           print(ch, end='')",
        "       print(\"\\\",\", end='\\n')",
        "   for final in quine[3:]:",
        "       print(final)",
        "   print(str)"
    ]

    for init in quine[0:3]:
        print(init)
    for mid in quine:
        print("     \"", end='')
        for ch in mid:
            if ch in ["\\", "\""]:
                print("\\", end='')
            print(ch, end='')
        print("\",", end='\n')
    for final in quine[3:]:
        print(final)

    print(str)                          ## Execute Program

main()
