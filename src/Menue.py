'''
Created on 23.06.2011

@author: philipp
'''

from libavg import avg

class MenueImage(avg.ImageNode):
    '''
    classdocs
    '''
    

    def __init__(self, presspic, solvedpic, levelid, *args, **kwargs):
        '''
        Constructor
        '''
        super(MenueImage, self).__init__(*args, **kwargs)
        self.player = avg.Player.get() 
        self.presspic = presspic    
        self.solvedpic = solvedpic  
        self.startpic = self.href
        self.levelid = levelid      # "level1" , "level2", ...
        self.intern_solved = False  # level am Anfang ungeloest -> solved = false
        self.i= 0
        self.startanimOn = True         # ist die Startanimation an?
        
        self.root = self.player.getRootNode()
        
        self.setEventHandler(avg.CURSOROVER, avg.MOUSE | avg.TOUCH, self.MouseOverPic)
        self.setEventHandler(avg.CURSOROUT, avg.MOUSE | avg.TOUCH, self.MouseOutPic)
        self.setEventHandler(avg.CURSORUP, avg.MOUSE | avg.TOUCH, self.MouseUpPic)
        
        
    def MouseOverPic(self,event):
        # Mouse over -> pic change to presspic
        if self.intern_solved:
            pass
        else:                                   # solange das Level noch nicht geloest wurde, also noch nicht gruen ist -> wird es gelb wenn man darueber geht
            event.node.href = self.presspic
            avg.fadeIn(self, 700)
        
    def MouseOutPic(self, event):
        # Mouse out -> pic change to startpic
        if self.intern_solved:                  # wenn das level geloest ist dann passiert nichts -> bleibt gruen
            pass
            #event.node.href = self.solvedpic
            #elf.opacity = 0
        else:                                   # gelb wird wieder ausgeblendet
            event.node.href = self.startpic
            self.opacity = 0
        
    def MouseUpPic(self, event):
        homescreen = self.player.getElementByID("homescreen")
        level = self.player.getElementByID(self.levelid)
        # Homescreen slide out
        avg.EaseInOutAnim(homescreen, "x", 1000, homescreen.pos.x, homescreen.pos.x - homescreen.size.x/1.4 , 50, 1000).start()
        # Level slide in
        avg.EaseInOutAnim(level, "x", 1000, level.pos.x, 0 , 50, 1000).start()
        
        
    def changePic(self):
        # die Zelle wird gruen
        self.opacity = 0            # zur Sicherheit, dass die Animation wirkich einblendent
        self.href= self.solvedpic   # zur Sicherheit, dass es das richtige Bild ist
        avg.fadeIn(self, 1000)      # blendet die gruene Solarzelle ein
        self.intern_solved = True   
    
    def reset(self):
        # reset the menue
        self.href = self.startpic   # normales Startbild
        avg.fadeOut(self, 100)      # "button/bild" ausgeblendet -> man sieht das dahinterligende Skuplturbild
        self.intern_solved = False  # intern_solved wieder auf false
        
    def blinking(self):
        # Blinken:
        self.opacity = 0            # zur Sicherheit
        self.href = self.presspic   #  "      "
        self.startanimOn = True     # Animation ist an
        if self.i <= 2:             # i = index 
            avg.fadeIn(self, 1000).setStopCallback(self.blinkingCont)   # 0, 1, 2 - > 3 mal einblenden -> jedes mal nach der Animation zu blinkingCont
        else:
            avg.fadeIn(self, 1000).setStopCallback(self.blinkingOff)    # 4. mal einblenden -> danach zu blinkingOff
        #self.href = self.startpic
        
    def blinkingCont(self):
        avg.fadeOut(self, 1000).setStopCallback(self.blinking)          # ausblenden + zurueck zu blinking
        self.i = self.i + 1                                             # index += 1
            
    def blinkingOff(self):
        # letztes ausblenden
        avg.fadeOut(self, 1000)
        self.i = 0                                                      # index zurueck auf 0 setzen
        self.startanimOn = False                                        # animtion ist beendet == nicht mehr an (false)
        self.sensitive = True
        
        
        