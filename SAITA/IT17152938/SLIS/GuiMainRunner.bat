@echo off
:loop
cmd "/c activate SLIS && python -m Gui.GuiMain && deactivate"
goto loop
pause