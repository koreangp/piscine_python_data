# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pscala <pscala@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/20 11:44:39 by pscala            #+#    #+#              #
#    Updated: 2025/11/27 14:47:17 by pscala           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[1] = "World"
ft_tuple = (ft_tuple[0], "France")
# ft_set[1] = "Paris"

print(type(ft_list))
print(type(ft_tuple))
print(type(ft_set))
print(type(ft_dict))

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
