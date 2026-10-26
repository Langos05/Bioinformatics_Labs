import collections
import os
from google import genai

codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGA':'_'
}

def read_fasta(filename):
    sequence = ""
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith(">"):
                clean_text = line.strip().upper()
                sequence = sequence + clean_text
    return sequence

def main():
    try:
        genome_sequence = read_fasta("genome.fasta")
    except FileNotFoundError:
        print("Error: File 'genome.fasta' not found.")
        return

    valid_codons = []
    
    for i in range(0, len(genome_sequence), 3):
        codon = genome_sequence[i:i+3]
        if len(codon) == 3 and 'N' not in codon:
            valid_codons.append(codon)
    
    codon_counts = collections.Counter(valid_codons)
    top_10_codons = codon_counts.most_common(10)
    
    top_10_amino_acids = []
    
    for item in top_10_codons:
        codon = item[0]
        amino_acid = codon_table.get(codon)
        
        if amino_acid != '_' and amino_acid not in top_10_amino_acids:
            top_10_amino_acids.append(amino_acid)
    
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not found.")
        print("Please run: $env:GEMINI_API_KEY=\"YOUR_API_KEY\" in PowerShell first.")
        return

    client = genai.Client()
    
    prompt = f"The top 10 most frequent codons in my viral genome are {top_10_codons}. These correspond to the following amino acids: {top_10_amino_acids}. What foods must a patient eat in order to avoid these specific amino acids and slow down the infection?"
    
    print("Querying AI...\n")

    
    try:
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=prompt
        )
        print("--- RECOMMENDED DIET ---")
        print(response.text)
    except Exception as e:
        print(f"Error contacting AI: {e}")
    

if __name__ == "__main__":
    main()