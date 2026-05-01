item=[
    ("pen 5"),
    ("book 6"),
    ("pencil 3")
]
def item_price(item):
 return item[1]
item.sort(key=item_price)
print(item)