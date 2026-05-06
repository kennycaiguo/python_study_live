from xml.dom.minidom import parse 

dom_tree = parse('country.xml')
doc = dom_tree.documentElement
# print(doc)
countries = doc.getElementsByTagName("country")
# print(countries)
for c in countries:
    name = c.getAttribute('name')
    print(f"Name:{name}")
    rank = c.getElementsByTagName("rank")[0]
    print(f"Rank:{rank.childNodes[0].data}")
    year = c.getElementsByTagName("year")[0]
    print(f"Yeat:{year.childNodes[0].data}")
    gdppc = c.getElementsByTagName("gdppc")[0]
    print(f"Rank:{gdppc.childNodes[0].data}")
    for neighbor in c.getElementsByTagName("neighbor"):  
          print(neighbor.tagName, ":", neighbor.getAttribute("name"), neighbor.getAttribute("direction")) 