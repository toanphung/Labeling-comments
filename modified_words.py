import pickle

l_ = []
with open("./stop_words_vietnamese.txt", "r") as f:
	for line in f.readlines():
		l_.append(line.strip())

pickle_out = open("./stop_words_vietnamese.pickle", "wb")
pickle.dump(l_, pickle_out)
pickle_out.close()

d_ = dict()
with open("./abbreviation_words_vietnamese.txt", "r") as f:
	for line in f.readlines():
		t_l = line.strip().split()
		print(t_l)
		d_[t_l[0]] = t_l[1]

pickle_out = open("./abbreviation_words_vietnamese.pickle", "wb")
pickle.dump(d_, pickle_out)
pickle_out.close()
