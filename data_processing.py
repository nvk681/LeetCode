all_states = ["ab", "ak", "ar", "az", "ca", "co", "ct", "de", "dc", "fl",
              "ga", "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me", "md",
              "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj", "nm",
              "ny", "nc", "nd", "oh", "ok", "or", "pa", "pe", "pr", "ri", "sc", "sd",
              "tn", "tx", "ut", "vt", "va", "vi", "wa", "wv", "wi", "wy", "al",
              "bc", "mb", "nb", "lb", "nf", "nt", "ns", "nu", "on", "qc", "sk",
              "yt", "dengl", "fraspm", "gl"]

total_plants_template = {}
sub_sorted_data = []

with open("plants.data", "rb") as file:
    for line in file:
        sub_sorted_data.append(line.decode("latin-1").strip().split(","))
        total_plants_template[sub_sorted_data[len(sub_sorted_data)-1][0]] = 0



sorted_dict = {}
for state in all_states:
    sorted_dict[state] = total_plants_template.copy()

for data in sub_sorted_data:
    plant = data[0]
    index = 1
    while index < len(data):
      sorted_dict[data[index]][plant] = 1
      index = index + 1

print(sorted_dict['az']['tephrosia candida'])