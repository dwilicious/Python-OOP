@echo off
echo "Install chocolatey dan docker"
echo "Jalankan sebagai user level Administrator"
echo "Instalasi Chocolatey"
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
echo "Instalasi Docker"
choco install docker-desktop -y