# JPL_Modified_OSR
Developed to work with JPL's Open Source Rover project

The code supplied by JPL didn't work initialy and it took weeks of troublshooting and following instrictions from the TapTalk forum and JPL's GutHub Issues page., which were invaluable in making the rover work. After making it work, the code had some issues and was hard to read. Therefore, I rewrote the code to run more efficiently and be easier to modify. Attached are the working JPL code (Working OSR Code) and my custom code (Custom_Rover_Code).

## Working OSR Code
Installing the osr code is easy, just follow the instructions from JPL but replace the files in the 'Working OSR Code' folder.

## Costom Rover Code
To use this code, download this folder and put it in the /home/pi folder. After that, type in the command 'sudo nano /etc/rc.local' and run it. Right above 'exit 0', type in the code 'python /home/pi/Custom_Rover_Code/Main.py' and press controll+x, y, and enter to save the edit. After that, the code should run on bootup.
