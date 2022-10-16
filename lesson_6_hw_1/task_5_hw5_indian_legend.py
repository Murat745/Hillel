"""
Lesson 6, homework 5, task 5 solution.
Indian legend
"""
wheat_quant_kg = float(input('Enter the wheat quantity in kg: '))
grains_quant = wheat_quant_kg / 0.000035
sum_grains_list = [int(2**i) for i in range(64)]
chess_board_list = []
numbers = range(1, 9)
letters = range(97, 105)

for i in letters:
    for j in numbers:
        chess = f'{chr(i)}{j}'
        chess_board_list.append(chess)

for index, n in enumerate(sum_grains_list):
    if grains_quant <= n:
        print('Chess cell coordinates are:', chess_board_list[index])
        break
