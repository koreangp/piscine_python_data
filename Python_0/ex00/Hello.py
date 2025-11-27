# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pscala <pscala@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/20 11:44:39 by pscala            #+#    #+#              #
#    Updated: 2025/11/27 15:36:26 by pscala           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[1] = "World"
ft_tuple = (ft_tuple[0], "France")
ft_set = {"Paris" if x == "tutu!" else x for x in (ft_set)}
ft_dict["Hello"] = "42 Paris"

print(ft_list)
print(ft_tuple)
print(sorted(ft_set))
print(ft_dict)
