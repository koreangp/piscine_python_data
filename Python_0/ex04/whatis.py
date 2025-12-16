# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pscala <pscala@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 19:51:04 by pscala            #+#    #+#              #
#    Updated: 2025/12/16 18:43:35 by pscala           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from colors import RESET, BOLD, RED, BLUE, YELLOW

if len(sys.argv) > 2:
    print(f"{BOLD}{RED}AssertionError: more than one argument is provided{RESET}")
    sys.exit(1)

if len(sys.argv) < 2:
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print(f"{BOLD}{RED}AssertionError: argument is not an integer{RESET}")
    sys.exit(1)

if number % 2 == 0:
    print(f"{BOLD}{BLUE}I'm Even.{RESET}")
else:
    print(f"{BOLD}{YELLOW}I'm Odd.{RESET}")
