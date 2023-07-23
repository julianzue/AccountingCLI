from colorama import Fore, Style, init
import pyfiglet
import time

init()


# colors

y = Fore.LIGHTYELLOW_EX
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
c = Fore.LIGHTCYAN_EX
re = Fore.RESET

# styles

dim = Style.DIM
res = Style.RESET_ALL


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
            {"name": "list", "function": self.liste, "info": "Lists the entries"},
            {"name": "add", "function": self.add_list, "info": "Adds an entries to the list"},
            {"name": "help", "function": self.help_page, "info": "Shows this  help page"},
            {"name": "close", "function": self.close, "info": "Closes this program"},
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
                print("")
                print(print_style("error", "No option found with this number!", ""))
                self.help_page()
        else:
            found = False
            for item in self.items:
                if choose == item["name"]:
                    found = True
                    item["function"]()

            if not found:
                print("")
                print(print_style("error", "No option found with this keyword!", ""))
                self.help_page()

    def liste(self):

        print("")

        index = 0
        sum_all = 0.0

        with open(filename, "r") as fr:
            for index, line in enumerate(fr.readlines(), 1):
                
                if line.strip("\n").split(" | ")[1] == "-":
                    color = r
                    symbol = "-"
                    sum_all += float(line.strip("\n").split(" | ")[2]) * (-1)
                else:    
                    color = re
                    sum_all += float(line.strip("\n").split(" | ")[2])

                spl = line.strip("\n").split(" | ")
                out = spl[0] + " | " + color + spl[1] + " " + spl[2] + " €" + re + " | " + spl[3]

                print(print_style("list", out, index))

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


    def help_page(self):

        print("")

        #print(c + "HELP" + re)

        #print("")

        for index, item in enumerate(self.items, 1):

            out = item["name"] + dim + " - " + item["info"] + res

            print(print_style("list", out, index))

        print("")

        self.choose()


    def close(self):

        print("")

        print(print_style("error", "Programm closed!", ""))

        print("")


Accounting()