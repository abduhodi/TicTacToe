from PyQt6.QtWidgets import QMessageBox


class Check_win:
    PLAYER1 = 0
    PLAYER2 = 0
    DRAW = 0
    def winner(btn_list: list):
        for btns in btn_list:
            check = ''
            for btn in btns:
                check += btn.text()
            if check == "XXX":
                return 1 
            if check == "OOO":
                return 2

        check = ''
        for i in range(len(btn_list)):
            check = ''
            for j in range(len(btn_list)):
                check += btn_list[j][i].text()
            if check == "XXX":
                return 1 
            if check == "OOO":
                return 2
        check = ''
        
        for i in range(len(btn_list)):
            check += btn_list[i][len(btn_list) - i - 1].text()
        if check == "XXX":
            return 1 
        if check == "OOO":
            return 2
        check = ''

        for i in range(len(btn_list)):
            check += btn_list[i][i].text()
        if check == "XXX":
            return 1 
        if check == "OOO":
            return 2

        return 0 

    def is_all_occupied(btn_list: list):
        for i in range(len(btn_list)):
            for j in range(len(btn_list)):
                if btn_list[i][j].text() == " ":
                    return False
        return True
