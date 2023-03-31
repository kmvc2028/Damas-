import pygame
from copy import deepcopy
from constants import *


def minimax(position, depth, max_player, game):
    #la profundidad es 0 o si hay un ganador, se devuelve la evaluación de la posición actual.
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    # Si el jugador actual es el jugador máximo, se busca el mejor movimiento para el jugador.
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            # Se obtiene la evaluación del movimiento actual.
            evaluation = minimax(move, depth-1, False, game)[0]
            print (minimax(move, depth-1, False, game))
            # Se actualiza el valor máximo y se guarda el movimiento actual si la evaluación es igual.
            maxEval = max(maxEval, evaluation)
            print(maxEval)
            if maxEval == evaluation:
                best_move = move
                print(move)

        return maxEval, best_move
    # Si el jugador actual no es el jugador máximo, se busca el mejor movimiento para el oponente.
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            # Se actualiza el valor mínimo y se guarda el movimiento actual si la evaluación es igual.
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    # Si se saltó una pieza, se elimina del tablero.
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            #draw_moves(game, board, piece)
            #Se crea una copia del tablero y de la pieza para simular el movimiento.
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.window)
    pygame.draw.circle(game.window, (0, 255, 0), (piece.x, piece.y), 30, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(1500)



