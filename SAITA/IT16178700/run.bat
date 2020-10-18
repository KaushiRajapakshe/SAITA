@echo off
%~d0
cd %~dp0
cmd "/c activate saita_psai && python -m GUI.InstalledApplicationIssueGUI && deactivate"
pause