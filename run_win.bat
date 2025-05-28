@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Add-Type -AssemblyName System.Windows.Forms; $WShell = New-Object -ComObject WScript.Shell; while ($true) { $WShell.SendKeys('{SCROLLLOCK}'); Start-Sleep -Seconds 60 }"
