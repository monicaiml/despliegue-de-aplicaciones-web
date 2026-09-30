from userfnc import get_name
from alert import print_alert

if __name__ == "__main__":
    name = get_name()
    print(name)
    if name == "HACKERMAN":
        print_alert()