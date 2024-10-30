seq1 = "abc123xyz"
seq2 = "789xyzabc"

set1 = set(seq1)
set2 = set(seq2)

common_el = list(set1 & set2)
every_el = list(set1 | set2)

print(f"Wspólne elementy dla dwóch sekwenccji to: {common_el}")
print(f"Elementy z obu sekwenccji to: {every_el}")