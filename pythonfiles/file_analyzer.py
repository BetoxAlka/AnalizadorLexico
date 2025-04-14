import os

class FileAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.lines = 0
        self.words = 0
        self.characters = 0

    def analyze(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    self.lines += 1
                    self.words += len(line.split())
                    self.characters += len(line)
        except FileNotFoundError:
            print(f"File {self.filepath} not found.")

    def get_report(self):
        return {
            'lines': self.lines,
            'words': self.words,
            'characters': self.characters
        }

    def display_report(self):
        report = self.get_report()
        print(f"File: {self.filepath}")
        print(f"Lines: {report['lines']}")
        print(f"Words: {report['words']}")
        print(f"Characters: {report['characters']}")

def scan_directory(path):
    stats = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path) and file.endswith('.txt'):
            analyzer = FileAnalyzer(full_path)
            analyzer.analyze()
            analyzer.display_report()
            stats.append(analyzer.get_report())
    return stats

def main():
    directory = input("Enter directory path: ")
    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    print(f"\nAnalyzing text files in directory: {directory}\n")
    all_stats = scan_directory(directory)
    print("\nSummary of all files:")
    for stat in all_stats:
        print(stat)

if __name__ == "__main__":
    main()
