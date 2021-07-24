import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Start gen_freq_list function
print("At what frequency do you want to start?")
#start_freq = int(input())
start_freq = 10000
print("At what frequency do you want to end?")
#end_freq = int(input())
end_freq = 15000
print("How many Hertz do you want each subsequential frequency to change?")
#step = int(input())
step = 1

def gen_freq_list(start_freq, end_freq, step):
    freq_list = []
    for freq in range(start_freq, end_freq, step):
        freq_list.append(str(freq)[2:])
    print(freq_list)
    return(freq_list)

freq_list = gen_freq_list(start_freq, end_freq + 1, step)

# Send the freq-value by cycling through all gen_freq_list values
# Amount of time between different frequencies is inputted to time_to_next

print("How many seconds do you want there to be between each subsequential frequency?")
#time_to_next = int(input())
time_to_next = 60

# Select Firefox as webdriver
driver = webdriver.Firefox()

# Open website
driver.get("https://generalfuzz.net/acrn/")

# Click "Sequence" button
#seq_button = driver.find_element_by_class_name(".btn.btn-default.active")
#seq_button.click()
# Click "Play Pattern" button
#play_pattern_button = driver.find_element_by_class_name(".btn-succes.btn-lg.btn-default")
#play_patter_button.click()

# Select the freq-value input box
freq_value_box = driver.find_element_by_class_name("freq-value")

# Start freq_list_index at 0
freq_list_index = 0
while True:
    if freq_list_index == 0:
        freq_value_box.send_keys(Keys.BACKSPACE)
        freq_value_box.send_keys(Keys.BACKSPACE)


        freq_value_box.send_keys(freq_list[freq_list_index])
        freq_list_index += 1

        #print(freq_list_index)
        #print(freq_list[freq_list_index])

        time.sleep(time_to_next)

    else:
        freq_value_box.send_keys(Keys.BACKSPACE)
        freq_value_box.send_keys(Keys.BACKSPACE)
        freq_value_box.send_keys(Keys.BACKSPACE)

        freq_value_box.send_keys(freq_list[freq_list_index])
        freq_list_index += 1

        #print(freq_list_index)
        #print(freq_list[freq_list_index])

        time.sleep(time_to_next)
