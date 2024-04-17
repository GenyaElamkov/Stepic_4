from collections.abc import Sequence


class DNA(Sequence):
    def __init__(self, chain: str) -> None:
        self.chain = chain
        self._dic = {"A": ("A", "T"), "T": ("T", "A"), "G": ("G", "C"), "C": ("C", "G")}

    def __getitem__(self, index):
        return self._dic[self.chain[index]]

    def __str__(self) -> str:
        return self.chain

    def __len__(self):
        return len(self.chain)

    def __contains__(self, value: object) -> bool:
        return value in self.chain

    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self.chain + other.chain)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, __class__):
            return self.chain == other.chain
        return NotImplemented

    # def __reversed__(self):
    #     return super().__reversed__()


# INPUT DATA:

# # TEST_1:
# dna = DNA('AGTC')

# print(dna[0])
# print(dna[1])
# print(dna[2])
# print(dna[3])
# print(dna[-1])
# print(dna[-2])

# # TEST_2:
# dna = DNA('AGT')

# print(dna)
# print(len(dna))
# print('A' in dna)
# print('C' in dna)

# # TEST_3:
# dna1 = DNA('ACG')
# dna2 = DNA('TTTAAT')
# dna3 = dna1 + dna2
# dna4 = dna2 + dna1

# print(dna3, type(dna3))
# print(dna4, type(dna4))

# # TEST_4:
# dna1 = DNA('ACG')
# dna2 = DNA('TTTAAT')
# dna3 = DNA('TTTAAT')

# print(dna1 == dna2)
# print(dna2 == dna3)
# print(dna1 != dna3)
# print(dna2 != dna3)

# # TEST_5:
# dna = DNA('TGAACCTGACCTCGATTTCAAGGG')

# print(*dna)
# print(*reversed(dna))
# print('A' in dna)
# print('C' not in dna)

# # TEST_6:
# dna = DNA('ACG')
# not_supported = [1, 2.23, [1, 2, 3], {1: 'one'}, {4, 5, 6}, True, False, 'CTA', (7, 8, 9)]

# for item in not_supported:
#     print(item == dna)

# # TEST_7:
# dnas = ['TAAAACCCCATCGGCTCTGACAATGAAC', 'AGATGTTCCCTCTAATATCTATACGAAT', 'ACGACGCACTGCATACAATACAATAGTG',
#         'TCCCAGTCAGGATCGGATTGGTATAATC', 'TACACGCATAGTGCCCAACTCCTACCCG', 'TCACCGCTGAAAACATGTTCTGGAGGGC',
#         'CCCAGGATAGACCTATTTGCCGTATCCA', 'ATCGATCGTGCGGGAAATCCTGCCATAT', 'AGACCAACTTATTGGGCACACGCTCCGG',
#         'CGCGTCCCCCATATCAACGCGTGAATGC', 'AGTCACGATCAGCTGGACGTAGTGGCAA', 'GTGTAGGGTCAAGGGACACCTGATATCT',
#         'AAAAGACGAAAATTGCTAAGTGGCAGTC', 'TGGAGGCCGAGCTCGCGTTGGAAATAGT', 'AAGTCTGCCGAGGCGGGTCGGGAGCGCC',
#         'ATTATCCAATCCAGTCACGTATTGAATA', 'ATTGTGAACCTTATACGTTAGTAATACC', 'AGACAATCATGCTATTAGGTATGACGTT',
#         'ATCACTGAGGCAGAGACTAGCCGCGCTT', 'TATGGGTGGTATCCTAAGCATTCAATGG']

# for base in dnas:
#     dna = DNA(base)
#     print(*dna)

# TEST_8:
dna = DNA("ACG")
print(dna.__eq__(1))
print(dna.__ne__(1.1))
print(dna.__add__([1, 2, 3]))
