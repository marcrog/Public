from pynput.keyboard import Key, Listener

def on_press(key):
	print("" + format(key))
	if key == Key.b:
		return False

listener = Listener(on_press = on_press, on_release = None)
listener.start()
listener.join()
