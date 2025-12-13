# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pscala <pscala@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 17:12:27 by pscala            #+#    #+#              #
#    Updated: 2025/12/13 19:47:25 by pscala           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:

	if object is None:
		print(f"Nothing: {object} {type(object)}")
		return (0)

	elif object.__class__ is bool and object is False:
		print(f"Fake: {object} {type(object)}")
		return (0)

	elif object.__class__ is float and object != object:
		print(f"Cheese: {object} {type(object)}")
		return (0)

	elif object.__class__ is int and object == 0:
		print(f"Zero: {object} {type(object)}")
		return (0)

	elif object.__class__ is str and object == "":
		print(f"Empty:{object} {type(object)}")
		return (0)

	else:
		print("Type not Found")
	return (1)



if __name__ == "__main__":
	main()

