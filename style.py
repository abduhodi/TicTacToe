from PyQt5.QtGui import QPixmap

class Style:
    TURN = -1

    def active():
        style = """
        font-size: 24px;
        color: #820000;
        font-weight: 600;
        """
        return style
    
    def inactive():
        style = """
        font-size: 14px;
        color: #181823;
        """
        return style

    def X():
        style = """
        font-size: 24px;
        color: #181823;
        font-weight:600;
        """
        return style

    def O():
        style = """
        font-size: 24px;
        color: #16FF00;
        font-weight:600;
        """
        return style

    def normal():
        style = """
        font-size: 14px;
        color: #181823;
        """
        return style
    