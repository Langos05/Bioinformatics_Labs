import math

def calcula_tm(sequence):
    sequence = sequence.upper();

    a = sequence.count("A")
    t = sequence.count("T")
    c = sequence.count("C")
    g = sequence.count("G")

    tm = 4 * (g+c) + 2 * (a+t)

    return tm

def calcula_tm_2(sequence, na_conc):
    
    sequence = sequence.upper();
    length = len(sequence)

    c = sequence.count("C")
    g = sequence.count("G")

    fraccion_gc = (g+c)/length
    tm = 81.5 + (16.6 * math.log10(na_conc)) + (41 * fraccion_gc) - (600 / length) #Na_conc = 0.05 M
    return tm

sequence = str(input("Introduce the sequence: "))
na_conc = str(input("Introduce the Na+ concentration (M) (default 0.05 M): "))
if na_conc == '':
    na_conc = 0.05
else:
    na_conc = float(na_conc)

result1= calcula_tm(sequence)
result2= calcula_tm_2(sequence, na_conc)
print("Sequence: ", sequence.upper())
print("Melting temperature of the sequence: ", result1, "°C")
print("Melting temperature of the sequence (method 2): ", result2, "°C")