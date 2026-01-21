# Pendu (Hangman) — Python / Pygame

Small Hangman project with a **Pygame UI** (menu + options) and a **word list manager**.

## Requirements

- Python 3.x
- `pygame`

Install Pygame:

```bash
python -m pip install pygame
```

## Run

From the project root (the folder that contains `main.py`):

```bash
python main.py
```

## Controls

- **Mouse**: click buttons (Menu / Options / Word management)
- **Esc**: go back / quit (depending on the screen)

In **Options → Mots → Ajouter mot**:

- Type letters on your keyboard
- **Backspace**: delete last character
- **Enter**: validate

In **Options → Mots → Retirer mot**:

- Click a word to remove it
- Use `<` / `>` arrows to change pages (if there are many words)

## Word list

The word list is stored in `assets/words.txt`.

- Lines after `--default--` are default words
- Lines after `--user` are user-added words

The app also provides:
- **Ajouter mot**: append a word
- **Retirer mot**: remove by clicking
- **Restaurer liste**: restore defaults

## Project structure

- `main.py`: app entrypoint (Pygame window)
- `src/menu.py`: main menu (Play / Options)
- `src/options.py`: options screens + word list management UI
- `src/words_mgt.py`: read/add/remove/reset words in `assets/words.txt`
- `assets/`: fonts, images, and `words.txt`

## Status / notes

- The **UI is working** (menu + options + word management).
- The **Play** button is currently a placeholder (`tbd game` in `src/menu.py`).

