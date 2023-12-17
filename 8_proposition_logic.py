def negation(p):
    return not p
def conjuction(p, q):
    return p and q
def disjunction(p, q):
    return p or q
def exclusive_disjuction(p, q):
    return (p and not q) or (not p and q)
def implication(p, q):
    return not p or q

logic = [True, False]
print('--- PREPOSITION LOGIC ---')

print('=== NEGATION ===')
print('p\t result')
for i in logic:
    print(i,'\t', negation(i))

print('== CONJUCTION ==')
print('p\t q\t result')
for i in logic:
    for j in logic:
        print(i,'\t',j,'\t', conjuction(i, j))

print('== DISJUCTNION ==')
print('p\t q\t result')
for i in logic:
    for j in logic:
        print(i,'\t',j,'\t', disjunction(i, j))

print('== exclusive_disjuction ==')
print('p\t q\t result')
for i in logic:
    for j in logic:
        print(i,'\t',j,'\t', exclusive_disjuction(i, j))

print('== implication ==')
print('p\t q\t result')
for i in logic:
    for j in logic:
        print(i,'\t',j,'\t', implication(i, j))