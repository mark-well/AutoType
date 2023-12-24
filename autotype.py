
#import pyautogui
import time

# Edit these variables to your desire
countDownDelay = 5; # this will give you time to point your cursor to whatever you want to start typing
message = "Pakyu ka!" # Message to be typed
numberOfMessages = 10 # How many message to be typed
typingSpeed = 0.5 # Typing speed in  millisecond
delayForEachMessage = 1; # 1 Second delay

#Main entry of the program
def main():
	print(f"Note: Once you press any key you have {countDownDelay} seconds delay to point your cursor to whichever you want to type in.\n")
	print(f"Message: {message}")
	print(f"Count: {numberOfMessages}")
	print("")
	
	input("Press any key to start: ")
	CountDown(countDownDelay)
	print("")
	StartTyping()

def CountDown(seconds):
	while(seconds >= 0):
		print(seconds)
		seconds -= 1;
		time.sleep(1)

def StartTyping():
	for i in range(numberOfMessages):
		#pyautogui.write(message, typingSpeed)
		#pyautogui.press("Enter")
	
		print(f"Successfully typed \"{message}\" ({i+1}/{numberOfMessages})")
		time.sleep(delayForEachMessage)

if __name__ == "__main__":
	main()