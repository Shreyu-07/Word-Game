## 🕵️‍♂️ Word Guessing Game in Python (Two Player Game)
### 🎮 **A Fun Word Guessing Game Using Python's `getpass` & `random` Library**

---

## 📜 **Description**
This is a **two-player word guessing game** built using **Python** where:  
- One player (`Typer`) enters a **hidden word** that is shuffled.  
- The second player (`Guesser`) must guess the original word based on the shuffled letters.  
- If the **Guesser guesses correctly**, they win! 🎉  
- If not, the correct word is revealed. ❌  
- The game allows you to play **multiple rounds** until you decide to quit.  

---

![game of words](https://github.com/user-attachments/assets/fe10ea95-b047-4990-be12-5d984d51567c)


## ✅ **Features**
### 🎮 1. Hidden Word Typing
- The **Typer** enters the word **without showing it** using Python's `getpass` library.
- The word appears as `*****` instead of showing actual letters.

---

### 🔀 2. Random Word Shuffling
- The word is **shuffled randomly** using Python's `random.shuffle()` function.
- The **Guesser** has to guess the original word from the shuffled letters.

---

### 💯 3. Guess Verification
- If the **Guesser** guesses the word correctly, a congratulation message appears. 🎉  
- If the **Guesser** fails, the correct word is revealed.

---

### 🔁 4. Multiple Rounds
- After each round, the game **asks if you want to continue** (`Yes/No`).
- You can play **as many rounds** as you want.

---

### ⏱ 5. Smooth Delay Effect
- Added a `time.sleep()` delay to create a smooth gaming effect between inputs and outputs.

---

## 💻 **Technologies Used**
| Technology     | Purpose                                  |
|----------------|-------------------------------------------|
| **Python 3.x** | Main language used                       |
| **getpass**    | To hide the input from the Typer          |
| **random**     | To shuffle the word                       |
| **time**       | To add a delay in the game experience     |

---

## 📜 **Code Structure**
The code is designed as follows:  

```
Word-Guessing-Game
│
├── guessing_game.py    <-- Main Python file
├── README.md           <-- This Readme file
```

---

## 📜 **How To Play?**
### ✅ Step 1: Clone This Repository
Open your terminal and run:  
```bash
git clone https://github.com/Shreyu-07/Word-Game.git
cd Word-Game
```

---

### ✅ Step 2: Run The Game
Run the Python file using:  
```bash
python Word-Game.py
```

---

### ✅ Step 3: Enter Player Names
You will be asked to enter:  
- The **Typer's name** (who will type the word)  
- The **Guesser's name** (who will guess the word)  

Example:  
```
:: Enter the Typer name : Shreyas
:: Enter the Guesser name : Mahesh
```

---

### ✅ Step 4: Start The Game
- The **Typer** will type a hidden word (like `apple`) using a hidden input field.  
- The word will be shuffled like: `lpape`.  
- The **Guesser** must guess the original word.  

Example:  
```
The shuffled word is: lpape
Mahesh, it's your turn to guess the word!
Enter your guess: apple
🎉 Congratulations! You guessed it right ✅
```

---

### ✅ Step 5: Play Again or Exit
- After each round, you will be asked:  
```plaintext
Do you want to continue playing? (Yes/No): 
```
- Type **Yes** to continue.  
- Type **No** to exit the game.

---

## 📊 **Expected Output**
Here’s what the game looks like during execution:

```
Welcome to the game of Guessing....
This game is only for 2 people: One should type the word and the other should guess.

:: Enter the Typer name : Shreyas
:: Enter the Guesser name : Mahesh

If you are the Typer, say 'yes' or else say 'no': yes
Enter the word (Hidden): ********

The shuffled word is: lpape
Mahesh, it's your turn to guess the word!
Enter your guess: apple
🎉 Congratulations! You guessed it right ✅

Do you want to continue playing? (Yes/No): yes
```

---

## 💯 **Possible Enhancements**
👉 If you want, I can add the following features:  
1. ✅ **Add a Scoreboard** (Show the score of Typer vs Guesser).  
2. ✅ **Add a Time Limit** (Guesser has only 30 seconds to guess).  
3. ✅ **Add Difficulty Levels** (Easy, Medium, Hard based on word length).  
4. ✅ **Save Game History** in a `CSV` file (who won and who lost).  
5. ✅ **Add Multiplayer Mode** (More than 2 players).  

👉 Would you like me to add these features? 🚀😎  
Just let me know. 👨‍💻

---

## 📜 **Author**
👨‍💻 Developed by: **Shreyas S Kulkarni**  
🚀 **GitHub Profile:** (https://github.com/Shreyu-07?tab=repositories)  
💡 **Email:** kulkarnishreyas1947@gmail.com  

---

## 💸 **License**
This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it for personal or commercial purposes.

---

## 🚀 **Contribute to This Project**
💡 Want to contribute to this project?  
Feel free to fork the repository, create a pull request, or suggest new features.  
All contributions are highly appreciated. 🚀🎮

---

## ⭐ **Don't Forget To Star This Repo!**
If you enjoyed the game or found it useful, **please star this repository**. 🌟  
It keeps me motivated to build more fun and creative projects like this! 🚀💻

---

## 💬 **Feedback**
If you face any issues, bugs, or want me to add new features, create an **issue** or contact me at:  
💡 **Email:** kulkarnishreyas1947@gmail.com  
---

✅ **This game was entirely built by Shreyas Kulkarni.** 🚀🎮  
👉 If you'd like me to add new features, just let me know. 😎

---

## ⭐ **Happy Coding! 💻🎮**
