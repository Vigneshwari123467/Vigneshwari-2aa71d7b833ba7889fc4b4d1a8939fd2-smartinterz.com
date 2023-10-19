







def linearSearchproduct(productlist, targetproduct):
  indices = []

  for index, product in                  enumerate(productlist):
    if product == targetproduct:
      indices.append(index)


  return indices

#Example usage
product = ["shoes", "boot", "loafer",    "shoes ", "sandal","shoes "]
target = "shoes"
target2 ="apple"
result =                                 linearSearchproduct(product,target)
print(result)

