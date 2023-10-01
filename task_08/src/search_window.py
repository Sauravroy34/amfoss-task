
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QHBoxLayout
import requests
from PySide6.QtGui import QPixmap
from PySide6.QtCore import  QRect 


class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()


        
        #self.image_url = self.search()["sprites"]["front_default"]
        self.labelpic = QLabel(self)            
        self.w = None  
        if self.search() == 4:
           self.labelpic.setPixmap("assests/grey.png")
       
        #self.labelpic.setGeometry(QRect(400, 20, 550, 700))
        if self.search() != 4:
            self.labelpic.setPixmap(QPixmap("assets/landing.jpg"))
            self.labelpic.setScaledContents(True) 

       
            
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
      



        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)


        #my code
        enter_button.clicked.connect(self.search)
        #my code
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)

        self.poke = QLabel(self)
        self.poke.setGeometry(QRect(400,20,550,700))

    def search(self):
        global stats 
        try :
            req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.textbox.text()}")
            url= req.json()["sprites"]["front_default"]
            stats = req.json()["abilities"][0]["ability"]["name"]
            print(stats)
            print(url)
            
            return 4
        except:
            pass



class saved(QWidget):
    def __init__(self):
        super().__init__()
            

    #my code
    
    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
