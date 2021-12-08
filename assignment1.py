"""
Replace the contents of this module docstring with your own details
Name: Davin Natanael
Date started: 08 December 2021
GitHub URL:https://github.com/davinnataz/assignment-1---movies-to-watch-davinnataz-master.git
"""

import csv
import operator

def read_file():
    #this function to open a movies.csv files for adding a movie there
    csv_file = open('movies.csv')
    csv_read = csv.reader(csv_file, delimiter=',')
    total_data = 0
    movies_list = []
    for row in csv_read:
        movie = []
        movie.append(row[0])
        movie.append(int(row[1]))
        movie.append(row[2])
        movie.append(row[3])
        total_data += 1
        movies_list.append(movie)
    return total_data, movies_list

def main():
    #this is a main function from this program
    """..."""
    total_data, movies_list = read_file()

    print("Movies To Watch 1.0 - by Davin Natanael")
    print(f"{total_data} movies loaded")

    while True:
        print_menu()
        menu = input(">>> ").upper()
        if (menu == 'L'):
            total_data, movies_list = Listed_movies(total_data,movies_list)
        elif (menu == 'A'):
            total_data, movies_list = add_movie(total_data,movies_list)
        elif (menu == 'W'):
            total_data, movies_list = watch_movies(total_data,movies_list)
        elif (menu == "Q"):
            quit_movies(total_data, movies_list)
            break
        else:   
            print("Menu not found")


def print_menu():  
    print("Menu:")
    print("L - List movies")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q - Quit")


def Listed_movies (total_data,movies_list):
    #this function is to show the list of movie and give knowledge if this movie is watched or not
    i = 0
    u = 0
    w = 0
    movies_list.sort(key=operator.itemgetter(1))
    for row in movies_list:
        if (row[3] == "u"):
            print(f"{i}. * {row[0]} \t\t\t - {row[1]} ({row[2]})")
            u += 1
        else:
            print(f"{i}.   {row[0]} \t\t\t - {row[1]} ({row[2]})")
            w += 1
        i += 1
    print(f"{w} movie watched, {u} movies still to watch")
    return total_data, movies_list


def watch_movies(total_data, movies_list):
    #this function is to watch a movie
    j = 0
    for row in movies_list:
        if (row[3] == 'w'):
            j += 1

    if (j == total_data):
        print("no more movies to watch")
        return total_data, movies_list

    print("Enter the number of a movie to mark as watched")
    while True:

        try:
            menu = int(input(">>> "))
        except ValueError:
            print("Invalid Input; Enter a valid number")
            continue

        if (total_data == 0):
            print("no records found")
        elif (menu < 0):
            print("Number must be >= 0")
        elif (menu >= total_data):
            print("Invalid movie number")
        else:
            if (movies_list[menu][3] == "w"):
                print(f"You have already watched {movies_list[menu][0]}")
            else:
                movies_list[menu][3] = "w"
                print(f"{movies_list[menu][0]} from {movies_list[menu][1]} watched")
            break

    return total_data, movies_list





if __name__ == '__main__':
    main()

