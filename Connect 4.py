from cmu_graphics import *

def onAppStart(app):
    app.rows = 6
    app.cols = 7
    app.boardLeft = 70
    app.boardTop = 120
    app.boardWidth = app.width-130
    app.boardHeight = app.height-130
    app.cellBorderWidth = 2
    app.turn = "A"
    app.start = True
    app.PlayerA = ["purple" for x in range(21)]
    app.Ax = 104
    app.Ay = 80
    app.newCircleA = True
    app.PlayerB = ["yellow" for y in range(21)]
    app.Bx = 506
    app.By = 80
    app.newCircleB = True
    app.board = [[None for x in range(7)] for y in range(6)]
    app.scene = "Round"
    app.win = None
    app.allowed = True
    app.restartRectLeft = 270
    app.restartRectWidth = 60
    app.restartRectTop = 328
    app.restartRectHeight = 25
    
def redrawAll(app):
    if app.scene == "Round":
        drawBoard(app)
        drawBoardBorder(app)
        rounds(app)
        play(app)
        if app.win == "winA":
            win(app, "A")
        if app.win == "winB":
            win(app, "B")

def rounds(app):    
    drawLabel("Connect 4", app.width//2, 80, font = 'montserrat', fill = 'pink', align = 'center', bold = True, size = 35)
    drawCircle(app.Ax, app.Ay, 30, fill = 'thistle', align = 'center', border = "plum" )
    drawCircle(app.Bx, app.By, 30, fill = 'lemonChiffon', align = 'center', border = "moccasin" )
    drawLabel("Player A", 104, 30, font = 'montserrat', fill = "plum", align = "center", bold = True, size = 20)
    drawLabel("Player B", 506, 30, font = 'montserrat', fill = "moccasin", align = "center", bold = True, size = 20)

def play(app):
    rows = [159, 238, 316, 394, 473, 551]
    cols = [104, 171, 238, 305, 372, 439, 506]
    for i in range(len(app.board)):
        for j in range(len(app.board[0])):
            if app.board[i][j] == "purple":
                drawCircle(cols[j], rows[i], 30, fill = 'thistle', align = 'center', border = "plum" )
            if app.board[i][j] == "yellow":
                drawCircle(cols[j], rows[i], 30, fill = 'lemonChiffon', align = 'center', border = "moccasin" )

def onKeyPress(app, key):
    if app.allowed == True:
        if key == 'space':
            if app.turn == "A":
                drop(app, "A")
            elif app.turn == "B":
                drop(app, "B")
        if key == "right" or key == "d":
            if app.turn == "A":
                move(app, "right", "A")
            if app.turn == "B":
                move(app, "right", "B")
        if key == "left" or key == "a":
            if app.turn == "A":
                move(app, "left", "A")
            if app.turn == "B":
                move(app, "left", "B")

def onMousePress(app, mouseX, mouseY):
    right = app.restartRectLeft + app.restartRectWidth
    bottom = app.restartRectTop + app.restartRectHeight
    if (app.restartRectLeft <= mouseX <= right) and (app.restartRectTop <= mouseY <= bottom):
        reset(app)

def drop(app, player):
    cols = [104, 171, 238, 305, 372, 439, 506]
    c = None
    
    if player == "A":
        for y in range(len(cols)):
            if cols[y] == app.Ax:
                c = y
    if player == "B":
        for y in range(len(cols)):
            if cols[y] == app.Bx:
                c = y
        
    if player == "A":   
        for i in range(5, -1, -1):
            if app.board[i][c] == None:
                app.board[i][c] = "purple"
                app.PlayerA.pop()
                app.start = False
                app.Ax = 104
                app.Ay = 80
                app.turn = "B"
                break    
    if player == "B":
        for i in range(5, -1, -1):
            if app.board[i][c] == None:
                app.board[i][c] = "yellow"
                app.PlayerB.pop()
                app.start = False
                app.Bx = 506
                app.By = 80
                app.turn = "A"
                break
    calcWinDiagonal(app)
    calcWinHorizontal(app)
    calcWinVertical(app)
    

def move(app, direction, player):
    if player == "A":
        if direction == "right":
            if 103 < app.Ax < 505:
                app.Ax += 67
        if direction == "left":
            if 105 < app.Ax < 507:
                app.Ax -= 67
    if player == "B":
        if direction == "right":
            if 103 < app.Bx < 505:
                app.Bx += 67
        if direction == "left":
            if 105 < app.Bx < 507:
                app.Bx -= 67
    
def calcWinHorizontal(app):
    for c in range(len(app.board[0]) - 3):
        for r in range(len(app.board)):
            if app.board[r][c] == "purple" and app.board[r][c+1] == "purple" and app.board[r][c+2] == 'purple' and app.board[r][c+3] == "purple":
                app.win = "winA"
                app.allowed = False
            elif app.board[r][c] == "yellow" and app.board[r][c+1] == "yellow" and app.board[r][c+2] == 'yellow' and app.board[r][c+3] == "yellow":
                app.win = "winB"
                app.allowed = False
                
def calcWinVertical(app):
    for c in range(len(app.board[0])):
        for r in range(len(app.board) - 3):
            if app.board[r][c] == "purple" and app.board[r+1][c] == "purple" and app.board[r+2][c] == 'purple' and app.board[r+3][c] == "purple":
                app.win = "winA"
                app.allowed = False
            elif app.board[r][c] == "yellow" and app.board[r+1][c] == "yellow" and app.board[r+2][c] == 'yellow' and app.board[r+3][c] == "yellow":
                app.win = "winB"
                app.allowed = False
                
def calcWinDiagonal(app):
    for c in range(len(app.board[0]) - 3):
        for r in range(len(app.board) - 3):
            if app.board[r][c] == "purple" and app.board[r+1][c+1] == "purple" and app.board[r+2][c+2] == 'purple' and app.board[r+3][c+3] == "purple":
                app.win = "winA"
                app.allowed = False
            elif app.board[r][c] == "yellow" and app.board[r+1][c+1] == "yellow" and app.board[r+2][c+2] == 'yellow' and app.board[r+3][c+3] == "yellow":
                app.win = "winB"
                app.allowed = False

def win(app, player):
    if player == "A":
        drawLabel("Player A wins!!!!", app.width//2, app.height//2, font = 'montserrat', size = 50, fill = 'thistle', bold = True, border = "plum")
        drawRect(300, 340, 60, 25, border = 'plum', fill = 'thistle', align = 'center')
        drawLabel("Restart", 300, 340, align = 'center', font = 'montserrat', fill = "orchid")
    if player == "B":
        drawLabel("Player B wins!!!", app.width//2, app.height//2, font = 'montserrat', size = 50, fill = 'lemonChiffon', bold = True, border = "moccasin")
        drawRect(300, 340, 60, 25, border = 'moccasin', fill = 'lemonChiffon', align = 'center')
        drawLabel("Restart", 300, 340, align = 'center', font = 'montserrat', fill = 'peachPuff')
        
def reset(app):
    app.PlayerA = ["purple" for x in range(21)]
    app.PlayerB = ["yellow" for y in range(21)]
    app.board = [[None for x in range(7)] for y in range(6)]
    app.scene = "Round"
    app.win = None
    app.allowed = True
    app.turn = "A"

##From CMU CS Academy
def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col)

def drawBoardBorder(app):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='pink',
           borderWidth=2*app.cellBorderWidth)
           
def drawCell(app, row, col):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=None, border='pink',
             borderWidth=app.cellBorderWidth)

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)
    
def main():
    runApp(width = 600, height = 600)
    
main()   
    
