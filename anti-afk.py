import win32api,win32con,win32gui
import time,random

class WowWindow:
	def setWowForeground(self):
		# get WOW window
		classname = "GxWindowClass"
		titlename = "魔兽世界"
		# get window hanlder
		hwnd = win32gui.FindWindow(classname, titlename)
		win32gui.SetForegroundWindow(hwnd)
		return hwnd

class AntiAfk:
	wowWindow = WowWindow()
	def killTime(self):
		self.wowWindow.setWowForeground()
		buttonList = [0x58, 0x20]
		random.shuffle(buttonList)
		for btn in buttonList:
			win32api.keybd_event(btn,0,0,0)
			time.sleep(random.randint(1, 2))
			win32api.keybd_event(btn,0,win32con.KEYEVENTF_KEYUP,0)
		time.sleep(random.randint(4, 5))
		
	def clickMenu(self,x, y):
		#set position
		win32api.SetCursorPos((x, y))
		#left click
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
							 win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
							 
	def logOut(self, top, bottom, right, left):
		centerX = (right + left) / 2
		centerY = (bottom + top) / 2
		height = bottom - top
		width = right - left
		print('log out, now height is',height,'width is',width,',center point is (', centerX, centerY, ')')
		factor = 0.088
		if height < 400:
			factor = 0.10
		downOff = height * factor
		self.wowWindow.setWowForeground()
		#ESC
		win32api.keybd_event(0x1B,0,0,0)
		win32api.keybd_event(0x1B,0,win32con.KEYEVENTF_KEYUP,0)
		time.sleep(0.5)
		self.clickMenu(int(centerX),int(centerY + downOff))
	
	# put macro '/logout' in '1'
	def logOutUsingCommand(self):
		self.wowWindow.setWowForeground()
		print('log out using /logout')
		win32api.keybd_event(0x31,0,0,0)
		win32api.keybd_event(0x31,0,win32con.KEYEVENTF_KEYUP,0)
		
	def changeAnotherCharacter(self):
		# press 'down'
		self.wowWindow.setWowForeground()
		print('change another character')
		win32api.keybd_event(0x28,0,0,0)
		win32api.keybd_event(0x28,0,win32con.KEYEVENTF_KEYUP,0)	
		
	def logIn(self):
		# press 'enter'
		self.wowWindow.setWowForeground()
		print('log in')
		win32api.keybd_event(0x0d,0,0,0)
		win32api.keybd_event(0x0d,0,win32con.KEYEVENTF_KEYUP,0)	
		
	def antiAfk(self):
		# get window hanlder and set forground
		hwnd = self.wowWindow.setWowForeground()
		# get window edge offsets
		left, top, right, bottom = win32gui.GetWindowRect(hwnd)
		
		print('window offsets are changed to', left, top, right, bottom)
		centerX = (right + left) / 2
		centerY = (bottom + top) / 2
		print('center point is (', centerX, centerY, ')')
		
		self.wowWindow.setWowForeground()
		time.sleep(0.5)
		
		print('kill time...')
		i = 0
		while i < 90:
			self.killTime()
			i = i + 1
		
		#take a break
		time.sleep(0.5)
		
		self.wowWindow.setWowForeground()
		
		#log out to select menu
		#self.logOut(top, bottom, right, left)
		self.logOutUsingCommand()
		
		#waiting for character selection screen
		time.sleep(random.randint(30, 35))
		
		# change character
		self.changeAnotherCharacter()
		
		#take a break
		time.sleep(1)
		
		# log in
		self.logIn()

		# waiting for log in
		time.sleep(10)

	def invoke(self):
		while True: 
			self.antiAfk()
			

#invoke
main = AntiAfk()
main.invoke()