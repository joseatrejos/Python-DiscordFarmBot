from pynput.keyboard import Key, Controller
import time
import random
import os

keyboard = Controller()

timeout = 60*300   # 5 hours time in seconds
timeout_start = time.time()
counter = 0

while time.time() < timeout_start + timeout:

    # Generate randomNumber
    #randomNumber = random.randint(1,999)
    time.sleep(1.5)

    # Write farm message
    keyboard.type("Ando farmeando")
    print("I wrote 'Ando farmeando'")

    # Wait a minute to send the message (Except for the 1st time)
    if(counter > 0):
        time.sleep(65)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print("I sent the farming message")

    # Add to the counter
    counter += 1

    # After 5 messages, request rank and print iteration number
    if(counter % 5 == 0):

        # Write !rank
        time.sleep(1)
        keyboard.type("!rank")
        print("I asked for your rank")

        # Press Enter
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("I sent the !rank message")

        if(counter >= 250):
            # Print shutdown message
            print('I will now turn off the PC after iteration' + str(counter))
            keyboard.type("Voy a apagar la compu, esta fue la iteración #" + str(counter))
            time.sleep(0.25)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            os.system('shutdown -s')
        else:
            # Print current iteration
            print('Now in iteration #' + str(counter))
            keyboard.type("Voy en la iteración " + str(counter))
            time.sleep(0.25)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
