"""
Replace the contents of this module docstring with your own details
Name: Davin Natanael
Date started: 08 December 2021
GitHub URL:https://github.com/davinnataz/assignment-1---movies-to-watch-davinnataz-master.git
"""

import csv
import operator

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


def main():
    # this is a main menu for movie to watch
    """..."""
    total_data, movies_list = read_file()
    print("Movies To Watch 1.0 - by Davin Natanael")
    print(f"{total_data} movies loaded")
    while True:
        print_menu()
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





def print_menu():
    #to show a menu
    print("Menu : ")
    print("L - List movie")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q - Quit")


def movies_list(total_data, movie_list):
    #to show a list movie and knowledge if it is watched or not
    i = 0
    u = 0
    w = 0
    movie_list.sort(key=operator.itemgetter(1))
    for row in movie_list:
        i += 1
        if row[3] == "u":
            u += 1
            print(f"{i}. * {row[0]} - {row[1]} ({row[2]})")
        else:
            w += 1
            print(f"{i}. * {row[0]} - {row[1]} ({row[2]})")
    print(f"{w} movie watched, {u} movies still to watch")
    return total_data, movie_list


if __name__ == '__main__':
    main()
