# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pscala <pscala@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/05 15:43:55 by pscala            #+#    #+#              #
#    Updated: 2025/12/13 21:24:33 by pscala           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:

	if object.__class__ is str:
		print(object, "is in the kitchen :", type(object))
	elif object.__class__ is int:
		print("Type not found")
	else:
		print(type(object).__name__.capitalize(), ":", type(object))
	return 42



# def main() -> None:
# 	ft_tuple = ("JoJo", 42, 3.14)
# 	ft_list = ["lion", "24", 6.14]
# 	ft_set = {"JoJolion", "oui"}
# 	ft_dict = {"JoJo" : "lion"}

# 	test = (ft_tuple, ft_list, ft_set, ft_dict, 42, "JoJolion")
# 	for item in test:
# 		print(f"{all_thing_is_obj(item)}")
