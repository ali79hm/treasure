linux bash Treasure
---

# make bash file excutable

#### Changing the user rights:
To run an executable file the user rigths of those files must be set correct. This can be done by doing the following:

 - Open a terminal
 - Browse to the folder where the executable file is stored
 - Type the following command:
   - for any . bin file: 
     ```bash
        sudo chmod +x filename.bin
     ```
   - for any .run file: 
     ```bash
        sudo chmod +x filename.run
     ```
     
 - When asked for, type the required password and press Enter

Now the file can be executed by the current user with root privileges.

#### Installing an executable file
Now the file can be run in the terminal by typing the following command in the terminal:
For any .bin file: 
  ```bash
     ./filename.bin
  ```
For any .run file: 
  ```bash
     ./filename.run
  ```