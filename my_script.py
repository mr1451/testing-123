# testing-123/my_script.py

def enlarge(i):
    return i * 100

# need to remove from global scope in order to import other things from this script
if __name__ == "__main__":
    my_number = float(input("Please input a number."))
   #n = enlarge(8)
    n = enlarge(my_number)
    print("ENLARGING THE NUMBER:", n) 