import multiprocessing
import threading

def square_numbers(numbers):
    results = []
    for n in numbers:
        results.append(n ** 2)
    return results

def count_up_to(n):
    for i in range(n):
        print(i)

if __name__ == '__main__':
    # Create a list of numbers to square
    numbers = list(range(1, 101))

    # Create a multiprocessing pool with 4 processes
    pool = multiprocessing.Pool(processes=4)

    # Map the square_numbers function onto the list of numbers using the pool
    results = pool.map(square_numbers, [numbers])

    # Create two threads to count up to 10
    thread1 = threading.Thread(target=count_up_to, args=(10,))
    thread2 = threading.Thread(target=count_up_to, args=(10,))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the threads to finish
    thread1.join()
    thread2.join()

    # Print the results
    print(results)
