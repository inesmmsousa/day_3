'''
Created on Feb 5, 2018

@author: mmp
'''
DNA_BASES = ['A', 'C', 'T', 'G', 'U']


def clean_fasta(sequence):
	"""
	clean fasta, remove all letters unless ACTG
	"""
	seq_return = ""
	for i in sequence:
		if i.upper() in DNA_BASES:
			seq_return += i.upper()
	return seq_return

if __name__ == "__main__":
	seq = 'accatatatagasfwefwgaggagattgq'
	seq_cleaned = clean_fasta(seq)
	print(seq_cleaned)
	
	### count dna bases
	for base in DNA_BASES:
		print('{} -> {}'.format(base, seq_cleaned.count(base)))

