import os

LINE = "I've been awake since 2019 with no day off, and at the climax you asked for 4K. I didn't drop you, I fainted with dignity."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
