import random

def reverse_complement(seq):
    pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    result = ""
    for base in reversed(seq):
        result += pairs[base]
    return result

def random_dna(length):
    bases = ["A", "T", "C", "G"]
    seq = ""
    for _ in range(length):
        seq += random.choice(bases)
    return seq

def create_transposon(ir_seq, body_length):
    right_ir = reverse_complement(ir_seq)
    body = random_dna(body_length)
    return ir_seq + body + right_ir

def insert_transposon(dna, pos, transposon, dr_length=5):
    target_site = dna[pos:pos + dr_length]
    inserted = target_site + transposon + target_site
    new_dna = dna[:pos] + inserted + dna[pos + dr_length:]
    return new_dna

def detect_transposons(dna, dr_length=5, ir_length=6, min_len=25, max_len=150):
    found = []
    n = len(dna)
    for start in range(n - min_len):
        left_dr = dna[start:start + dr_length]
        left_ir = dna[start + dr_length:start + dr_length + ir_length]
        expected_right_ir = reverse_complement(left_ir)
        for end in range(start + min_len, min(n, start + max_len)):
            right_dr = dna[end - dr_length:end]
            right_ir = dna[end - dr_length - ir_length:end - dr_length]
            if left_dr == right_dr and right_ir == expected_right_ir:
                found.append((start, end))
    return found

initial_length = random.randint(200, 450)
dna = random_dna(initial_length)

t1 = create_transposon("ATGCAT", 30)
dna = insert_transposon(dna, 20, t1)

t2 = create_transposon("GCTAGC", 40)
dna = insert_transposon(dna, 35, t2)

t3 = create_transposon("CGTACG", 25)
dna = insert_transposon(dna, 50, t3)

t4 = create_transposon("TACGTA", 20)
dna = insert_transposon(dna, len(dna) - 40, t4)

print("DNA length:", len(dna))
print("DNA sequence:", dna)

positions = detect_transposons(dna)
print("Detected transposons (start, end):")
for pos in positions:
    print(pos)