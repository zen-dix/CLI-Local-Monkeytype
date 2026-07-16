# CLI-Local-Monkeytype ⌨️

A lightweight, flicker-free, and highly responsive Terminal User Interface (TUI) typing tutor built in Python. Designed for minimalists, terminal enthusiasts, and developers who want to practice touch typing directly in their shell environment.

## ✨ Current Features

- **Modern Terminal UI (TUI):** Uses a clean, fullscreen interactive application context leveraging the robust `blessed` engine.
- **Flicker-Free Rendering:** Optimized screen updates. The renderer targets specific character coordinates rather than using aggressive full-screen clears, resulting in an incredibly smooth interface.
- **Dynamic Interactive Colorizer:**
  - **Green** for correct characters.
  - **Red** for mistakes (with active `_` underlining for spaces).
  - **Reversed Text** cursor highlights the current character to type.
  - **Dimmed Text** for remaining words.
- **Engineered Context Management:** Safely restores system cursor visibility, screen buffer settings, and terminal configurations upon graceful exit or signal interruptions (`Ctrl+C` / `KeyboardInterrupt`).
- **Real-time Statistics Tracker:** Dynamically tracks and displays your typing speed in Words Per Minute (WPM) and accuracy percentage on the fly.
- **Local Dictionary Loader:** Supports loading localized dictionaries (standard `en_1000` or `ru_1000` word collections) with a bulletproof fallback mechanism to default vocabularies if files are missing.

## 🛠️ Architecture

The project adheres to strict **Separation of Concerns (SoC)**, separating the backend logic from the rendering pipeline:

- `main.py`: The entry point managing the non-blocking execution cycle (Event Loop), keyboard input parsing, and state updates.
- `engine.py`: Core business logic including the mathematical WPM tracker (`StatsTracker`) and localized dictionary compiler (`WordGenerator`).
- `ui.py`: Custom terminal renderer (`TUIRenderer`) and shell context manager (`TUIContext`) responsible for color layouts, safe exit routines, and adaptive cursor positioning.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A Unix-based terminal (Linux/macOS)

### Installation

```bash
# Clone the repository
git clone https://github.com/zen-dix/CLI-Local-Monkeytype

# Navigate into the project directory
cd CLI-Local-Monkeytype

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Linux/macOS:
source venv/bin/activate
# For Windows (PowerShell): \venv\Scripts\Activate.ps1
# For Windows (CMD): \venv\Scripts\activate.bat

# Install the required package inside the environment
pip install blessed

# Navigate to the source folder and run the script
cd src
python main.py
```
## 🗺️ Roadmap & Upcoming Plans

This project is actively developed. The following features are planned next:

- [ ] **Adaptive Backspace Logic:** Implement a precise character-history stack to correctly recalculate accuracy and statistical WPM history when correcting errors with backspace.
    
- [ ] **Code Practice Mode (Killer Feature):** A dedicated practice format for programmers. It will parse actual source code snippets and feature smart indentation auto-skipping, ignoring formatting spaces at the start of code blocks.
    
- [ ] **Window Resize Signal Handling (`SIGWINCH`):** Catch terminal resize signals dynamically to instantly re-center the interface without crashing or breaking layout alignment.
    
- [ ] **Custom Timers & Session Lengths:** Add customizable sessions (e.g., 15, 30, 60 seconds, or 25, 50, 100 words).
    
- [ ] **Type-Safety & Unit Tests:** Full type annotation coverage verified with `mypy`, and unit tests targeting the `StatsTracker` formulas.
