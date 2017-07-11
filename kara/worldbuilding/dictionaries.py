#python dictionaries


str = 'cat'

"cat1"   #3
"cat2"   #5
"cat3"   #47.5

#cat_list["cat1","cat2","cat3"]
# cat_size_list = [3,5,47.5]


#use a dictionary  {key,value}, mutable
#if you are going to sort, use the same types
# dict.items() - > list of tuples corresponding to diction ary entries

cat_sizes = {
    "cat1":3,
    "cat2":5,
    "cat3": 47.5,
}
cat1_size = cat_sizes["cat1"]
print (cat_sizes["cat1"])




#write function numbers_squared_dict(n)   returns a dictionary
#with keys k in [1->n], and corresponding values k^2
#numbers _squard_dict(3)
#{1:1, 2:4, 3:9)}
"""

squared_d = dict()
for n in range(1,(n+1))
    squared_d[n] = n *n
    return squared_d
"""

def sort_by_key(dict):
    return sorted(dict.items())

def reverse_sort_by_key(dict):
    return sorted(dict.items(),reverse = True)
def srt_by_value(dict):
    return sorted(dict.items(),key = operator.itemgetter(1))
#for tuple (x,y) operator.itemgetter would give you y's value


d = {
    1:"hi",
    3: "roses",
    2: "bye",
    4: "bye2"
}

print (sort_by_key(d))

#how to lopop over entries in the dictionary
d= {
    1:"hi",
    2: "low",
    3: "sheep"
}
for (key,values) in d.items():
    print (key,values)"C:\Program Files\Python36\python.exe" C:/Users/FLL234-13/PycharmProjects/ccircle/kara/worldbuilding/dictionaries.py
3
[(1, 'hi'), (2, 'bye'), (3, 'roses'), (4, 'bye2')]
1 hi
2 low
3 sheep

Process finished with exit code 0





