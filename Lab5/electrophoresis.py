import random
import matplotlib.pyplot as plt

with open('sequence.fasta', 'r') as file:
    sequence = ''.join(line.strip() for line in file if not line.startswith('>'))

samples = []
for _ in range(10):
    length = random.randint(100, min(3000, len(sequence)))
    start = random.randint(0, len(sequence) - length)
    samples.append(sequence[start:start + length])

plt.figure(figsize=(7, 6))

for i, sample in enumerate(samples):
    length = len(sample)
    migration = len(sequence) - length
    x = i + 1
    plt.plot([x, x], [0, migration], color='gray', linestyle=':', linewidth=1)
    plt.plot([x - 0.2, x + 0.2], [migration, migration], color='blue', linewidth=3)
    plt.text(x, migration, f'{length} bp', ha='center', va='bottom', fontsize=8)

plt.xlim(0.5, 10.5)
plt.ylim(len(sequence), 0)
plt.xticks(range(1, 11), [f'Sample {i}' for i in range(1, 11)], rotation=45)
plt.ylabel('Migration through the gel')
plt.title('DNA Gel Electrophoresis')
plt.tight_layout()
plt.show()
