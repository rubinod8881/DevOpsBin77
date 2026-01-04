import os
import time

def clear_screen():
    # Clears terminal for Windows (cls) or Mac/Linux (clear)
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_diamond(max_size):
    while True: # Loop forever
        # Grow the diamond
        for size in range(1, max_size + 1):
            clear_screen()
            # Top half
            for i in range(size):
                print(" " * (max_size - i) + "*" * (2 * i + 1))
            # Bottom half
            for i in range(size - 2, -1, -1):
                print(" " * (max_size - i) + "*" * (2 * i + 1))
            time.sleep(0.1) # Pause for 0.1 seconds

        # Shrink the diamond
        for size in range(max_size - 1, 0, -1):
            clear_screen()
            for i in range(size):
                print(" " * (max_size - i) + "*" * (2 * i + 1))
            for i in range(size - 2, -1, -1):
                print(" " * (max_size - i) + "*" * (2 * i + 1))
            time.sleep(0.1)

# Run the animation with a max height of 10
animate_diamond(10)