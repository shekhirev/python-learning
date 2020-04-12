# вычислить количество различных объектов в списке
# objects задана ранее
s = {id(obj) for obj in objects}
print(len(s))
