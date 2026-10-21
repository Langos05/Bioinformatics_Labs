import random

def read_ncbi_fasta(filename):
    with open(filename, "r") as file:
        return file.read().replace("\n", "")

def get_reads(genome, num_reads):
    reads = []
    for _ in range(num_reads):
        length = random.randint(100, 120)
        start = random.randint(0, len(genome) - length)
        reads.append(genome[start:start+length])
    return reads

def assembly(reads):
    assembled = reads.pop(0)
    
    while reads:
        merged = False
        for i, read in enumerate(reads):
            for overlap in range(len(read), 0, -1):
                if assembled.endswith(read[:overlap]):
                    assembled += read[overlap:]
                    reads.pop(i)
                    merged = True
                    break
            if merged:
                break
        
        if not merged:
            assembled += reads.pop(0)
            
    return assembled

genome = read_ncbi_fasta("virus.fasta")
reads = get_reads(genome, 2000)
result = assembly(reads)

print(len(genome))
print(len(result))
print(genome == result)