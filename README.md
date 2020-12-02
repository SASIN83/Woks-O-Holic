# Woks-O-Holic
This is an attempt to combine Virtual and physical environment to tackle Mental and physical health problem. 
_Work-O-Holic_ is a free desktop app that addresses the mental health by providing the user an interface that guides users through activities at certain interval of time, which is selected by studying various sources. 
**It has following activities:**
    1. Short Exercises
    2. Reads jokes, quotes and facts
    3. Suggests books to read
    4. Stress Press

All above activities are spoken by the Application thus user can just work without worrying about the time. Other than just activities above it provides an option, if user has medicine to be taken while they are busy at work, they can just set time to take medicine and Application will just remind the user by voice.

This app also provide a medium through **Instagram**, if they need some consultation regarding mental health they can just click the button and they can talk to the **Consultant** on Instagram.

## How I built it
OS used: **Windows**
Programming Language: **Python**
Libraries/Packages: **tkinter, requests, datetime, pyttsx3, time, webbrowser, threading.**
Methods: **Class, Multi-threading, Text-to-Speech, sleep, API calls**
APIs used for reading materials: **ICnDB**(Jokes)**, Foresmatic**(Quotes)**, OpenLibrary**(Book Suggestions).
IDE/ TextEditor: **VS-Code, Python IDLE**

[Foresmatic API](http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en)

[Openlibrary API](https://openlibrary.org/books)

[ICnDB API](http://api.icndb.com/jokes/random)

As it is a basic application made with Python, which might be not responding sometimes, it is converted to **.exe** using Commend line interface of PyInstaller, so that if it crashes or starts not responding, user can close the program by closing the Command Prompt opened with it.
