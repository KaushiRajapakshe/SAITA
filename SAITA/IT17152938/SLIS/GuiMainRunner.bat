@echo off
%~d0
cd %~dp0
:loop
cmd "/c activate SLIS && python -m Gui.GuiMain && deactivate"
goto loop
pause