# Mouth Shader Tool
Mouth shader (fake shadow) tool for Maya, written in Python 3

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Hello animators! 

Do you want a simple way to add depth to your character's mouth in the polish phase of your shot? 
Do you always want to darken the inside of the mouth so the teeth and tongue stand out? - Maybe this will help??

This tool creates a simple gradient shader material and assigns it to a plane. 
The plane can then be placed at the back of a character's mouth (behind the tongue), 
to help create depth when the mouth is open.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
MOUTH SHADER TOOL
(mouthShader_tool.py)
Version 1.2.1 / 28/11/24

Tool created by James Boyle (@JamesBAnim)
Original idea inspired by Charles Icay (@IkHandle)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LICENSE MIT
Copyright (c) 2024 James Boyle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
INSTALLATION
Copy this file into your maya scripts directory, for example:

WIN - C:/Documents and Settings/user/My Documents/maya/scripts/mouthShader_tool.py
MACOS - /Users/user/Library/Preferences/Autodesk/maya/scripts/mouthShader_tool.py

Run the tool from python command line or shelf button by 
importing the module, and then calling the primary function:

    import mouthShader_tool
    mouthShader_tool.run()

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
ICON
Copy the icon JPG (mouthShader_tool.jpg) to the icon folder in your maya prefs, for example:

WIN - C:/Documents and Settings/user/My Documents/maya/2024/prefs/icons/mouthShader_tool.jpg
MACOS - /Users/name/Library/Preferences/Autodesk/maya/2024/prefs/icons/mouthShader_tool.jpg

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
COMPATIBILITY
Python 3
Maya 2022 - 2024

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DESCRIPTION
This tool creates a simple gradient shader material and assigns it to a plane. 
The plane can be placed at the back of a character's mouth (behind the tongue), 
to help create depth when the mouth is open.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
HOW TO USE


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
