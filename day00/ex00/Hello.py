ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list
ft_list[1] = "World!"

# tuple
# ft_tuple[1] = "FRANCE" 
# ft_tuple = ("Hello", "France!")
tmp = list(ft_tuple)
tmp[1] = "France!"
ft_tuple = tuple(tmp)


# set
ft_set.remove("tutu!")
ft_set.add("Lyon!")


# dic
ft_dict["Hello"] = "42Lyon!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)