import curses
from random import randint

curses.initscr()
win = curses.newwin(20, 60, 0, 0)
curses.noecho()
curses.curs_set(0)

snake = [[4,10], [4,9], [4,8]]
food = [10,20]
score = 0

win.keypad(1)
key = curses.KEY_RIGHT
prevKey = curses.KEY_RIGHT

win.addch(food[0], food[1], '*')

while key != 27:
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    win.addstr(0, 27, ' SNAKE ')
    win.timeout(int(150 - (len(snake)/5 + len(snake)/10)%120))
    
    event = win.getch()
    if (event != -1):
        prevKey = key
        key = event

    if key == ord(' '):
        key = -1
        win.addstr(10, 25, ' PAUSED ')
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        win.addstr(10, 25, '        ')
        continue
    
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, 27]:
        key = prevKey
        
    if (key == curses.KEY_LEFT and prevKey == curses.KEY_RIGHT):
        key = prevKey
    elif (key == curses.KEY_RIGHT and prevKey == curses.KEY_LEFT):
        key = prevKey
    elif (key == curses.KEY_UP and prevKey == curses.KEY_DOWN):
        key = prevKey
    elif (key == curses.KEY_DOWN and prevKey == curses.KEY_UP):
        key = prevKey
        
    if(key == curses.KEY_DOWN):
        snake.insert(0, [snake[0][0] + 1, snake[0][1]])
    elif(key == curses.KEY_UP):
        snake.insert(0, [snake[0][0] - 1, snake[0][1]])
    elif(key == curses.KEY_LEFT):
        snake.insert(0, [snake[0][0], snake[0][1] - 1])
    elif(key == curses.KEY_RIGHT):
        snake.insert(0, [snake[0][0], snake[0][1] + 1])
        
    if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break
    #OU
    """  OPCIONAL
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1
    """
    
    if snake[0] in snake[1:]: break

    if snake[0] == food:
        score += 1
        food = []
        while food == []:
            food = [randint(1, 18), randint(1, 58)]
            if food in snake: food = []    
        win.addch(food[0], food[1], '*')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
        
    win.addch(snake[0][0], snake[0][1], '#')
        
curses.endwin()

print("\nScore - " + str(score))