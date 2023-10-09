from Bio import pairwise2

class SequenceAligner:
    def __init__(self):
        pass

    def align_sequences(self, sequence1, sequence2):
        alignments = pairwise2.align.globalxx(sequence1, sequence2, one_alignment_only=True)
        
        if not alignments:
            return "No alignments found."
        
        best_alignment = alignments[0]
        aligned_sequence1 = best_alignment.seqA
        aligned_sequence2 = best_alignment.seqB
        
        alignment_result = f"Alignment results:\n\nSequence 1:\n{aligned_sequence1}\n\nSequence 2:\n{aligned_sequence2}"
        return alignment_result
