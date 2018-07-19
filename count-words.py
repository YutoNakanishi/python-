text = """
Here's a list of community resources in the Fountain Hills area.;
In the Fountain Hills downtown area;
we have a few centers that serve the general public.
"""

text = text.replace(";","")
text = text.replace(",","")
text = text.replace(".","")
words = text.split()

counter = {}
for w in words:
    ws = w.lower()
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

for k,v in sorted(counter.items()):
    if v >=2:
        print(k,v)
