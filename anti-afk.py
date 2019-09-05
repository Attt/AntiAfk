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
	logoutShortcutAscii = 0x31
	logoutGap = 540
	needChangeCharacter = 'y'
	wowWindow = WowWindow()
	def killTime(self):
		self.wowWindow.setWowForeground()
		# press 'SPACE'
		win32api.keybd_event(0x20,0,0,0)
		time.sleep(random.randint(1, 2))
		win32api.keybd_event(0x20,0,win32con.KEYEVENTF_KEYUP,0)
		time.sleep(random.randint(4, 5))
		
	# run macro '/logout'
	def logOutUsingCommand(self):
		self.wowWindow.setWowForeground()
		win32api.keybd_event(self.logoutShortcutAscii,0,0,0)
		win32api.keybd_event(self.logoutShortcutAscii,0,win32con.KEYEVENTF_KEYUP,0)
		
	def changeAnotherCharacter(self):
		# press 'down'
		self.wowWindow.setWowForeground()
		win32api.keybd_event(0x28,0,0,0)
		win32api.keybd_event(0x28,0,win32con.KEYEVENTF_KEYUP,0)	
		
	def logIn(self):
		# press 'enter'
		self.wowWindow.setWowForeground()
		win32api.keybd_event(0x0d,0,0,0)
		win32api.keybd_event(0x0d,0,win32con.KEYEVENTF_KEYUP,0)	
		
	def antiAfk(self):
		# get window hanlder and set forground
		hwnd = self.wowWindow.setWowForeground()
		
		self.wowWindow.setWowForeground()
		time.sleep(0.5)
		
		i = 0
		# calculate looping times
		t = int(self.logoutGap / 6)
		while i < t:
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
		if self.needChangeCharacter == 'y':
			self.changeAnotherCharacter()
		
		#take a break
		time.sleep(1)
		
		# log in
		self.logIn()

		# waiting for log in
		time.sleep(10)

	def printSettings(self):
		print("当前默认设置为:")
		print("->>\t是否需要切换角色:", '是' if self.needChangeCharacter =='y' else '否')
		print("->>\tlogout宏的快捷键为:", chr(self.logoutShortcutAscii))
		print("->>\t小退的间隔时间大约为:", self.logoutGap, '秒')
		print("")
		
	def settings(self):
		self.printSettings()
		reSetting = input("是否需要重新设置？(y/n):")
		
		if reSetting == 'y':
			print("")
			self.needChangeCharacter = input("是否需要切换角色？(y/n):")
			c = '\b单角色模式'
			if self.needChangeCharacter == 'y':
				c = '\b多角色模式'
			print('->>设置为',c)
			print("")
			
			sc = input("logout宏的快捷键为:")
			self.logoutShortcutAscii = ord(sc)
			print('->>快捷键设置为', sc)
			print("")
			
			self.logoutGap = int(input("小退的间隔时间大约需要设置为（秒）:"))
			if self.logoutGap < 6:
				self.logoutGap = 6
			print("")
			print('间隔时间设置为', self.logoutGap)
		print("")
		self.printSettings()
		print('->>设置完成，准备开始...')
		
	def invoke(self):
		self.settings()
		while True: 
			self.antiAfk()
			

#invoke
main = AntiAfk()
main.invoke()