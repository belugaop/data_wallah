import random
import pandas as pd

def generate_random_dna_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

def generate_random_rna_sequence(length):
    return ''.join(random.choice('ACGU') for _ in range(length))

def calculate_gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100

def calculate_nucleotide_frequency(dna_sequence):
    nucleotide_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in dna_sequence:
        if nucleotide in nucleotide_count:
            nucleotide_count[nucleotide] += 1
    return nucleotide_count

def dna_to_rna(dna_sequence):
    return dna_sequence.replace('T', 'U')

def rna_to_dna(rna_sequence):
    return rna_sequence.replace('U', 'T')

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df['DNA Sequence'].tolist()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def read_rna_sequence(file_path):
    try:
        df = pd.read_csv(file_path)
        return df['RNA Sequence'].tolist()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def save_results_to_csv(result, file_path):
    df = pd.DataFrame([result], columns=['DNA Sequence', 'GC Content', 'RNA Sequence'])
    df.to_csv(file_path, index=False)
    print(f"Result saved to '{file_path}'.")

def print_separator():
    print("\n═════════════════════════════════════════════════════\n")

def get_user_sequence(sequence_type):
    sequence = input(f"Enter the {sequence_type} sequence: ").upper()
    if all(base in 'ACGTU' for base in sequence):
        return sequence
    else:
        print(f"Invalid {sequence_type} sequence. Please use only A, C, G, T, or U.")
        return None

def main():
    while True:
        print("██████╗░██╗░█████╗░░████████╗░█████╗░░█████╗░██╗░░░░░███████╗")
        print("██╔══██╗██║██╔══██╗░╚══██╔══╝██╔══██╗██╔══██╗██║░░░  ██╔════╝")
        print("██████╦╝██║██║░░██║░  ░██║░░░██║░░██║██║░░██║██║░░░░ ██████╗░")
        print("██╔══██╗██║██║░░██║░ ░░██║░░░██║░░██║██║░░██║██║░░░  ░╚═══██╗")
        print("██████╦╝██║╚█████╔╝░░ ░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝")
        print("╚═════╝░╚═╝░╚════╝░░░ ░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░")
        
        print("\n")
        
        print("𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝑷𝒓𝒐𝒋𝒆𝒄𝒕 ❗")
        


        print("╔════════════════════════════════════════╗")
        print("║ 1. Enter DNA Sequence Manually         ║")
        print("║ 2. Enter RNA Sequence Manually         ║")
        print("║ 3. Generate Random DNA Sequence        ║")
        print("║ 4. Generate Random RNA Sequence        ║")
        print("║ 5. Read DNA Sequence from CSV          ║")
        print("║ 6. Read RNA Sequence from CSV          ║")
        print("║ 7. Exit                                ║")
        print("╚════════════════════════════════════════╝")
        

        main_choice = input("𝗖𝗵𝗼𝗼𝘀𝗲 𝗮𝗻 𝗼𝗽𝘁𝗶𝗼𝗻 𝘁𝗼 𝗴𝗲𝘁 𝘀𝘁𝗮𝗿𝘁𝗲𝗱.  : ")
            
        if main_choice == '1':
            random_sequence = get_user_sequence("DNA")
            if random_sequence:
                print("\nDNA Sequence entered successfully.")

        elif main_choice == '2':
            random_sequence = get_user_sequence("RNA")
            if random_sequence:
                print("\n RNA Sequence entered successfully.")
            
        elif main_choice == '3':
            random_sequence = generate_random_dna_sequence(int(input("\nEnter the length of the DNA sequence: ")))
            print("\n Random DNA Sequence generated successfully.")
            
        elif main_choice == '4':
            random_sequence = generate_random_rna_sequence(int(input("Enter the length of the RNA sequence: ")))
            print("\n Random RNA Sequence generated successfully.")

        elif main_choice == '5':
            file_path = input("Enter the CSV file path: ")
            dna_sequences = read_csv(file_path)
            if dna_sequences:
                random_sequence = dna_sequences[0]
                print("\n DNA Sequence read from CSV successfully.")

        elif main_choice == '6':
            file_path = input("Enter the CSV file path: ")
            rna_sequences = read_rna_sequence(file_path)
            if rna_sequences:
                random_sequence = rna_sequences[0]
                print("\n RNA Sequence read from CSV successfully.")    

        elif main_choice == '5':
            random_sequence = get_user_sequence("DNA")
            if random_sequence:
                print("\n DNA Sequence entered successfully.")

        elif main_choice == '6':
            random_sequence = get_user_sequence("RNA")
            if random_sequence:
                print("\n RNA Sequence entered successfully.")
                

        elif main_choice == '7':
            print("Exiting the program. Goodbye!")
            print_separator()
            break

        else:
            print("\n Invalid choice. Please enter a number between 1 and 7.")
            print_separator()
            continue

        perform_operations(random_sequence)
        
def perform_operations(random_sequence):
    gc_content = 0
    rna_sequence = ""

    while True:
        print_separator()
        
        print("█▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀")
        print("█▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█")
        
        print("\n")
        
        print("╔════════════════════════════════════════╗")
        print("║1. Calculate GC Content                 ║")
        print("║2. Calculate Nucleotide Frequency       ║")
        print("║3. Convert DNA to RNA                   ║")
        print("║4. Convert RNA to DNA                   ║")
        print("║5. Go Back to Main Menu                 ║ ")
        print("╚════════════════════════════════════════╝")


        
        operation_choice = input("𝙀𝙣𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙘𝙝𝙤𝙞𝙘𝙚 ： ")

        if operation_choice == '1':
            gc_content = calculate_gc_content(random_sequence)
            print("\n GC Content calculated successfully:", gc_content)

        elif operation_choice == '2':
            nucleotide_frequency = calculate_nucleotide_frequency(random_sequence)
            print("\n Nucleotide Frequency calculated successfully:")
            for nucleotide, count in nucleotide_frequency.items():
                print(f"{nucleotide}: {count}")

        elif operation_choice == '3':
            rna_sequence = dna_to_rna(random_sequence)
            print("\n DNA to RNA conversion successful. RNA Sequence:", rna_sequence)

        elif operation_choice == '4':
            dna_sequence = rna_to_dna(random_sequence)
            print("\n RNA to DNA conversion successful. DNA Sequence:", dna_sequence)

        elif operation_choice == '5':
            print("\n Returning to the Main Menu.")
            print_separator()
            break

        else:
            print("\n Invalid choice. Please enter a number between 1 and 5.")
            print_separator()
            continue

        download_choice = input("\n Do you want to download results? (y/n): ")
        if download_choice.lower() == 'y':
            result = (random_sequence, gc_content, rna_sequence)
            save_results_to_csv(result, 'results.csv')
            print("\n Results downloaded successfully.")

        more_operations_choice = input("\n Do you want to continue for more operations? (y/n): ")
        if more_operations_choice.lower() != 'y':
            break        

if __name__ == "__main__":
    main()
