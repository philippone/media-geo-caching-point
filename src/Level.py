'''
Created on 24.06.2011

@author: philipp
'''

from libavg import avg
from Buttons import AnswerButton, MistakePoint, Piece


class Level(avg.DivNode):
    '''
    Level class
    
    extends: DivNode
    
    takes: menue(reference to got_menue Button)
    '''
    
    def __init__(self, menue, *args, **kwargs):
        '''
        Constructor
        '''
        super(Level, self).__init__( *args, **kwargs)
        self.player = avg.Player.get()
        self.solved = False         # feld ob Level geloest
        self.qFalse = 0             # feld wie oft falsch beantwortet
        self.menue = menue          # feld welches menue zum level gehoert
    
    
    
    
class Question(Level):
    '''
    LEVEL: QUESTION

    extend Level

    takes: question(string), answers(sting List), solution(string a1-a4), pics(string list), menue(reference to goto_menue Button)
    '''
    
    

    def __init__(self, question, answers, solution, pics, menue, infotext="", *args, **kwargs):
        '''
        Constructor
        '''
        super(Question, self).__init__(menue, *args, **kwargs)
        self.question = question    # "Frage"
        self.answers = answers      # ["a1", "a2" ,...]
        self.pics = pics            # {pic1.jpg, pic2.jpg,...}
        self.solution = solution
        self.infotext = infotext    # "infotext"
        
        self.captureHolder = None
        self.captureHolder2 = None
        self.dragOffset = 0
        self.timeid = 0
        self.old_pos = 0
        self.dragOffsetX = 0
        self.dragOffsetY = 0
        self.longclicked = False
        self.current_event = None
        
        # main div
        self.main=avg.DivNode(pos=(200,130), size=(1070,690), parent= self)
        # Question
        self.q_bgr = avg.ImageNode(pos=(0,0), size=(1070,90), href="Div-Backround.png", parent= self.main)
        
        
        # set fontsize
        if len(self.question) < 50:
            self.length = 40
        elif len(self.question) < 90:
            self.length = 25 
        else:
            self.length = 15
        self.q = avg.WordsNode( pos=(self.q_bgr.size.x/2,self.q_bgr.pos.y+10), font="Arial Black", fontsize=self.length+5, alignment="center", text=question, parent= self.main)
        
        # range
        self.range = avg.DivNode(pos=(0,120), size=(1070,570), parent=self.main)
        self.r_bgr = avg.ImageNode(pos=(0,0), size=self.range.size, href="Div-Backround.png", parent= self.range)
        # answer buttons
        py = 50
        i=0
        self.a = []
        for a in self.answers:
            self.a.append( AnswerButton(text=a, TorF=False, level=self, menue= self.menue, pos=(220,py), size=(630,70),  parent= self.range) )
            py = py + 90
            i = i+1
        # decision 
        if self.solution == "a1":
            self.a[0].TorF = True
        elif self.solution == "a2":
            self.a[1].TorF = True
        elif self.solution == "a3":
            self.a[2].TorF = True
        else:
            self.a[3].TorF = True
            
        # Info
        self.info = avg.DivNode(pos=(0,120), size=(1050, 580), opacity=0, sensitive=False, crop= True, parent = self.main)
        self.info_text = avg.WordsNode(text=self.infotext, pos=(10,10), size=(1030, 560), font="Arial", fontsize=20, parent= self.info)
        
        # bottombar
        self.bottom = avg.DivNode(pos=(200,840), size=(1070,60), parent=self)
        self.b_bgr = avg.ImageNode(href="Div-Backround.png", pos=(0,0),size=self.bottom.size, parent=self.bottom)
        self.backX = avg.WordsNode(text="X", pos=(self.bottom.size.x-10, 5), font="Arial Black", fontsize=30, alignment="right",parent=self.bottom)
        # information to drag
        self.help = avg.WordsNode(text="Ziehe das Bild in die Mitte, um es zu vergroessern", pos=(10,5), font="Arial Black", fontsize=30, alignment="left", opacity=0, parent=self.bottom)
        
        # Sidebar
        self.sidebar = avg.DivNode(pos=(1360,0), size=(560,1200), parent=self)
        self.sb_bg = avg.ImageNode(href="Div-Backround.png", pos=(0,0), size=(560,1200), parent=self.sidebar)
        self.scroll = avg.DivNode(pos=(10,0), parent= self.sidebar)
        # Div for big picture
        self.bigP = avg.DivNode(pos=(-1170,125), size=(1070, 690), parent=self.scroll)
        # close button
        self.close = avg.WordsNode(text="X", font="Arial Black", fontsize=30, pos=(1245, 90), opacity=0, parent=self)
        px = 0
        py = 0
        i = 0
        self.picture = []
        # pics in sidebar
        for pic in self.pics:
            self.picture.append( avg.ImageNode(href=pic, pos=(px,py), size=(550,406), parent=self.scroll) )
            self.scroll.size = avg.Point2D(550, self.scroll.size.y + 406.0)
            self.picture[i].setEventHandler(avg.CURSORDOWN, avg.MOUSE | avg.TOUCH, self.startZoom)
            self.picture[i].setEventHandler(avg.CURSORMOTION, avg.MOUSE | avg.TOUCH, self.moveToZoom)
            self.picture[i].setEventHandler(avg.CURSORUP, avg.MOUSE | avg.TOUCH, self.endZoom)
            py = py+ 410
            i = i +1
       
        
        # Evetns
        # go back
        self.backEvent = self.backX.setEventHandler(avg.CURSORUP, avg.MOUSE| avg.TOUCH, self.goback)
        # Scrolling + fadein
        self.sidebar.setEventHandler(avg.CURSORDOWN, avg.MOUSE | avg.TOUCH, self.startScroll)
        self.sidebar.setEventHandler(avg.CURSORMOTION, avg.MOUSE | avg.TOUCH, self.doScroll)
        self.sidebar.setEventHandler(avg.CURSORUP, avg.MOUSE | avg.TOUCH, self.endScroll)
        self.sidebar.setEventHandler(avg.CURSOROUT, avg.MOUSE | avg.TOUCH, self.endScroll)
        # close button
        self.close.setEventHandler(avg.CURSORDOWN, avg.MOUSE | avg.TOUCH, self.zoomOut)
        
        
    """
    Scrollfunktion der Bilderleiste
    """   
    def startScroll(self, event):
        # startet das Scrollen
        avg.fadeIn(self.help, 500)          # Hilfetext wird eingeblendet (, dass man das Bild in die Mitte ziehen kann um es zu vergroessern)
        ny = self.scroll.pos.y
        y = event.pos.y
        if self.captureHolder is None:
            self.captureHolder = event.cursorid
            self.dragOffset = ny - y                # Verschiebung nur in der y-Achse
            
    
    def doScroll(self, event):
        # sehbare Verschiebung mit dem Mauszeiger(Finger)
        if event.cursorid == self.captureHolder:
            self.scroll.pos = avg.Point2D(self.scroll.pos.x, event.pos.y + self.dragOffset)
    
    def endScroll(self, event):
        # Ende des Scrollen (loslassen)
        avg.fadeOut(self.help, 500)
        if event.cursorid == self.captureHolder:
            self.captureHolder = None
        if self.scroll.pos.y  > 100:    # eig. ... > 0    # Wenn das oberste Bild weiter runter als 100 px gezogen wird, wird es wieder nach oben gesetzt              
            avg.EaseInOutAnim(self.scroll, "y", 1000, self.scroll.pos.y, 0, 50, 1000).start()
        if self.scroll.pos.y + self.scroll.size.y +350 <= event.node.size.y:    # das gleiche fuer das letzte Bild (wird wieder nach oben geschoben, wenn es zuweit unten ist)
            avg.EaseInOutAnim(self.scroll, "y", 1000, self.scroll.pos.y, -((len(self.picture)*410)-1080) , 50, 1000).start() #self.scroll.pos.y +250
        # > 100 und +350 als Toleranz!
    """
    Zoomfunktion der Bilder
    """
    def startZoom(self, event):
        if self.captureHolder2 is None:
            self.captureHolder2 = event.cursorid
            event.node.setEventCapture(event.cursorid)
            self.old_pos = event.node.pos                       # alte Position wird gespeichert (Postion in der Leiste)
            self.current_event = event.node                     # die Node (Bildreferenz) wird gespeichert
            self.dragOffsetX = event.node.pos.x - event.pos.x   # kann nur in der x-Achse verschoben werden
            event.node.sensitive = False
            for answer in self.a:                               # damit die Antwortbuttons unter dem Bild nicht versehentlich gedrueckt werden
                answer.sensitive = False
    
    def endZoom(self, event):
        # Entscheidung ob Bild vergroessert wird oder nicht:
        if self.captureHolder2 == event.cursorid:
            event.node.releaseEventCapture(event.cursorid)
            
            if event.node.pos.x  < -100:                        # wenn das Bild umm 100px nach links verschoben wird
                self.sidebar.sensitive =  False                 # wird die Leiste (scrollen) deaktiviert
                self.doZoom(event)                              # doZoom() -> vergroessert das Bild
            else:
                self.sidebar.sensitive = True                   
                self.doNotZoom(event)                           # verschiebt das Bild an die vorherige Position, sofern es nicht mehr als 100px nach links verschoben wurde
    
    def moveToZoom(self, event):
        # Bewegung des Bildes in der x-Achse
        if self.captureHolder2 == event.cursorid:
            event.node.pos = avg.Point2D(event.pos.x + self.dragOffsetX, event.node.pos.y)
            
    def doZoom(self, event):
        # Bild wird vergroessert und auf die richitge Position gesetzt + "x"-Schliessen-Button wird eingeblendet
        avg.EaseInOutAnim(event.node, "pos", 1000, event.node.pos, avg.Point2D(- 1170, 130+ (-self.scroll.pos.y)), 50, 1000).start()
        avg.EaseInOutAnim(event.node, "size", 1000, event.node.size, avg.Point2D(1070,690), 50, 1000).start()
        avg.fadeIn(self.close, 1000)
        
    
    def zoomOut(self, event):
        # Das Bild wird verkleinert
        pic = self.current_event                                                                    # gespeicherte Referenz
        avg.EaseInOutAnim(pic, "pos", 1000, pic.pos, (0,self.old_pos.y), 50, 1000).start()          # Animation zum verschieben
        avg.EaseInOutAnim(pic, "size", 1000, pic.size, avg.Point2D(550,406), 50, 1000).start()      # Animation zum verkleinern
        self.sidebar.sensitive = True
        avg.fadeOut(self.close, 1000)
        self.captureHolder2 = None
        self.current_event.sensitive = True
        for answer in self.a:                                                                       # Antworten wieder anklickbar
                answer.sensitive = True
              
    def doNotZoom(self, event):
        # Das Bild wird nicht vergroessert, sondern nur an seine Stelle in der Leiste zurueck verschoben
        avg.EaseInOutAnim(event.node, "pos", 1000, event.node.pos, (0,self.old_pos.y), 50, 1000).start() 
        self.captureHolder2 = None
        event.node.sensitive = True
        for answer in self.a:
                answer.sensitive = True

    def goback(self, event):
        #background = self.player.getElementByID("background")
        homescreen = self.player.getElementByID("homescreen")
        levelslide = avg.EaseInOutAnim(self, "x", 1000, self.pos.x, self.pos.x + self.size.x , 50, 1000).start()
        homeslide= avg.EaseInOutAnim(homescreen, "x", 1000, homescreen.pos.x, homescreen.pos.x + homescreen.size.x/1.4 , 50, 1000).start()
        # Infotext weg dafuer Buttons wieder her
        avg.fadeOut(self.info, 1000)
        for button in self.a:
            button.showButton()
        
    
    def reset(self):
        # Reset der Frage
        self.solved = False
        self.qFalse = 0
        for answer in self.a:
            answer.reset()
        self.sidebar.sensitive = True
        self.close.opacity = 0
        self.captureHolder2 = None
        if self.current_event != None:
            self.current_event.sensitive = True
        py = 0
        for p in self.picture:                  # alle Bilder werden in die Seitenleiste gesetzt, falls (eins) vergroessert ist
            p.pos = avg.Point2D(0,py)
            p.size = avg.Point2D(550,406)
            py = py + 410






class QuestionHideSidebar(Question):
    '''
    LEVEL: Question Hide Sidebar
    
    extend Question
    
    takes: question(string), answers(sting List), solution(string a1-a4), pics(string list), menue(reference to goto_menue Button)
    '''
    
    def __init__(self, question, answers, solution, pics, menue, *args, **kwargs):
        super(QuestionHideSidebar, self).__init__(question, answers, solution, pics, menue, *args, **kwargs)
        self.main.pos = (400,130)
        self.bottom.pos = (400,840)
        self.sidebar.pos = (1920,0)
        for answer in self.a:
            answer.hide = True
    
    def slideIn(self):
        # die Bilderleiste wird eingeblendet (aufgerufen im AnswerButton, wenn die Frage richtig beanwortet wird)
        avg.EaseInOutAnim(self.main, "pos", 1000, self.main.pos, (200,130), 50, 1000).start()
        avg.EaseInOutAnim(self.bottom, "pos", 1000, self.bottom.pos, (200,840), 50, 1000).start()
        avg.EaseInOutAnim(self.sidebar, "pos", 1000, self.sidebar.pos, (1360,0), 50, 1000).start()

    # Override
    def reset(self):
        # Reset von QuestionHide
        self.solved = False
        self.qFalse = 0
        for answer in self.a:
            answer.reset()
        self.sidebar.sensitive = True
        self.close.opacity = 0
        self.captureHolder2 = None
        if self.current_event != None:
            self.current_event.sensitive = True
        py = 0
        for p in self.picture:
            p.pos = avg.Point2D(0,py)
            p.size = avg.Point2D(550,406)
            py = py + 410
        self.main.pos = (400,130)           # "Fenster" werden wieder richtig gerueckt (die selben 3 wie bei slideIn() verschoben werden)
        self.bottom.pos = (400,840)
        self.sidebar.pos = (1920,0)
        






class SearchMistake(Level):
    '''
    LEVEL: Search the mistake 

    extend Level

    takes:  orgpic(original picture), fakepic(picture with mistakes), mPos(List of mistakes's location) ,menue(reference to goto_menue Button)
    '''
    
    def __init__(self, orgpic, fakepic, mPos, menue, *args, **kwargs):
        super(SearchMistake, self).__init__(menue, *args, **kwargs)
        self.orgpic = orgpic
        self.fakepic = fakepic
        self.mPos = mPos            # mistake positions
        self.mistakesum = len(mPos) # sum of mistakes
        
        
        # node for pics
        self.pics = avg.DivNode(pos=(80, 50), size=(1760, 920), parent=self)
        # bottom node
        self.bottom = avg.DivNode(pos=(80,990), size=(1760, 60), parent= self)
        self.leftb = avg.ImageNode(href="Div-Backround.png", pos=(0,0), size=(870,60), parent= self.bottom)
        self.back = avg.WordsNode(text="X", pos=(1730,10), alignment="right", fontsize=30, font="Arial Black", parent= self.bottom)
        avg.WordsNode(text="Originalbild", pos=(850, 10), font="Arial Black", fontsize=30, alignment="right", parent =self.bottom)
        self.rightb = avg.ImageNode(href="Div-Backround.png", pos=(890,0), size=(870,60), parent= self.bottom)
        self.back = avg.WordsNode(text="X", pos=(1730,10), alignment="right", fontsize=30, font="Arial Black", parent= self.bottom)
        avg.WordsNode(text="Fehlerbild", pos=(910, 10), font="Arial Black", fontsize=30, parent =self.bottom)
        # static in MistakePoint, here only for first implementation of self.mistakefound
        self.mistakecounter = 0
        # shows how many mistakes were found
        self.mistakedisplay = avg.WordsNode(text="Fehler "+ str(self.mistakecounter) +"/"+str(self.mistakesum)  , pos=(20, 10), font="Arial Black", fontsize=30, parent =self.bottom)
        # original pic
        self.orgpic_bgr = avg.ImageNode(href="Div-Backround.png", pos=(0,0), size=(870, 920), parent= self.pics)
        self.orgpicNode = avg.ImageNode(href=self.orgpic, pos=(20,20), size=(830,880), parent= self.pics)
        # fake pic
        self.fakepic_bgr = avg.ImageNode(href="Div-Backround.png", pos=(890,0), size=(870, 920), parent= self.pics)
        self.fakepicDiv = avg.DivNode(pos=(910,20), size=(830,880), parent= self.pics)
        self.fakepicNode = avg.ImageNode(href=self.fakepic, pos=(0, 0), size=(830,880), parent = self.fakepicDiv)
        # click the mistake to show a red circle around them
        self.div = []
        self.circ = []
        for position in self.mPos: 
            self.circ.append(MistakePoint(href="mistake/circle.png", found=False, level = self, pos = position, size=(50,50), opacity=0, parent=self.fakepicDiv) )

        #Events
        self.back.setEventHandler(avg.CURSORDOWN, avg.MOUSE | avg.TOUCH, self.goback)
        self.intervalS = self.player.setInterval(500, self.isSolved)
        
            
    def goback(self, event):
        # back to homescreen
        level = self.player.getElementByID(self.id)
        homescreen = self.player.getElementByID("homescreen")
        avg.EaseInOutAnim(level, "x", 1000, level.pos.x, level.pos.x + level.size.x , 50, 1000).start() # level slide out
        avg.EaseInOutAnim(homescreen, "x", 1000, homescreen.pos.x, homescreen.pos.x + homescreen.size.x/1.4 , 50, 1000).start() # homescreen slide in
    
    def isSolved(self):
        # ueberprueft ob das Level geloest wurde (gefundene Fehler == Anzahl der Fehler im Bild)
        if self.mistakesum == self.mistakecounter:
            self.player.clearInterval(self.intervalS)    # Interval wird gestoppt (ob Level geloest)
            self.menue.changePic()                      # Bild von Menue wird gruen
            self.mistakedisplay.color = "098e09"        # "Fehler 5/5" wird gruen
            self.solved = True                          # level feld wird auf true gesetzt (wichitg fuer Main.isSolved)

    def reset(self):
        # reset Level
        if self.solved:
            self.intervalS = self.player.setInterval(500, self.isSolved) # startet das Interval wieder (ob Level geloest)
            self.solved = False
        self.mistakecounter = 0                                     # gefundene Fehler = 0
        self.mistakedisplay.text = "Fehler 0/"+str(self.mistakesum) # "Fehler 0/5" 
        self.mistakedisplay.color = "FFFFFF"                        # wird wieder weiss
        # reset MistakeButton
        for p in self.circ:
            p.reset()   # jeder rote Kreis wird ausgeblendet
        
        




   
   
   
            
class Puzzle(Level):
    '''
    LEVEL: Puzzle
    
    extend Level
    
    takes: thumbnail(small pic to see the final situation), pieces(List of 16 pieces -> size of piece(245,232.5)), rfield(String of fieldnumber)
    '''
    
    """
    positions for pieces
    """
    one     = (20,20)
    two     = (275, 20)
    three    = (530,20)
    four    = (785,20)
    
    five    = (20, 262.5)
    six     = (275, 262.5)
    seven   = (530,262.5)
    eight   = (785, 262.5)
    
    nine    = (20, 505)
    ten     = (275, 505)
    eleven  = (530, 505)
    twelve  = (785, 505)
    
    thirteen    = (20, 747.5)
    fourteen    = (275, 747.5)
    fifteen     = (530, 747.5)
    sixteen     = (785, 747.5)
    randomPositions = [ ten, fifteen, four, eleven, two, three,  five, sixteen, six, seven,  thirteen, nine, one,  twelve,  fourteen, eight]
    
    
    def __init__(self, thumbnail, pieces, rfield, *args, **kwargs):
        super(Puzzle, self).__init__(*args, **kwargs)
        self.thumbnail = thumbnail
        self.rfield = rfield    # right field 
        self.solved = False     # is level solved
        self.started = False    # is level started
        
        # main
        self.main = avg.DivNode(pos=(100,50), size=(1720, 1000), parent= self)
        # thumbnail
        self.tnDiv = avg.DivNode(pos=(1070,0), size=(650, 619), parent= self.main)
        self.tnDiv_bgr = avg.ImageNode(href="Div-Backround.png", pos=(0,0), size=(650, 619), parent= self.tnDiv)
        self.tnImg = avg.ImageNode(href= self.thumbnail, pos=(20,20), size=(610, 579), parent= self.tnDiv)
        # description
        self.description = avg.DivNode(pos=(1070,639), size=(650, 271), parent= self.main)
        self.descriptioin_bgr = avg.ImageNode(href="Div-Backround.png", pos=(0,0), size=(650, 271), parent= self.description)
        self.description_text = avg.WordsNode(text="Tippe zwei Puzzelteile an,<br/>um sie zu tauschen", pos=(610, 10), alignment="right", font="Arial Black", fontsize=30, parent=self.description)
        self.timecounter = avg.WordsNode(text="0:0:0 - Zeit", pos=(610,120), font="Arial Black", fontsize=30, alignment="right", parent=self.description)
        self.changecounter = avg.WordsNode(text="0 - Zuege", pos=(610,150), font="Arial Black", fontsize=30, alignment="right", parent=self.description)
        self.changeCV = 0
        # back
        self.back = avg.DivNode(pos=(1070,930), size=(650, 70), parent= self.main)
        self.back_bgr = avg.ImageNode(href="Div-Backround.png", pos=(0,0), size=(650, 70), parent= self.back)
        self.back_X = avg.WordsNode(text="X", font="Arial Black", fontsize=30, alignment="right", pos=(610, 10), parent=self.back)
        # puzzle
        self.puzzle = avg.DivNode(pos=(0,0), size=(1050, 1000), parent= self.main)
        self.puzzle_bgr = avg.ImageNode(href="Div-Backround.png", pos=(0,0), size=(1050, 1000), parent=self.puzzle)
        
        # right position of pieces
        self.rightpos = []
        for nr in self.rfield:
            if nr == 1:
                self.rightpos.append(Puzzle.one)
            if nr == 2:
                self.rightpos.append(Puzzle.two)
            if nr == 3:
                self.rightpos.append(Puzzle.three)
            if nr == 4:
                self.rightpos.append(Puzzle.four)
            if nr == 5:
                self.rightpos.append(Puzzle.five)
            if nr == 6:
                self.rightpos.append(Puzzle.six)
            if nr == 7:
                self.rightpos.append(Puzzle.seven)
            if nr == 8:
                self.rightpos.append(Puzzle.eight)
            if nr == 9:
                self.rightpos.append(Puzzle.nine)
            if nr == 10:
                self.rightpos.append(Puzzle.ten)
            if nr == 11:
                self.rightpos.append(Puzzle.eleven)
            if nr == 12:
                self.rightpos.append(Puzzle.twelve)
            if nr == 13:
                self.rightpos.append(Puzzle.thirteen)
            if nr == 14:
                self.rightpos.append(Puzzle.fourteen)
            if nr == 15:
                self.rightpos.append(Puzzle.fifteen)
            if nr == 16:
                self.rightpos.append(Puzzle.sixteen)
        # location of pices
        self.rpieces = []
        px = 20
        py = 20
        p = 1
        i = 0
        for pi in pieces:
            self.rpieces.append( Piece(href=pi, pos=(px, py), rpos=self.rightpos[i], size=(245, 232.5), parent=self.puzzle))
            self.rpieces[i].setEventHandler(avg.CURSORUP, avg.MOUSE, self.choose)
            if p == 4 or p == 8 or p == 12:
                px = 20
                py = py + 242.5
            else:
                px = px + 255
            p = p + 1
            i = i+1
        
        # Events
        self.back_X.setEventHandler(avg.CURSORUP, avg.MOUSE | avg.TOUCH, self.goback)
        # for pieces event
        self.choosen = 0
        self.node1 = None
        self.oldpos1 = (0,0)
        # decicion
        self.interval = self.player.setInterval(500, self.isSolved)
        self.counterStarted = False
        self.h = 1
        self.m = 1
        self.s = 1
        self.timeinterval = None
        self.ptochange = None
        
        
    def choose(self, event):
        # startet einmal den Timer/Counter
        if self.counterStarted:
            pass
        else:
            self.timeinterval = self.player.setInterval(1000, self.time)
            self.counterStarted = True
        # vertauscht die zwei Teile
        if self.choosen == 1:
            # change pics
            self.node1.pos = event.node.pos
            event.node.pos = self.oldpos1
            
            """
            """
            self.ptochange.href = self.ptochange.href[:-6] + ".png"
            """
            """
            # raise counter
            self.changeCV = self.changeCV + 1
            self.changecounter.text = str(self.changeCV) + " - Zuege"
            # click #2
            self.choosen = 0
        else:
            self.cursorid1 = True # -1
            self.node1 = event.node
            self.oldpos1 = event.node.pos
            """
            hervorhebung
            """
            self.ptochange = event.node
            event.node.href = event.node.href[:-4] + "_c.png"
            
            """
            """
            # click #1
            self.choosen = 1
    
    def isSolved(self):
        # ueberprueft ob alle puzzelteile an der richtigen position liegen
        solved = False
        for node in self.rpieces:
            if node.pos == node.rpos:
                solved = True
            else:
                solved = False
                break   
        if solved:
            # Wenn das Level geloest, dann wird das Menuebild geaendert und das interval gestoppt
            self.solved = True
            self.menue.changePic()
            self.player.clearInterval(self.interval)
            
    def time(self):
        # level started
        self.started = True
        # zaehlt die Zeit, solange das Level noch nicht geloest ist
        if self.solved == False:
            if self.s % 60 == 0:
                self.timecounter.text = str(self.h-1) + ":" + str(self.m-1) + ":" + str(self.s-1) + " - Zeit"
                self.m = self.m + 1
                self.s = 0
            if self.m % 60 == 0:
                self.timecounter.text = str(self.h-1) + ":" + str(self.m-1) + ":" + str(self.s-1) + " - Zeit"
                self.h = self.h +1               
                self.m = 1
                self.s = 0
            else:
                self.timecounter.text = str(self.h-1) + ":" + str(self.m-1) + ":" + str(self.s-1) + " - Zeit"
                self.s = self.s + 1
        else:
            # wenn Level geloest, dann stoppt das zeitinterval und Zeit und Zuege werden gruen
            self.player.clearInterval(self.timeinterval)
            self.timecounter.color = "098e09"
            self.changecounter.color = "098e09"
            
    def goback(self, event):
        # back to homescreen
        level = self.player.getElementByID(self.id)
        background = self.player.getElementByID("background")
        homescreen = self.player.getElementByID("homescreen")
        levelslide = avg.EaseInOutAnim(level, "x", 1000, level.pos.x, level.pos.x + level.size.x , 50, 1000).start()
        homeslide= avg.EaseInOutAnim(homescreen, "x", 1000, homescreen.pos.x, homescreen.pos.x + homescreen.size.x/1.4 , 50, 1000).start()
        
    def reset(self):
        if self.solved == False:
            if self.started:
                self.player.clearInterval(self.timeinterval)            # stoppt die Zeit
        if self.solved:
            self.interval = self.player.setInterval(500, self.isSolved)
        #reset timer
        self.h = 1
        self.m = 1
        self.s = 1
        self.timecounter.text = "0:0:0 - Zeit"
        self.timecounter.color = "FFFFFF"
        self.changecounter.color = "FFFFFF"
        self.counterStarted = False
        # reset move counter
        self.changeCV = 0
        self.changecounter.text = "0 - Zuege"
        # reset pieces pos
        i = 0
        for p in self.rpieces:
            p.pos = Puzzle.randomPositions[i]
            i = i + 1
        self.solved = False     # level wieder ungeloest
        self.started = False    # level noch nicht gestartet
        
        