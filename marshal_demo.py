import marshal
import os

data = {'jack': 4098, 'sape': 4139}

converted_bytes = marshal.dumps(data)
print("\n-=- converted_bytes -=-\n")
print(converted_bytes)

loaded_data = marshal.loads(converted_bytes)
print("\n-=- loaded_data -=-\n")
print(loaded_data)

ouf = open('datafile.dat', 'wb')
marshal.dump(data, ouf)
ouf.close()

inf = open('datafile.dat', 'rb')
loaded_dict = marshal.load(inf)
inf.close()

print("\n-=- loaded_dict -=-\n")
print(loaded_dict)

os.remove('datafile.dat')
