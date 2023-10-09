# main.py
import tkinter as tk
from tkinter import filedialog
from gui import SequenceAnalyzer
from sequence_alignment import SequenceAligner
from database_access import SequenceDatabase
from blast_integration import BlastIntegration
from gc_calculator import GCCalculator

class BioinformaticsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bioinformatics App")
        self.root.geometry("800x600")

        # Initialize the Sequence Analyzer, Sequence Aligner, Sequence Database, Blast Integration, and GC Calculator
        self.sequence_analyzer = SequenceAnalyzer()
        self.sequence_aligner = SequenceAligner()
        self.sequence_db = SequenceDatabase("sequence_database.db")
        self.blast_integration = BlastIntegration()
        self.gc_calculator = GCCalculator()

        # Connect GUI actions to functions
        self.sequence_analyzer.align_button.config(command=self.perform_alignment)
        self.sequence_analyzer.load_button.config(command=self.load_sequence_file)
        self.sequence_analyzer.blast_button.config(command=self.run_blast)
        self.sequence_analyzer.gc_button.config(command=self.calculate_gc_content)

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

    def run_blast(self):
        sequence = self.sequence_analyzer.sequence_entry.get("1.0", "end-1c")
        blast_result = self.blast_integration.run_blast(sequence)
        self.sequence_analyzer.result_text.delete(1.0, tk.END)
        self.sequence_analyzer.result_text.insert(tk.END, blast_result)

    def calculate_gc_content(self):
        sequence = self.sequence_analyzer.sequence_entry.get("1.0", "end-1c")
        gc_content = self.gc_calculator.calculate_gc_content(sequence)
        self.sequence_analyzer.result_text.delete(1.0, tk.END)
        self.sequence_analyzer.result_text.insert(tk.END, f"GC Content: {gc_content:.2f}%")

if __name__ == "__main__":
    app = BioinformaticsApp()
    app.root.mainloop()
