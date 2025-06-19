# Emailpad
*This is a macropad designed to speed up email writing process. It has 3 buttons for commonly used email phrases and a rotary encoder to quickly switch between fields!*

## Features 

- **3 Macro Buttons:**

 Button 1 - Common email intro ("I hope this email finds you well.")
 
 Button 2 - Common closing ("Best wishes,\nRuzanna")
 
 Button 3 - Follow up reminder ("Please let me know if you have any questions")

- **Rotary encoder**

 1 Clockwise - Scroll up between email app fields (Tab)
 
 2 Counterclockwise - Scroll down between email app fields (Shift+Tab)
  
- Custom pcb (using KiCAD)
- Custom 3d model (using OnShape)
- KMK firmware (using Python)
- SK6812 MINI-E LEDs

## Images 

**CAD**

![image](https://github.com/user-attachments/assets/d9b8957b-57b3-46fe-b364-d55bb98b092f)
![image](https://github.com/user-attachments/assets/342784a7-9cd7-4535-b212-c2f1b1ea3463)
![image](https://github.com/user-attachments/assets/585fdb07-9f4b-4e72-af3e-086eed7f988e)

*Case components & fit*

![Screenshot 2025-06-18 210301](https://github.com/user-attachments/assets/8976d2ad-3cf6-4d40-adf1-66f51e12ba7f)
![Screenshot 2025-06-18 210446](https://github.com/user-attachments/assets/47689093-3b86-4b34-8ab6-cae9f01318ea)
![Screenshot 2025-06-18 210531](https://github.com/user-attachments/assets/2f3f2ab9-82e3-4e8f-be0b-c68f6cc737e1)



**PCB**

![image](https://github.com/user-attachments/assets/c05b8fe3-f023-4a5e-a9f5-3a2e648b672e)
![image](https://github.com/user-attachments/assets/eee18f38-174f-4e7b-87af-a221e1947e7b)
![image](https://github.com/user-attachments/assets/a0450140-42a5-4405-bf81-3d8e6a5416d7)
![image](https://github.com/user-attachments/assets/95dfccf1-6a43-4ddb-a079-29154c029d1e)


## Bill of Materials 
| Quantity | Material               | Description                        |
|----------|------------------------|------------------------------------|
| 1        | Seeed XIAO RP2040      | USB-C Microcontroller              |
| 3        | MX-Style switches      | Macro keys                         |
| 1        | EC11 Rotary encoder    | Tab navigation                     |
| 2        | 1N4148 Diodes          | For encoder & Microcontroller      |
| 2        | SK6812MINI-E LEDs      | Lighting                           |
| 1        | Custom PCB             | Custom printable circuit board     |
| 1        | 3d printed Case        | Enclosure for parts                |
| 4        | M3x16mm screws         | For assembly                       |

## Firmware
The firmware is writen in Python using KMK Firmware.

**Pins**

Button 1 - GP27

Button 2 - GP28

Button 3 - GP29

Encoder A - GP0

Encoder B - GP1

### Instructions

1 - Install KMK into your XIAO RP2040,

2 - Upload the firmware on the device's USB flash drive as .py,

3 - You can also customize it by substituting the email phrases with the ones you use!


*Created by Ruzanna Gaboyan!*











