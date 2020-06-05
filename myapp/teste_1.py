import sys
import os
sys.path.insert(1,"/home/pinto/Documentos/repos/LTIs200simulator/teste_scripts")
import teste4

def print_data(input):
        for i in range(len(input)):
                print(input[i])


def chang_stdout():
        filename = os.path.join(os.path.dirname(__file__), "out.txt")

        sys.stdout = open(filename, "a")

if __name__ == "__main__":
    chang_stdout()
    print("__file__ is", __file__)
    te = teste4.TestSelf(5, 4)
    print_data([0,1,2,3])


    print("Teste soma:")
    print(te.soma(c=1))
    print(te.a)
