import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Number1",help ="First number")
    parser.add_argument("Number2", help="second number")
    parser.add_argument("operation",help="operation, operation i support is add ,multipilcation ,division ,subtraction")


args = parser.parse_args()
print("Argument 1 is "+ args.Number1)
print("Argument 2 is "+args.Number2)


if args.operation == "add":
    result = int(args.Number1) + int(args.Number2)
    abc = "string 1 " + "string 2"
    print("Combined string is  :" + abc)
    print("operation is addition and the value is  : " + str(result))


elif args.operation == 'multiplication':
     result = int(args.Number1) * int(args.Number2)

     print("operation is multiplication and the value is : " + str(result))

elif args.operation == "division":
    #result = float(args.Number1) / float(args.Number2) (This line is printing only tuncanted values so fixing the bug hence changing fro int to float

    result = float(args.Number1) / float(args.Number2)
    print("operation is division  and the value is : " + str(result))

elif args.operation == "subtraction":
    result = int(args.Number1) - int(args.Number2)
    print("operation is subtraction   and the value is : " + str(result))

else:
    print("i dont understand operation you have specified. Operation you have specified " +args.operation +" is unknown.")

