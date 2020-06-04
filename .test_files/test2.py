import datetime
import time

def repeat_datetime():

    while(1):

        print("Datetime agora: ", datetime.datetime.now())
        time.sleep(2)

def repeat_time():
    while(1):
    
        print("Tempo agora: ", time.time())
        time.sleep(2)


if __name__ == "__main__":

    # repeat_print()
    # repeat_datetime()
    repeat_time()







