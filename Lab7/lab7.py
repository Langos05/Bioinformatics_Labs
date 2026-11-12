import re
import matplotlib.pyplot as plt

def parse_fasta(filepath):
    with open(filepath, "r") as f:
        return "".join(line.strip() for line in f if not line.startswith(">"))

def get_fragments(dna, seq, cut_offset):
    total_len = len(dna)
    cuts = [m.start() + cut_offset for m in re.finditer(seq, dna)]
    if not cuts:
        return [total_len]
    fragments = []
    prev = 0
    for c in cuts:
        fragments.append(c - prev)
        prev = c
    fragments.append(total_len - prev)
    fragments.sort(reverse=True)
    return fragments

seq1 = parse_fasta("genome1.fasta")
seq2 = parse_fasta("genome2.fasta")

enzymes = {
    "EcoRI": {"seq": "GAATTC", "cut": 1},
    "BamHI": {"seq": "GGATCC", "cut": 1},
    "HindIII": {"seq": "AAGCTT", "cut": 1}
}

lanes = []
lane_labels = []

for name, data in enzymes.items():
    frag1 = get_fragments(seq1, data["seq"], data["cut"])
    frag2 = get_fragments(seq2, data["seq"], data["cut"])
    
    lanes.append(frag1)
    lane_labels.append(f"G1 ({name})")
    
    lanes.append(frag2)
    lane_labels.append(f"G2 ({name})")

max_len = max(len(seq1), len(seq2))

plt.figure(figsize=(10, 6))

for i, fragments in enumerate(lanes):
    x = i + 1
    plt.plot([x, x], [0, max_len], color="gray", linestyle=":", linewidth=1)
    
    for frag in fragments:
        plt.plot([x - 0.25, x + 0.25], [frag, frag], color="blue", linewidth=3)
        plt.text(x, frag, f"{frag} bp", ha="center", va="bottom", fontsize=7)

plt.xlim(0.5, len(lanes) + 0.5)
plt.ylim(max_len + 200, 0)
plt.xticks(range(1, len(lanes) + 1), lane_labels, rotation=45)
plt.ylabel("Fragment size (bp)")
plt.title("Restriction Enzyme Digestion - Gel Electrophoresis")
plt.tight_layout()
plt.show()