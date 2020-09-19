import pandas as pd
import part2, inspect

df = pd.read_csv("gene_table.txt", delimiter=",")

classes_names = list()
record_list = list()

tuple_class = inspect.getmembers(part2, inspect.isclass)

for m in tuple_class :
	if not inspect.isabstract(m[1]) and m[0] != 'ABC':
		classes_names.append(m[0])
		class_caller = m[1](df)
		record_caller = class_caller.record()
		record_list.append(record_caller)

class_dictionary = dict(zip(classes_names, record_list))