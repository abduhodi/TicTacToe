import random
from check import Check_win

class Computer_second:
    def easy(block_list: list):
        cells = []
        for i in range(len(block_list)):
            for j in range(len(block_list)):
                if block_list[i][j].text() == ' ':
                    cells.append(block_list[i][j])
        return random.choice(cells)


    def is_first_move(block_list: list):
        x = 0
        for i in range(len(block_list)):
            for j in range(len(block_list)):
                if block_list[i][j].text() == 'X':
                    x += 1
                if x == 2:
                    return False
        return True


    def find_doubleX(block_list: list):
        length = len(block_list)
        for i, btns in enumerate(block_list):
            btns = [btn.text() for btn in btns]
            if btns.count("X") == 2 and " " in btns:
                return block_list[i][btns.index(" ")]
        
        for i in range(length):
            cell = []
            for j in range(length):
                cell.append(block_list[j][i].text())
            if cell.count("X") == 2 and " " in cell:
                return block_list[cell.index(" ")][i]
        
        cell = []
        for i in range(length):
            cell.append(block_list[i][length-i-1].text())
        if cell.count("X") == 2 and " " in cell:
            ind = cell.index(" ")
            return block_list[ind][length-ind-1]
        
        cell = []
        for i in range(length):
            cell.append(block_list[i][i].text())
        if cell.count("X") == 2 and " " in cell:
            ind = cell.index(" ")
            return block_list[ind][ind]

        return None


    def find_doubleO(block_list: list):
        length = len(block_list)
        for i, btns in enumerate(block_list):
            btns = [btn.text() for btn in btns]
            if btns.count("O") == 2 and " " in btns:
                return block_list[i][btns.index(" ")]
        
        for i in range(length):
            cell = []
            for j in range(length):
                cell.append(block_list[j][i].text())
            if cell.count("O") == 2 and " " in cell:
                return block_list[cell.index(" ")][i]
        
        cell = []
        for i in range(length):
            cell.append(block_list[i][length-i-1].text())
        if cell.count("O") == 2 and " " in cell:
            ind = cell.index(" ")
            return block_list[ind][length-ind-1]
        
        cell = []
        for i in range(length):
            cell.append(block_list[i][i].text())
        if cell.count("O") == 2 and " " in cell:
            ind = cell.index(" ")
            return block_list[ind][ind]

        return None

    def back_diagonal(block_list: list):
        cell = ''
        cell += block_list[0][2].text()
        cell += block_list[1][1].text()
        cell += block_list[2][0].text()
        return cell


    def diagonal(block_list: list):
        cell = ''
        cell += block_list[0][0].text()
        cell += block_list[1][1].text()
        cell += block_list[2][2].text()
        return cell


    def corner(block_list: list):
        cells = []
        if block_list[0][0].text() == ' ':
            cells.append(block_list[0][0])
        if block_list[0][2].text() == ' ':
            cells.append(block_list[0][2])
        if block_list[2][0].text() == ' ':
            cells.append(block_list[2][0])
        if block_list[2][2].text() == ' ':
            cells.append(block_list[2][2])
        return cells

    
    def plus(block_list: list):
        cells = []
        if block_list[0][1].text() == ' ':
            cells.append(block_list[0][1])
        if block_list[1][0].text() == ' ':
            cells.append(block_list[1][0])
        if block_list[1][2].text() == ' ':
            cells.append(block_list[1][2])
        if block_list[2][1].text() == ' ':
            cells.append(block_list[2][1])
        return cells


    def singleO(block_list: list):
        length = len(block_list)
        for i, btns in enumerate(block_list):
            btns = [btn.text() for btn in btns]
            if btns.count("O") == 1 and btns.count(" ") == 2:
                return block_list[i][btns.index(" ")]
        
        for i in range(length):
            cell = []
            for j in range(length):
                cell.append(block_list[j][i].text())
            if cell.count("O") == 1 and cell.count(" ") == 2:
                return block_list[cell.index(" ")][i]
        
        cell = []
        for i in range(length):
            cell.append(block_list[i][length-i-1].text())
        if cell.count("O") == 1 and cell.count(" ") == 2:
            ind = cell.index(" ")
            return block_list[ind][length-ind-1]
        
        cell = []
        for i in range(length):
            cell.append(block_list[i][i].text())
        if cell.count("O") == 1 and cell.count(" ") == 2:
            ind = cell.index(" ")
            return block_list[ind][ind]

        return None        


    def empty(block_list: list):
        cells = []
        for i in range(len(block_list)):
            for j in range(len(block_list)):
                if block_list[i][j].text() == " ":
                    cells.append(block_list[i][j])
        return cells


    def hard(self, block_list: list):
        if self.is_first_move(block_list):
            if block_list[1][1].text() == ' ':
                return block_list[1][1]
            else:
                return random.choice(self.corner(block_list))
        else:
            winning = self.find_doubleO(block_list)
            if winning is not None:
                return winning
            warning = self.find_doubleX(block_list)
            if warning is not None:
                return warning
            if (self.back_diagonal(block_list) or self.diagonal(block_list)) in ["XXO", "OXX"]:
                btn = self.corner(block_list)
                if btn:
                    return random.choice(btn)
            if (self.back_diagonal(block_list) or self.diagonal(block_list)) == 'XOX':
                btn = self.plus(block_list)
                if btn:
                    return random.choice(btn)
            btn = self.singleO(block_list)
            if btn is not None:
                return btn
            else:
                return random.choice(self.empty(block_list))