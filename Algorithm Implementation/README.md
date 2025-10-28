# 🧠 Algorithm Implementation Collection

This repository contains **implementations of fundamental algorithms** in Artificial Intelligence and Computer Science.  
Each algorithm is clearly implemented with **well-documented code and examples** to help you understand how they work in practice.

---

## 📚 Table of Contents
1. [Breadth-First Search (BFS)](#-breadth-first-search-bfs)
2. [Depth-First Search (DFS)](#-depth-first-search-dfs)
3. [Depth-Limited Search (DLS)](#-depth-limited-search-dls)
4. [Iterative Deepening Search (IDS)](#-iterative-deepening-search-ids)
5. [Best-First Search](#-best-first-search)
6. [Beam Search](#-beam-search)
7. [Bidirectional Search](#-bidirectional-search)
8. [Hill Climbing](#-hill-climbing)
9. [Minimax Algorithm](#-minimax-algorithm)
10. [Alpha-Beta Pruning](#-alpha-beta-pruning)
11. [A* (A-Star) Search](#-a-astar-search)

---

## 🔍 Breadth-First Search (BFS)
**How it Works:**  
BFS explores all neighboring nodes at the current depth before moving deeper. It uses a **queue** data structure.

**Steps:**
- Start from the source node  
- Visit all immediate neighbors  
- Move to the next level  
- Mark visited nodes  

**Applications:**
- Shortest path in unweighted graphs  
- Web crawlers  
- Network broadcasting  
- Social networks (friend-of-friend search)

**Complexity:**  
- Time: **O(V + E)**  
- Space: **O(V)**  

**Example Output:**  
`A B C D E F G H I`

---

## 🌲 Depth-First Search (DFS)
**How it Works:**  
DFS explores as deep as possible along one path before backtracking. It uses a **stack or recursion**.

**Applications:**
- Path finding  
- Topological sorting  
- Cycle detection  
- Maze solving  

**Complexity:**  
- Time: **O(V + E)**  
- Space: **O(V)**  

**Example Output:**  
`A G H I B E F D C`

---

## ⚙️ Depth-Limited Search (DLS)
**How it Works:**  
A variant of DFS that stops when a **depth limit** is reached.

**Applications:**
- Fixed-depth game trees  
- Resource-limited searches  
- Infinite-path avoidance  

**Complexity:**  
- Time: **O(b^d)**  
- Space: **O(d)**  

**Example Output:**  
`Target not found within depth`

---

## 🔁 Iterative Deepening Search (IDS)
**How it Works:**  
Combines BFS’s completeness with DLS’s low memory. Repeats DLS with increasing depth limits.

**Applications:**
- Game trees  
- Pathfinding with unknown depth  

**Complexity:**  
- Time: **O(b^d)**  
- Space: **O(d)**  

**Example Output:**  
`Target found at depth 4`

---

## 💡 Best-First Search
**How it Works:**  
Selects the path that appears best using a **heuristic function (h(n))**.  
Uses a **priority queue** for node selection.

**Applications:**
- GPS navigation  
- Robot pathfinding  
- AI games  

**Complexity:**  
- Time: **O(b^m)**  
- Space: **O(b^m)**  

**Example Output:**  
`0 1 3 8 9`

---

## 🎯 Beam Search
**How it Works:**  
Similar to Best-First Search but limits the number of nodes considered at each level (beam width).

**Applications:**
- Machine translation  
- Speech recognition  
- Image captioning  

**Complexity:**  
- Time: **O(b × k)**  
- Space: **O(b)**  

**Example Output:**  
`Goal found at node 7`

---

## 🔄 Bidirectional Search
**How it Works:**  
Runs two searches — forward from start and backward from goal — meeting in the middle.

**Applications:**
- Shortest path  
- Route planning  
- Social graph search  

**Complexity:**  
- Time: **O(b^(d/2))**  
- Space: **O(b^(d/2))**  

**Example Output:**  
`Target found at depth 3`

---

## 🧩 Bidirectional Path Search
**How it Works:**  
Extends bidirectional search by reconstructing the full path once the two searches meet.

**Applications:**
- GPS systems  
- Robot motion planning  
- Game pathfinding  

**Complexity:**  
- Time: **O(b^(d/2))**  
- Space: **O(b^(d/2))**

**Example Output:**  
`Path found: A → B → C → D`

---

## 🌟 A* (A-Star) Search
**How it Works:**  
A* Search is a **best-first search algorithm** that finds the shortest path from a start node to a goal node using a **heuristic function**. It combines **path cost (g(n))** and **heuristic estimate (h(n))** to determine the next node to explore:

\[
f(n) = g(n) + h(n)
\]

**Steps:**
- Initialize the open list with the start node  
- Calculate `f(n)` for all neighbors  
- Select the node with the lowest `f(n)`  
- Repeat until the goal is reached or no nodes remain  
- Reconstruct the path from start to goal  

**Applications:**
- GPS navigation systems  
- Robot path planning  
- Video games (pathfinding)  
- Network routing  

**Complexity:**  
- Time: **O(b^d)** (worst case, depends on heuristic)  
- Space: **O(b^d)**  

**Example Output:**  
`Path found: A → B → D → G`  



