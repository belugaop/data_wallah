# blast_integration.py
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

class BlastIntegration:
    def __init__(self):
        pass

    def run_blast(self, sequence):
        try:
            # Perform a BLAST search using NCBI's online service
            result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
            
            # Parse the BLAST results
            blast_record = NCBIXML.read(result_handle)
            
            # Process and analyze the BLAST results as needed
            # For simplicity, we'll just print the alignment descriptions here
            alignments = blast_record.alignments
            if alignments:
                for alignment in alignments:
                    print("Alignment Title:", alignment.title)
            
            result_handle.close()
        except Exception as e:
            print("Error running BLAST:", str(e))

if __name__ == "__main__":
    # Example usage of the BlastIntegration class
    sequence_to_search = "AGCTACGTA"  # Replace with your actual sequence
    blast = BlastIntegration()
    blast.run_blast(sequence_to_search)
