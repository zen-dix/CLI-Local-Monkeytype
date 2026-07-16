from pathlib import Path
import random
import time

DEFAULT_WORDS = [
    "the",
    "be",
    "to",
    "of",
    "and",
    "a",
    "in",
    "that",
    "have",
    "I",
    "it",
    "for",
    "not",
    "on",
    "with",
    "he",
    "as",
    "you",
    "do",
    "at",
    "this",
    "but",
    "his",
    "by",
    "from",
    "they",
    "we",
    "say",
    "her",
    "she",
]


class WordGenerator:
    def load_dictionary(self, mode: str) -> list[str]:
        project_root = Path(__file__).resolve().parent.parent
        file_path = project_root / "dicts" / f"{mode}.txt"
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                words = file.read().split()
            return words
        except FileNotFoundError:
            print(
                f"Warning: Dictionary {file_path.name} not found. Using default fallback."
            )
            return DEFAULT_WORDS

    def generate_text_block(self, mode: str, count: int) -> str:
        words = self.load_dictionary(mode)
        return " ".join(random.choices(words, k=count))


class StatsTracker:
    def __init__(self) -> None:
        self.start_time = None
        self.end_time = None
        self.correct_chars = 0
        self.total_typed = 0

    def register_keystroke(self, target_char: str, input_char: str) -> None:
        if self.start_time is None:
            self.start_time = time.time()
        self.total_typed += 1
        if target_char == input_char:
            self.correct_chars += 1

    @property
    def accuracy(self) -> float:
        if self.total_typed == 0:
            return 100.0
        else:
            return round(self.correct_chars / self.total_typed * 100, 2)

    def stop(self):
        if self.start_time is None:
            self.start_time = time.time()
        self.end_time = time.time()

    @property
    def wpm(self) -> float:
        if self.start_time is None:
            return 0.0
        end = self.end_time if self.end_time is not None else time.time()
        elapsed_seconds = end - self.start_time
        if elapsed_seconds < 0.1:
            return 0.0
        minutes = elapsed_seconds / 60
        wpm = (self.correct_chars / 5) / minutes
        return round(wpm, 2)

    @property
    def elapsed_time(self) -> float:
        if self.start_time is None:
            return 0.0
        end = self.end_time if self.end_time is not None else time.time()
        return end - self.start_time


# tests
if __name__ == "__main__":
    wordgen = WordGenerator()
    print("Target:", wordgen.generate_text_block("ru_1000", 10))

    tracker = StatsTracker()
    tracker.correct_chars = 100
    tracker.total_typed = 110
    tracker.start_time = time.time() - 30
    tracker.stop()
    symb = input()
    tracker.register_keystroke("b", symb)

    print(f"Accuracy: {tracker.accuracy}%")
    print(f"WPM: {tracker.wpm}")
