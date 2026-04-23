# 🧠 FocusBoard — Explained Like You're 5

## 🚀 What is FocusBoard?

FocusBoard is like a **magic control room inside your computer terminal**.

It helps you do 3 main things:

- 📝 Make a to-do list (like “homework”, “study”, “play”)
- 💬 Talk to other people (like a chat room)
- ⏱ Stay focused using timers (like a study clock)

Think of it like a **super desk where everything you need is in one place**.

---

## 🧩 How FocusBoard Works (Simple Version)

Imagine FocusBoard is a small city:

### 🟦 core/ = The Brain
This is where rules live.

It decides:
- what a user is
- what a message is
- how tasks are saved

👉 It does NOT show anything on screen  
It just “thinks”

---

### 🟩 server/ = The Mailman
This part delivers messages between people.

If you send a chat:
- server receives it
- server gives it to everyone else

👉 It is like a post office for messages

---

### 🟨 client/ = The Screen You See
This is the actual app you use.

It shows:
- your tasks
- your chat
- your timer

👉 This is what you “look at and press buttons on”

---

### 🟪 data/ = The Notebook
This is where everything is written down:
- users
- messages
- tasks

👉 Even if the app closes, this remembers things

---

## 🌐 How Everything Talks

Here is the flow:

1. You type a message in FocusBoard
2. The client sends it to the server
3. The server gives it to other users
4. Everyone sees it on their screen

It’s like:
> ✉️ writing a note → postman delivers it → friends read it

---

## ⚠️ Important Rules (No Breaking Stuff)

To keep FocusBoard working:

### 🚫 Don’t mix parts
- client must NOT talk directly to data files
- server must NOT control the screen
- core must NOT show UI

Each part has ONE job only.

---

## 🧠 What Each Part Thinks It Is

- core → “I understand everything”
- server → “I deliver messages”
- client → “I show everything to the user”
- data → “I remember everything”

---

## 🎯 What FocusBoard Wants to Become

One day, FocusBoard will be:

- a place to work
- a place to chat
- a place to focus
- all in one screen

Like a **mini operating system inside the terminal**

---

## 🧪 Current Status

Right now:
- structure is ready ✔
- code is NOT built yet ❌
- brain/server/client still need to be created

---

## 🚀 Final Idea

FocusBoard is like:

> “A school desk where your notebook, phone, timer, and friends all exist together in one place.”

---