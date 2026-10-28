with open('sequence.fasta', 'r') as file:
    sequence = ''.join(line.strip() for line in file if not line.startswith('>'))

sequence = sequence.upper()
repetitions = []

for pattern_length in range(3, 7):
    for start in range(len(sequence)):
        pattern = sequence[start:start + pattern_length]
        repeated_sequence = pattern + pattern

        if len(pattern) == pattern_length and 6 <= len(repeated_sequence) <= 10:
            if sequence[start:start + len(repeated_sequence)] == repeated_sequence:
                repetitions.append((start + 1, pattern, repeated_sequence))

if repetitions:
    for position, pattern, repeated_sequence in repetitions:
        print(f'Position: {position}, pattern: {pattern}, repeated sequence: {repeated_sequence}')
else:
    print('No repetitions found.')
