def all_thing_is_obj(object: any) -> int:
	dictType = {
		list : "List",
		tuple : "Tuple",
		set : "Set",
		dict : "Dict"
		}
	if type(object) in dictType:
		print(dictType[type(object)], ": ", type(object))
	elif type(object) == str:
		print(object, "is in the kitchen :", type(object))
	else:
		print("Type not found")
	return 42