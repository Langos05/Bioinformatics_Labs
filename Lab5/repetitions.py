with open('sequence.fasta', 'r') as file:
    sequence = ''.join(line.strip() for line in file if not line.startswith('>'))

sequence = sequence.upper()
repetitions = []

for pattern_length in range(3, 7):
    for start in range(len(sequence)):
        pattern = sequence[start:start + pattern_length]
        if len(pattern) < pattern_length:
            continue

        if start > 0 and sequence[start - 1] == pattern[-1]:
            continue

        repeat_count = 0
        while sequence[start + repeat_count * pattern_length:start + (repeat_count + 1) * pattern_length] == pattern:
            repeat_count += 1

        if 6 <= repeat_count <= 10:
            repeated_sequence = pattern * repeat_count
            repetitions.append((start + 1, pattern, repeat_count, repeated_sequence))

if repetitions:
    for position, pattern, repeat_count, repeated_sequence in repetitions:
        print(f'Position: {position}, pattern: {pattern}, copies: {repeat_count}, sequence: {repeated_sequence}')
else:
    print('No repetitions found.')
