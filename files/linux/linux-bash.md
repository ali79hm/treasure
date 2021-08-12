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

# colors in bash files

The ANSI/VT100 terminals and terminal emulators are not just able to display black and white text ; they can display colors and formatted texts thanks to escape sequences. Those sequences are composed of the Escape character (often represented by ```^[``` or ```<Esc>```) followed by some other characters: ```<Esc>[FormatCodem```.

In Bash, the <Esc> character can be obtained with the following syntaxes:

\e

\033

\x1B

### formating 
  
| Description                                           | Escape character | Example                                    |     |
|-------------------------------------------------------|------------------|--------------------------------------------|-----|
| Bold/Bright                                           |```\e[1m```| ```echo   -e   "Normal \e[1mBold"```       | ![](linux-bash/pic/linux-bash-bold.png) |
| Dim                                                   |```\e[2m```| ```echo   -e   "Normal \e[2mDim"```        | ![](linux-bash/pic/linux-bash-dim.png)    |
| Underlined                                            |```\e[4m```| ```echo   -e   "Normal \e[4mUnderlined"``` | ![](linux-bash/pic/linux-bash-underline.png)    |
| Blink                                                 |```\e[5m```| ```echo   -e   "Normal \e[5mBlink"```      | ![](linux-bash/pic/linux-bash-blink.gif)    |
| Reverse (invert the foreground and background colors) |```\e[7m```| ```echo   -e   "Normal \e[7minverted"```   | ![](linux-bash/pic/linux-bash-reverse.png)    |
| Hidden (useful for passwords)                         |```\e[8m```| ```echo   -e   "Normal \e[8mHidden"```     | ![](linux-bash/pic/linux-bash-hidden.png)   |


### reset 

| Description          | Escape character | Example                                                 | Preview |
|----------------------|------------------|---------------------------------------------------------|---------|
| Reset all attributes |```\e[0m```| ```echo   -e   "\e[0mNormal Text"```                    | ![](linux-bash/pic/linux-bash-reset.png)        |
| Reset bold/bright    |```\e[21m```| ```echo   -e   "Normal \e[1mBold \e[21mNormal"```       | ![](linux-bash/pic/linux-bash-reset-bold.png)        |
| Reset dim            |```\e[22m```| ```echo   -e   "Normal \e[2mDim \e[22mNormal"```        | ![](linux-bash/pic/linux-bash-reset-dim.png)        |
| Reset underlined     |```\e[24m```| ```echo   -e   "Normal \e[4mUnderlined \e[24mNormal"``` | ![](linux-bash/pic/linux-bash-reset-underline.png)        |
| Reset blink          |```\e[25m```| ```echo   -e   "Normal \e[5mBlink \e[25mNormal"```      | ![](linux-bash/pic/linux-bash-reset-blink.gif)        |
| Reset reverse        |```\e[27m```| ```echo   -e   "Normal \e[7minverted \e[27mNormal"```   | ![](linux-bash/pic/linux-bash-reset-reverse.png)         |
| Reset hidden         |```\e[28m```| ```echo   -e   "Normal \e[8mHidden \e[28mNormal"```     | ![](linux-bash/pic/linux-bash-reset-hidden.png)       |

### color

#### forground color

| Description              | Escape character | Example                                         | Preview |
|--------------------------|------------------|-------------------------------------------------|---------|
| Default foreground color | ```\e[39m```     | ```echo   -e   "Default \e[39mDefault"```       |  ![](linux-bash/pic/linux-bash-color-default.png) |
| Black                    | ```\e[30m```     | ```echo   -e   "Default \e[30mBlack"```         |  ![](linux-bash/pic/linux-bash-color-black.png)        |
| Red                      | ```\e[31m```     | ```echo   -e   "Default \e[31mRed"```           |  ![](linux-bash/pic/linux-bash-color-red.png)       |
| Green                    | ```\e[32m```     | ```echo   -e   "Default \e[32mGreen"```         |  ![](linux-bash/pic/linux-bash-color-green.png)       |
| Yellow                   | ```\e[33m```     | ```echo   -e   "Default \e[33mYellow"```        |  ![](linux-bash/pic/linux-bash-color-yellow.png)       |
| Blue                     | ```\e[34m```     | ```echo   -e   "Default \e[34mBlue"```          |  ![](linux-bash/pic/linux-bash-color-blue.png)       |
| Magenta                  | ```\e[35m```     | ```echo   -e   "Default \e[35mMagenta"```       |  ![](linux-bash/pic/linux-bash-color-magenta.png)       |
| Cyan                     | ```\e[36m```     | ```echo   -e   "Default \e[36mCyan"```          |  ![](linux-bash/pic/linux-bash-color-cyan.png)       |
| Light gray               | ```\e[37m```     | ```echo   -e   "Default \e[37mLight gray"```    |  ![](linux-bash/pic/linux-bash-color-light-gray.png)       |
| Dark gray                | ```\e[90m```     | ```echo   -e   "Default \e[90mDark gray"```     |  ![](linux-bash/pic/linux-bash-color-dark-gray.png)       |
| Light red                | ```\e[91m```     | ```echo   -e   "Default \e[91mLight red"```     |  ![](linux-bash/pic/linux-bash-color-light-red.png)       |
| Light green              | ```\e[92m```     | ```echo   -e   "Default \e[92mLight green"```   |  ![](linux-bash/pic/linux-bash-color-light-green.png)      |
| Light yellow             | ```\e[93m```     | ```echo   -e   "Default \e[93mLight yellow"```  |  ![](linux-bash/pic/linux-bash-color-light-yellow.png)       |
| Light blue               | ```\e[94m```     | ```echo   -e   "Default \e[94mLight blue"```    |  ![](linux-bash/pic/linux-bash-color-light-blue.png)       |
| Light magenta            | ```\e[95m```     | ```echo   -e   "Default \e[95mLight magenta"``` |  ![](linux-bash/pic/linux-bash-color-light-magenta.png)       |
| Light cyan               | ```\e[96m```     | ```echo   -e   "Default \e[96mLight cyan"```    |  ![](linux-bash/pic/linux-bash-color-light-cyan.png)       |
| White                    | ```\e[97m```     | ```echo   -e   "Default \e[97mWhite"```         |  ![](linux-bash/pic/linux-bash-color-white.png)       |

#### background color

| Description              | Escape character | Example                                         | Preview |
|--------------------------|------------------|-------------------------------------------------|---------|
| Default foreground color | ```\e[39m```     | ```echo   -e   "Default \e[39mDefault"```       | ![](linux-bash/pic/linux-bash-bgcolor-default.png)        |
| Black                    | ```\e[30m```     | ```echo   -e   "Default \e[30mBlack"```         |  ![](linux-bash/pic/linux-bash-bgcolor-black.png)       |
| Red                      | ```\e[31m```     | ```echo   -e   "Default \e[31mRed"```           |  ![](linux-bash/pic/linux-bash-bgcolor-red.png)       |
| Green                    | ```\e[32m```     | ```echo   -e   "Default \e[32mGreen"```         |  ![](linux-bash/pic/linux-bash-bgcolor-green.png)       |
| Yellow                   | ```\e[33m```     | ```echo   -e   "Default \e[33mYellow"```        |  ![](linux-bash/pic/linux-bash-bgcolor-yellow.png)       |
| Blue                     | ```\e[34m```     | ```echo   -e   "Default \e[34mBlue"```          |  ![](linux-bash/pic/linux-bash-bgcolor-blue.png)       |
| Magenta                  | ```\e[35m```     | ```echo   -e   "Default \e[35mMagenta"```       |  ![](linux-bash/pic/linux-bash-bgcolor-magenta.png)       |
| Cyan                     | ```\e[36m```     | ```echo   -e   "Default \e[36mCyan"```          |  ![](linux-bash/pic/linux-bash-bgcolor-cyan.png)       |
| Light gray               | ```\e[37m```     | ```echo   -e   "Default \e[37mLight gray"```    |  ![](linux-bash/pic/linux-bash-bgcolor-light-gray.png)       |
| Dark gray                | ```\e[90m```     | ```echo   -e   "Default \e[90mDark gray"```     |  ![](linux-bash/pic/linux-bash-bgcolor-dark-gray.png)       |
| Light red                | ```\e[91m```     | ```echo   -e   "Default \e[91mLight red"```     |  ![](linux-bash/pic/linux-bash-bgcolor-light-red.png)       |
| Light green              | ```\e[92m```     | ```echo   -e   "Default \e[92mLight green"```   |  ![](linux-bash/pic/linux-bash-bgcolor-light-green.png)       |
| Light yellow             | ```\e[93m```     | ```echo   -e   "Default \e[93mLight yellow"```  |  ![](linux-bash/pic/linux-bash-bgcolor-light-yellow.png)       |
| Light blue               | ```\e[94m```     | ```echo   -e   "Default \e[94mLight blue"```    |  ![](linux-bash/pic/linux-bash-bgcolor-light-blue.png)       |
| Light magenta            | ```\e[95m```     | ```echo   -e   "Default \e[95mLight magenta"``` |  ![](linux-bash/pic/linux-bash-bgcolor-light-magenta.png)       |
| Light cyan               | ```\e[96m```     | ```echo   -e   "Default \e[96mLight cyan"```    |  ![](linux-bash/pic/linux-bash-bgcolor-light-cyan.png)       |
| White                    | ```\e[97m```     | ```echo   -e   "Default \e[97mWhite"```         |  ![](linux-bash/pic/linux-bash-bgcolor-white.png)       |