# main.py
import tkinter as tk
from tkinter import filedialog
from gui import SequenceAnalyzer
from sequence_alignment import SequenceAligner
from database_access import SequenceDatabase
from blast_integration import BlastIntegration
from gc_calculator import GCCalculator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class belugaApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("beluga App")
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
        self.sequence_analyzer.export_pdf_button.config(command=self.export_as_pdf)

        # Run the GUI
        self.sequence_analyzer.run()

    # ... Other methods ...

    def export_as_pdf(self):
        try:
            sequence = self.sequence_analyzer.sequence_entry.get("1.0", "end-1c")
            analysis_result = self.get_analysis_result(sequence)

            # Ask the user for a PDF file path to save the analysis result
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if file_path:
                # Generate the PDF file
                self.create_pdf(file_path, analysis_result)

        except Exception as e:
            self.display_error_message(f"An error occurred while exporting as PDF: {str(e)}")

    def create_pdf(self, file_path, analysis_result):
        # Create a PDF file using ReportLab
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        # Set up the PDF content
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 100, "beluga Analysis Result")
        c.drawString(100, height - 120, "-----------------------------------------")

        # Write the analysis result to the PDF
        y_position = height - 150
        for line in analysis_result.split('\n'):
            c.drawString(100, y_position, line)
            y_position -= 20

        # Save and close the PDF file
        c.save()

    # ... Other methods ...

if __name__ == "__main__":
    app = belugaApp()
    app.root.mainloop()
