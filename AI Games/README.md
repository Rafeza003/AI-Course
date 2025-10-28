 # 🎮 AI Game Collection (Python)

> 🤖 This project contains **three classic AI-based games** developed in Python — each powered by the **Minimax Algorithm** with **Alpha-Beta Pruning** and intelligent move selection.

---

## 🧠 Overview

This project demonstrates the use of **Artificial Intelligence search algorithms** in classic strategy games.  
Each game applies:
- **Minimax Algorithm**
- **Alpha-Beta Pruning**
- **Heuristic Evaluation**
- **Depth-Limited Search**

The purpose is to show how AI can simulate **human-like decision-making** in competitive environments.  
All games use a simple GUI built with **`tkinter`** or **`pygame`** for interactive gameplay.


## ## 🎯 Game 1– Rock, Paper, Scissors (RPS)

**Description:**  
A classic hand game where the player competes against the AI.  
The AI predicts the player’s next move using **random choice** or optional heuristic.

**Algorithm Used:**
- Random Choice AI  
- Optional pattern-based heuristic  

**Features:**
- GUI with Tkinter buttons  
- Real-time AI move display  
- Dynamic score tracking  

---

## 🎯 Game 2 – Tic Tac Toe

**Description:**  
A classic 3×3 game where the player competes against an unbeatable AI.  
The AI always chooses the best possible move.

**Algorithm Used:**
- **Minimax Algorithm**: Evaluates all game states recursively.  
- **Alpha-Beta Pruning**: Optimizes performance by skipping irrelevant moves.  

**How It Works:**
1. The game board is stored as a 3×3 matrix.  
2. AI checks for winning, losing, and draw positions.  
3. Uses Minimax to select the optimal move.  
4. Guarantees either win or draw (never loses).  

**Features:**
- Simple GUI with Tkinter  
- Real-time AI move prediction  
- Visual X and O display  

---
## 🎯 Game 3– Chess

**Description:**  
A simplified Chess AI that predicts the next move using search algorithms.  
It evaluates future board states to determine the most optimal move.

**Algorithm Used:**
- Minimax Algorithm  
- Alpha-Beta Pruning  
- Depth-Limited Search  
- Piece Value Evaluation Function  

**How It Works:**
1. AI generates all possible legal moves.  
2. Each move is scored based on piece values and positions.  
3. Minimax explores future board states recursively.  
4. Alpha-Beta Pruning skips unnecessary branches, making it faster.  

**Features:**
- Move highlighting  
- Turn-based play  
- Basic evaluation function for piece advantage  


