import json
import io
from random import randint

get_riddles = open('riddles.json', 'r')
riddles = json.load(get_riddles)
# for riddle in riddles['riddles_list']:
    # print(riddle)


# def create_room():
#     row = 10
#     column = 10
#     get_rooms = open('rooms.json', 'r')
#     rooms = json.load(get_rooms)
#     random_number = randint(0, 9)
#     room = rooms["rooms_list"][random_number]
#     if row == 0 and column == 0:
#         board_dict[(row, column)] = room
#         # return room[random_index]['rooms']
#
# print(create_room())
# for room in rooms['rooms_list']:
#     print(room)

get_riddles.close()


# def make_board(rows, columns):
#     board = {}
#     for row in range(rows):
#         for column in range(columns):
#             board[(row, column)] = "Johnson"
#             if column == 1:
#                 print("\n")
#             print(board)
#     # print(row, column)# ["Welcome to the pit of doom", None]
#     return board
#
# print(make_board(10,10))

#
def make_board(rows: int, columns: int) -> dict:
    board_dict = {}
    get_rooms = open('rooms.json', 'r')
    rooms = json.load(get_rooms)
    hallway = {'room': 'hallway'}
    for row in range(rows):
        for column in range(columns):
            if row == randint(0, 9) or column == randint(0, 9):
                board_dict[(row, column)] = rooms["rooms_list"][randint(0, 9)]
            else:
                board_dict[(row, column)] = hallway
    return board_dict



def make_riddle(character: dict) -> bool:
    riddles_dict = {}
    get_riddles = open('riddles.json', 'r')
    riddles = json.load(get_riddles)
    if (character['x-coordinate'], character['y-coordinate']) ==


def check_for_challenge():
  if room != hallway:
      return True
  else:
      return False


there_is_a_challenge = check_for_challenge()

