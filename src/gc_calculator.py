# gc_calculator.py

class GCCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate_gc_content(sequence):
        sequence = sequence.upper()  # Convert the sequence to uppercase for case insensitivity
        gc_count = sequence.count("G") + sequence.count("C")
        total_bases = len(sequence)
        if total_bases > 0:
            gc_content = (gc_count / total_bases) * 100
        else:
            gc_content = 0
        return gc_content
