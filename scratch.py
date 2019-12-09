from time import sleep


def rgb2hex(r, g, b, ):         # RGB to Hex
    hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex


def hex2rgb(hex):               # Hex to RGB
    value = hex.lstrip('#')
    return tuple(int(value[i:i + len(value) // 3], 16) for i in range(0, len(value), len(value) // 3))


def prompt():
    print("Hello and welcome to my color converter!")
    sleep(2)
    while True:
        option = input("To convert Hex to RGB press '1', press '2' for RGB to Hex, or press '0' to exit.")
        option = option.upper()

        if option == '1':
            print("Hex to RGB..")
            sleep(1)
            hex = input("Please enter 6 digits: ")
            rgb = hex2rgb(hex)
            print(rgb)

        elif option == '2':
            print("RGB to Hex..")
            sleep(1)
            r = int(input("Enter red value: "))
            if r > 255 or r < 0:
                print("ERROR - Not within 0-255 range")
                return
            g = int(input("Enter green value: "))
            if g > 255 or g < 0:
                print("ERROR - Not within 0-255 range")
                return
            b = int(input("Enter blue value: "))
            if b > 255 or b < 0:
                print("ERROR - Not within 0-255 range")
                return
            hex = rgb2hex(r,g,b)
            print(hex)

        elif option == '0':
            print("Thanks for converting!")
            sleep(1)
            exit()

        else:
            print("ERROR")


prompt()
