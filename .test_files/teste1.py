import multiprocessing
import test2
import time



init = time.monotonic()

if __name__ == "__main__":  # confirms that the code is under main function
    # names = ['America', 'Europe', 'Africa']
    procs = []
    print("Aqui 1")
    proc = multiprocessing.Process(name='proc', target=test2.repeat_datetime)  # instantiating without any argument
    proc2 = multiprocessing.Process(name='proc2', target=test2.repeat_time)
    procs.append(proc)
    procs.append(proc2)
    # print("Aqui 2")
    proc.start()
    proc2.start()
    # proc.join()
    # proc2.join()
    # proc.
    print("Elapsed: ",time.monotonic() - init)

    # instantiating process with arguments
    # for name in names:
    #     # print(name)
    #     proc = Process(target=print_func, args=(name,))
    #     procs.append(proc)
    #     proc.start()

    # complete the processes
    time.sleep(3)

    # proc.join()
    # proc2.join()
    while((time.monotonic() - init) < 10):pass
        # print("Elapsed: ", time.monotonic() - init)

    print("Aqui ó")
    
    proc.terminate()
    proc2.terminate()

    print("Hell yeah")