def check_winner(board):
  for row in board:
    if all(row[i] == row[0] for i in range(len(row))) and row[0] != ".":
      return row[0]

  
  for col in range(3):
    if all(board[i][col] == board[0][col] for i in range(len(board))) and board[0][col] != ".":
      return board[0][col]

 
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ".":
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ".":
    return board[0][2]



 
  return "DRAW"

def main():

  t = int(input())

  for _ in range(t):
    board = []
    for _ in range(3):
      board.append(input())

    print(check_winner(board))

if __name__ == "__main__":
  main()
