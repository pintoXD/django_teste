import sys

def print_data(input):
        for i in range(len(input)):
                print(input[i])


def chang_stdout():

    sys.stdout = open("out.txt", "a")

if __name__ == "__main__":
    chang_stdout()
    print_data([0,1,2,3])
