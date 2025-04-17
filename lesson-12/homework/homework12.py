import threading
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check primes in a given range
def check_primes(start, end, result_list):
    primes = [n for n in range(start, end) if is_prime(n)]
    result_list.extend(primes)

# Function to divide the range among threads and collect results
def threaded_prime_checker(start, end, num_threads):
    thread_list = []
    results = []
    step = (end - start) // num_threads

    for i in range(num_threads):
        thread_start = start + i * step
        thread_end = start + (i + 1) * step if i != num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, results))
        thread_list.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in thread_list:
        thread.join()

    return sorted(results)

# Example usage
start = 1
end = 100
num_threads = 4
primes = threaded_prime_checker(start, end, num_threads)
print(f"Prime numbers between {start} and {end}: {primes}")

import threading
from collections import defaultdict

# Function to count words in a chunk of text
def count_words_in_chunk(start, end, lines, word_count_dict):
    local_word_count = defaultdict(int)
    for line in lines[start:end]:
        words = line.split()
        for word in words:
            local_word_count[word.lower()] += 1
    
    # Update the global word count dictionary
    with threading.Lock():
        for word, count in local_word_count.items():
            word_count_dict[word] += count

# Function to process the file with multiple threads
def threaded_file_processing(file_name, num_threads):
    word_count_dict = defaultdict(int)
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    thread_list = []
    chunk_size = len(lines) // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words_in_chunk, args=(start, end, lines, word_count_dict))
        thread_list.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in thread_list:
        thread.join()

    return word_count_dict

# Example usage
file_name = 'large_text_file.txt'  # Replace with your actual file path
num_threads = 4
word_counts = threaded_file_processing(file_name, num_threads)

# Print word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")
