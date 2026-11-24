import os

LINE = "I asked my boss one quick question, so now there's a weekly meeting called Quick Question where the only answer ever given is 'let's circle back next week.'"

def main():
    text = " ".join(LINE.split())
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
