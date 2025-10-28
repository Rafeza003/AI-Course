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

---

## 🎯 Game 1 – Chess

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

---

## 🎯 Game 2 – Connect Four

**Description:**  
A 7×6 grid-based game where two players drop discs into columns to connect four in a row.  
The AI anticipates the player’s moves and blocks them while trying to win.

**Algorithm Used:**
- Minimax Algorithm with Depth Limit  
- Alpha-Beta Pruning  
- Heuristic Evaluation (based on connected discs)

**How It Works:**
1. AI simulates all possible column drops.  
2. Scores each move using heuristic evaluation.  
3. Minimax with Alpha-Beta pruning selects the best outcome.  

**Features:**
- Adjustable search depth  
- Visual board made with Pygame  
- Player vs. AI gameplay  

---

## 🎯 Game 3 – Tic Tac Toe

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

