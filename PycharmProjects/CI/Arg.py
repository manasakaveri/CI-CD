def print_two(*args):
    arg1 ,arg2 =args
    print(f"arg1:{arg1},arg2 : {arg2 }")

# ok ,thatt *args is actually pointless,we an just do this

def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2 : {arg2}")

#this just takes one argument
def print_one(arg1 ):
    print(f"arg1:{arg1}")

#this one takes no arguments
def print_none():
    print("I got nothing")


print_two("Manasa","Aditi")
print_two_again("Manasa","Aditi")
print_one("First !")
print_none()
