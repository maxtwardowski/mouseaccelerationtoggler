#THIS SCRIPT ENABLES/DISABLES 'ENHANCE POINTER PRECISION' FEATURE IN MOUSE SETTINGS ON WINDOWS OS
#!/usr/bin/env python
from pywinauto.application import Application

#opening the Mouse Properties app
app = Application().Start(cmd_line=u'"C:\\WINDOWS\\System32\\rundll32.exe" C:\\WINDOWS\\System32\\shell32.dll,Control_RunDLL C:\\WINDOWS\\System32\\main.cpl')

#accessing tabs in the window
mouseproperties_window = app.Dialog
mouseproperties_tabs = mouseproperties_window.TabControl

#switching to Pointer Options tab
mouseproperties_tabs.Select(u'Pointer Options')

#toggling the Enhance Pointer Position checkbox
checkbox_enhancepointer = mouseproperties_window.CheckBox
checkbox_enhancepointer.Click()

#saving changes and closing the app
button_OK = mouseproperties_window.OK
button_OK.Click()
app.kill()
