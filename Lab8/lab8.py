import matplotlib.pyplot as plt

def get_cg(seq):
    cg = seq.count("C") + seq.count("G")
    return (cg / len(seq)) * 100

def get_ic(seq):
    n = len(seq)
    total = 0
    for u in range(1, n):
        matches = 0
        for i in range(n - u):
            if seq[i] == seq[i + u]:
                matches += 1
        total += (matches / (n - u)) * 100
    return total / (n - 1)

def make_pattern(seq, window_size):
    cg_values = []
    ic_values = []
    for i in range(len(seq) - window_size + 1):
        window = seq[i:i + window_size]
        cg_values.append(get_cg(window))
        ic_values.append(get_ic(window))
    center_cg = sum(cg_values) / len(cg_values)
    center_ic = sum(ic_values) / len(ic_values)
    return cg_values, ic_values, center_cg, center_ic

def read_fasta(filename):
    sequences = []
    current = ""
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current != "":
                    sequences.append(current.upper())
                    current = ""
            else:
                current += line
        if current != "":
            sequences.append(current.upper())
    return sequences

s = "CGGACTGATCTATCT" + "A" * 27 + "CGTAGCATCTATCGATCTATCGATCTATCCTAGCGATCTA"
window_size = 30

print("CG%:", round(get_cg(s), 2))
print("IC:", round(get_ic(s), 2))

promoters = read_fasta("gene_promoters_complete.fa")
s1 = promoters[0]

s1_cg, s1_ic, s1_center_cg, s1_center_ic = make_pattern(s1, window_size)

plt.figure(1)
plt.scatter(s1_cg, s1_ic, s=10, color="blue")
plt.xlabel("C+G %")
plt.ylabel("Information Content (IC)")
plt.title("Promoter S1 Pattern")

centers_cg = []
centers_ic = []
for seq in promoters[:100]:
    if len(seq) >= window_size:
        _, _, c_cg, c_ic = make_pattern(seq, window_size)
        centers_cg.append(c_cg)
        centers_ic.append(c_ic)

plt.figure(2)
plt.scatter(centers_cg, centers_ic, s=15, color="red")
plt.xlabel("Center C+G %")
plt.ylabel("Center IC")
plt.title("Centers of Weight")

plt.show()