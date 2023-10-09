import tkinter as tk
from tkinter import filedialog

class SequenceAnalyzer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sequence Analysis Tool")
        self.root.geometry("800x600")

        self.create_gui_elements()

    def create_gui_elements(self):
        self.create_help_button()
        self.create_hello_label()
        self.create_sequence_input()
        self.create_alignment_button()
        self.create_load_button()
        self.create_result_display()

    def create_help_button(self):
        help_button = tk.Button(self.root, text="Help", command=self.show_help)
        help_button.pack(pady=10)

    def create_hello_label(self):
        user_name = "John"  # Replace with the actual user's name
        hello_label = tk.Label(self.root, text=f"Hello {user_name}", font=("Helvetica", 14))
        hello_label.pack()

    def create_sequence_input(self):
        sequence_label = tk.Label(self.root, text="Enter Sequence:")
        sequence_label.pack()
        self.sequence_entry = tk.Text(self.root, height=5, width=50)
        self.sequence_entry.pack()

    def create_alignment_button(self):
        align_button = tk.Button(self.root, text="Perform Alignment", command=self.perform_alignment)
        align_button.pack(pady=10)

    def create_load_button(self):
        load_button = tk.Button(self.root, text="Load Sequence from File", command=self.load_sequence_file)
        load_button.pack(pady=10)

    def create_result_display(self):
        result_label = tk.Label(self.root, text="Alignment Results:")
        result_label.pack()
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack()

    def show_help(self):
        # Placeholder: Display a help message or user guide
        pass

    def perform_alignment(self):
        # Placeholder: Implement sequence alignment logic
        self.result_text.delete(1.0, tk.END)  # Clear previous results
        sequence = self.sequence_entry.get("1.0", "end-1c")  # Get the entered sequence
        self.result_text.insert(tk.END, f"Alignment results for sequence:\n{sequence}\n\n")
        self.result_text.insert(tk.END, "Alignment results will be displayed here.")

    def load_sequence_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Sequence Files", "*.fasta *.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.sequence_entry.delete("1.0", tk.END)  # Clear previous sequences
                self.sequence_entry.insert(tk.END, file.read())

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    analyzer = SequenceAnalyzer()
    analyzer.run()
