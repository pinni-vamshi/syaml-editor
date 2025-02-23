import tkinter as tk
import sys

def create_table(rows, cols):
    root = tk.Tk()
    root.title("SYAML Table Preview")

    for i in range(rows):
        for j in range(cols):
            entry = tk.Entry(root, width=10, font=("Arial", 12))
            entry.grid(row=i, column=j, padx=5, pady=5)

    root.mainloop()

def main():
    if len(sys.argv) != 3:
        print("Usage: syaml-preview <rows> <cols>")
        sys.exit(1)
    try:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
    except ValueError:
        print("Rows and columns must be integers.")
        sys.exit(1)
    create_table(rows, cols)

if __name__ == '__main__':
    main()
