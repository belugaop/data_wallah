# main.py
import tkinter as tk
from tkinter import filedialog
from gui import SequenceAnalyzer
from sequence_alignment import SequenceAligner
from database_access import SequenceDatabase

class BioinformaticsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bioinformatics App")
        self.root.geometry("800x600")

        # Initialize the Sequence Analyzer, Sequence Aligner, and Sequence Database
        self.sequence_analyzer = SequenceAnalyzer()
        self.sequence_aligner = SequenceAligner()
        self.sequence_db = SequenceDatabase("sequence_database.db")

        # Connect GUI actions to functions
        self.sequence_analyzer.align_button.config(command=self.perform_alignment)
        self.sequence_analyzer.load_button.config(command=self.load_sequence_file)

        # Run the GUI
        self.sequence_analyzer.run()

    def perform_alignment(self):
        sequence = self.sequence_analyzer.sequence_entry.get("1.0", "end-1c")
        alignment_result = self.sequence_aligner.align_sequences(sequence, "Reference Sequence")
        self.sequence_analyzer.result_text.delete(1.0, tk.END)
        self.sequence_analyzer.result_text.insert(tk.END, alignment_result)

    def load_sequence_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Sequence Files", "*.fasta *.txt")])
        if file_path:
            with open(file_path, "r") as file:
                sequence = file.read()
                self.sequence_analyzer.sequence_entry.delete("1.0", tk.END)
                self.sequence_analyzer.sequence_entry.insert(tk.END, sequence)

if __name__ == "__main__":
    app = BioinformaticsApp()
    app.root.mainloop()
