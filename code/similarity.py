def pmi(x, y):
	pass

def chain_similarity(chain, f, g):
	sum([pmi((e, d), (f, g)) for (e, d) in chain])