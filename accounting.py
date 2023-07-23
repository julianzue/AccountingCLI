from colorama import Fore, init
import pyfiglet
import time

init()


# colors

y = Fore.LIGHTYELLOW_EX
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
c = Fore.LIGHTCYAN_EX
re = Fore.RESET


def print_style(action, text, count):

    output = ""

    if action == "input":
        output = y + "[+] " + re + text

    elif action == "list":
        output = c + "{:03d}".format(count) + " " + re + text

    elif action == "info":
        output = c + "[*] " + re + text

    elif action == "error":
        output = r + "[!] " + re + text
    
    return output


filename = "list.txt"


class Accounting():
    def __init__(self):

        self.items = [
            {"name": "list", "function": self.liste},
            {"name": "add", "function": self.add_list},
            {"name": "close", "function": self.close},
        ]

        f = pyfiglet.Figlet()
        print(c + f.renderText("Money") + re)

        for index, item in enumerate(self.items, 1):
            print(print_style("list", item["name"], index))

        print("")

        self.choose()
        
    def choose(self):

        choose = input(print_style("input", "", ""))

        if choose.isnumeric():
            try:
                self.items[int(choose) - 1]["function"]()
            except:
                print(print_style("error", "No option found with this number!", ""))


    def liste(self):

        print("")

        index = 0
        sum_all = 0.0

        with open(filename, "r") as fr:
            for index, line in enumerate(fr.readlines(), 1):
                print(print_style("list", line.strip("\n"), index))

                if line.strip("\n").split(" | ")[1] == "-":
                    sum_all += float(line.strip("\n").split(" | ")[2]) * (-1)
                else:    
                    sum_all += float(line.strip("\n").split(" | ")[2])

        if index == 0:
            print(print_style("error", "List is empty!", ""))

        print("")
        print(c + "[*] " + re +  "Total: " + "{:7.2f}".format(sum_all) + " €")

        print("")
        self.choose()


    def add_list(self):
        
        print("")
        
        name = input(print_style("input", "Name:  ", ""))
        price = input(print_style("input", "Price: ", ""))
        plus_minus = input(print_style("input", "+/-:   ", ""))

        with open(filename, "a") as fa:

            t = time.strftime("%Y-%m-%d %H:%M")

            fa.write(t + " | " + plus_minus + " | " + "{:7.2f}".format(float(price)) + " | " + name + "\n")

        print("")

        print(print_style("info", "Successfully added!", ""))

        print("")

        self.choose()

    def close(self):

        print("")

        print(print_style("error", "Programm closed!", ""))

        print("")


Accounting()