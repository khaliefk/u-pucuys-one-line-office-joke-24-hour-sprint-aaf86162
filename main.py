import os

LINE = "I sent my boss one quick question, and now we have a weekly meeting called Quick Question that has outlasted two interns."

def main():
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
