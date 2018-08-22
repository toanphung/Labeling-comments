data = []
with open('./reviews_lazada_data.csv', 'r') as f_in:
	data.append(f_in.readline())
	for line in f_in.readlines():
		if line.startswith("desktop") or line.startswith("android") or line.startswith("ios") or line.startswith("mobile"):
			data.append(line.strip())
			continue
		data[-1] += " " + line.strip()

with open('./comments_lazada_data.csv', 'w') as f_out:
	for d in data:
		f_out.write(d + "\n")
