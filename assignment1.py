"""
Replace the contents of this module docstring with your own details
Name: Davin Natanael
Date started: 08 December 2021
GitHub URL:https://github.com/davinnataz/assignment-1---movies-to-watch-davinnataz-master.git
"""

import csv
import operator

def main():
    # this is a main menu for movie to watch
    """..."""
    print("Movies To Watch 1.0 - by Davin Natanael")
    print(f"{total_data} movies loaded")
    while True:
        print_menu():
        menu = imput(">>>").upper
        if menu == 'L':
            total_data, movie_list = movies_list(total_data, movie_list)
        elif menu == 'A':
            total_data, movie_list = adding_movie(total_data, movie_list)
        elif menu == 'W':
            total_data, movie_list = watching_movie(total_data, movie_list)
        elif menu == 'Q':
            quit_menu(total_data, movie_list)
            break
        else:
            print("Menu is not found")

def read_file():
    #this function is to transfer data from movies.csv
    csv_file = open('movies.csv')
    csv_read = csv.reader(csv_file, delimiter =',')
    total_data = 0
    movie_list =[]
    for row in csv_read:
        movie = []
        movie.append(row[0])
        movie.append(int(row[1]))
        movie.append(row[2])
        movie.append(row[3])
        total_data += 1
        movie_list.append(movie)
        return total_data, movie_list

if __name__ == '__main__':
    main()
