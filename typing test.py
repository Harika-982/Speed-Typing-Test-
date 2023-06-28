import time

def run_speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)
    input("Press Enter when you are ready to start.")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_per_minute = calculate_words_per_minute(user_input, elapsed_time)
    
    print("Your typing speed: {:.2f} words per minute.".format(words_per_minute))
    

def calculate_words_per_minute(user_input, elapsed_time):
    words_typed = len(user_input.split())
    minutes_elapsed = elapsed_time / 60
    words_per_minute = words_typed / minutes_elapsed
    return words_per_minute


if __name__ == "__main__":
    run_speed_typing_test()
