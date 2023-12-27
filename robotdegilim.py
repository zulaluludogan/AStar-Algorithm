import numpy as np

class Node:
    def __init__(me,board_array,g_n,fval,move):
        """ Initialize the node with the board_array, level of the node and the calculated f function value """
        me.board_array = board_array
        me.g_n = g_n
        me.fval = fval
        me.move = move

    def find_number_position(me, board_array, number):
      return (np.where(board_array == number)[0][0], np.where(board_array == number)[1][0])

    def find_star_position(me, board_array):
      """ Find the star position """
      return (np.where(board_array == 0)[0][0], np.where(board_array == 0)[1][0])

    def apply_move(me, board_array, move):
        """ Applies a single move to the board array"""
        board_array_cp = np.copy(board_array)
        star_position = me.find_star_position(board_array)
        xn, yn = star_position[1]+move[1], star_position[0]+move[0]

        if (0<= xn <=2 and 0<= yn <=2):
          board_array_cp[ star_position[0], star_position[1] ], board_array_cp[yn, xn] = board_array_cp[yn, xn], board_array_cp[ star_position[0], star_position[1] ]
          return board_array_cp
        else:
          return None

    def possible_boards(me):
      star_x, star_y = me.find_star_position(me.board_array)
      possible_moves = ([1,0],[-1,0],[0,1],[0,-1])
      children = []

      for i in possible_moves:
            child = me.apply_move(me.board_array, i)
            if child is not None:
                child_node = Node(child,me.g_n+1,0,i)
                children.append(child_node)
      return children

class Solve8():
  def __init__(me):
    me.open = []
    me.closed = []

  def __str__(me):
    return 'RobotDeğilim'

  def find_number_position(me, board_array, number):
      return (np.where(board_array == number)[0][0], np.where(board_array == number)[1][0])

  def f_function(me, root):
    return me.heuristic(root.board_array) + root.g_n

  def heuristic(me, root_array):
    cost = 0
    for number in range(1,9):
      # row, column = me.find_number_position(root.board_array, number)
      row, column = np.where(root_array == number)[0][0], np.where(root_array == number)[1][0]

      row_winner = number // 3 if (number % 3 != 0) else (0 if number == 3 else 1)
      column_winner = number - row_winner * 3 - 1
      cost += abs(row -  row_winner)
      cost += abs(column - column_winner)
      # print(f"number: {number}")
      # print(f"row: {row}, column: {column}")
      # print(f"row_winner: {row_winner}, column_winner: {column_winner}")
      # print("____________________-")
    return cost

  def Solve(me,  Tile):
    root = Node(Tile.Board,0,0,0)
    root.fval = me.f_function(root)
    # do some magic
    me.open.append(root)
    movez = []

    while True:
            cur = me.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.board_array:
                for j in i:
                    print(j,end=" ")
                print("")

            if(me.heuristic(cur.board_array) == 0):
                movez.append(cur.move)
                break

            for i in cur.possible_boards():
                i.fval = me.f_function(i)
                me.open.append(i)
                
            me.closed.append(cur)
            movez.append(cur.move)
            # print(movez)
            del me.open[0]

            """ sort the open list based on f value """
            me.open.sort(key = lambda x:x.fval,reverse=False)

    del movez[0]    
    return movez
