'''
Created on 24.06.2011

@author: philipp
'''

from libavg import avg

"""
Button class to extend

ImageNode with text
"""
"""
wird nicht mehr gebraucht!

class Button(avg.ImageNode):
    '''
    classdocs
    '''
    
    def __init__(self, text, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.player = avg.Player.get()
        
        self.bText = text
        self.parent = self.getParent()
        # background of button
        self.background = self.player.getElementByID(self.id)
        # text in der Mitte 
        self.text = avg.WordsNode(text=self.bText, pos=(self.pos.x+ self.size.x /2, self.pos.y+ self.size.y/2.7), size = self.size, alignment="center", parent=self.parent)

"""




class AnswerButton(avg.DivNode):
    '''
    AnswerButton extend DivNode
    if answer is true -> backgroudimg change to (green)
            false -> " " " (red)
    '''
    
    def __init__(self, text, TorF, level, menue, hide=False, *args, **kwargs):
        super(AnswerButton, self).__init__(text, level, *args, **kwargs)
        self.player= avg.Player.get()
        
        self.text = text
        self.level = level
        self.menue = menue
        self.TorF = TorF        # entscheidet ob die Antwort richitg oder Falsch ist
        self.hide = hide        # wenn hide true, dann wird die Seitenleiste mit Bildern eingeblendet (default = false)
        
        self.true = avg.ImageNode(href="green.png", size=(self.size.x-2,self.size.y-2), pos=(self.pos.x+1,self.pos.y+1), opacity=0, parent=self.getParent())
        self.false = avg.ImageNode(href="red.png", size=(self.size.x-2,self.size.y-2), pos=(self.pos.x+1,self.pos.y+1), opacity=0, parent=self.getParent())
        self.bg = avg.WordsNode(text=text, size=self.size, pos=(self.pos.x + self.size.x/2, self.pos.y ), alignment="center",  font="Arial Black", fontsize=50, parent= self.getParent())
        
        self.clickevent = self.bg.setEventHandler(avg.CURSORUP,avg.MOUSE, self.click)
        
    # Click the right button -> solved field -> true + green (false->red)    
    def click(self, event):
        if self.TorF:
            avg.fadeIn(self.true, 500, 1).setStopCallback(self.showInfo)   # Button wird gruen
            self.level.solved = True        # feld von Level (parent) wird auf true gesetzt
            self.menue.changePic()          # Menue: Solarzelle wird gruen
            if self.hide:                   # blednet Seitenleiste ein
                self.level.slideIn()
        else:
            avg.fadeIn(self.false, 500, 1)  # Button wird rot
            self.level.qFalse = self.level.qFalse + 1   # Frage falsch beantwortet -> Conter wird erhoeht
    
    def showInfo(self):
        for button in self.level.a:
            button.bg.sensitive = False
            avg.fadeOut(button.bg, 1000)
            avg.fadeOut(button.true, 1000)
            avg.fadeOut(button.false, 1000)
        avg.fadeIn(self.level.info, 1000)
    
    def showButton(self):
        self.bg.sensitive = True
        avg.fadeIn(self.bg, 1000)
    
    def reset(self):
        # reset the answerbutton 
        avg.fadeOut(self.true,1000)
        avg.fadeOut(self.false,1000)





        
class MistakePoint(avg.ImageNode):
    '''
    MistakePoint
    
    takes: found(is point found True/False), mistakefound(WordsNode: number of found points)
    '''
    
    
    def __init__(self, found, level, *args, **kwargs):
        super(MistakePoint, self).__init__(*args, **kwargs)
        self.found = found
        self.level = level
        
        self.setEventHandler(avg.CURSORDOWN, avg.MOUSE | avg.TOUCH, self.isFound)
        
    def isFound(self, event):
        # wenn die Fehler-Stelle im Bild angetippt wird, wird ein roter Kreis an dieser Stelle eingeblendet
        avg.fadeIn(event.node, 500)
        avg.LinearAnim(event.node, "pos", 500, (event.node.pos.x +event.node.size.x/2, event.node.pos.y+event.node.size.y/2), (event.node.pos.x,event.node.pos.y) ).start()
        avg.LinearAnim(event.node, "size", 500, (0,0), (event.node.size.x,event.node.size.y) ).start()
        self.level.mistakecounter = self.level.mistakecounter +1            # Fehlercounter wird um 1 erhoeht
        #self.level.mistakefound.text = str(self.level.mistakecounter)
        self.level.mistakedisplay.text = "Fehler "+ str(self.level.mistakecounter) + "/"+ str(self.level.mistakesum)
        self.found = True           # found feld wird auf true gesetzt (spaeter wichitg fuer Abrage ob alle Fehler gefunden sind)
        self.sensitive = False      # Fehler wird "deaktiviert" damit der Counter nicht durch eine Stelle immer wieder erhoeht werden kann
        #self.deactive()
    
    def deactive(self):
        if self.found:
            self.sensitive = False
    
    def reset(self):
        # Reset des Fehlerbuttons
        self.found = False
        self.sensitive = True
        self.opacity = 0
        #self.level.mistakecounter = 0
        
        

class Piece(avg.ImageNode):
    '''
    Piece of Puzzle
    
    takes: rpos(right position of piece)
    '''
    
    def __init__(self, rpos, *args, **kwargs):
        super(Piece, self).__init__(*args, **kwargs)
        self.rpos = rpos
        