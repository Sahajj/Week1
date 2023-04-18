import threading

def count_up_to(n):
    for i in range(n):
        print(i)

if __name__ == '__main__':
    # Create two threads to count up to 10
    thread1 = threading.Thread(target=count_up_to, args=(10,))
    thread2 = threading.Thread(target=count_up_to, args=(10,))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the threads to finish
    thread1.join()
    thread2.join()
