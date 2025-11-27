# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pscala <pscala@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/27 15:41:39 by pscala            #+#    #+#              #
#    Updated: 2025/11/27 16:25:06 by pscala           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import date
import time


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def main() -> None:
	ft_date = date.today()
	day = ft_date.day
	month = months[ft_date.month - 1]
	year = ft_date.year

	timestamp = time.time()
	formatted = f"{timestamp:,.4f}"

	print(f"Seconds since January 1, 1970: {formatted} or {timestamp:.2e} in scientific notation")
	print(f"{day} {month} {year}")


if __name__ == "__main__":
	main()
