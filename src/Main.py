'''
Created on 23.06.2011

@author: philipp
'''
#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-


from libavg import avg, AVGApp

from Menue import MenueImage
from Level import Question, SearchMistake, Puzzle, QuestionHideSidebar
#from Meue.VideoPlayer import VideoPlayer


class Main(AVGApp):
    
    
    def __init__(self, parent):
        self.player = avg.Player.get()
        self.root = self.player.getRootNode() #rootNode
        # fullscreen activate
        self.player.setResolution(False, 1920, 1080, 32)    # fullscreen (on, off)
        
        # size of mainfraime
        self.size_root = self.player.getRootNode().size

        self.abTop = 180    # Abstand nach oben
        self.abLeft = 150   # Anstand nach unten

        # Startscreen  
        self.homescreen = avg.DivNode(id="homescreen", pos=(0,0),size=(1920,1080), parent = self.root)
        # background
        self.background = avg.ImageNode(id="background", pos=(0,-1080), href="background3.jpg", parent = self.homescreen)
        
        # title (MEDIA GEO CACHING POINT)
        self.title_bgr_M = avg.ImageNode(id="title_bgr_M", pos=(460,30), size=(340,90), href="Div-Backround.png", parent= self.homescreen)
        self.title_bgr_G = avg.ImageNode(id="title_bgr_G", pos=(70,120), size=(730,90), href="Div-Backround.png", parent= self.homescreen)
        self.title_bgr_P = avg.ImageNode(id="title_bgr_P", pos=(470,210), size=(330,90), href="Div-Backround.png", parent= self.homescreen)
        self.title1 = avg.WordsNode(id="Title1", pos=(800,10), text="MEDIA", fontsize=90, font="Arial Black",alignment="right",  parent= self.homescreen)
        self.title2 = avg.WordsNode(id="Title2", pos=(800,100), text="GEO-CACHING", fontsize=90, font="Arial Black",alignment="right",  parent= self.homescreen)
        self.title3 = avg.WordsNode(id="Title3", pos=(800,190), text="POINT", fontsize=90, font="Arial Black",alignment="right",  parent= self.homescreen)
        
        # description title (Herzlich willkommen)
        self.welcome = avg.ImageNode(id="Welcome",  pos=(440, 370), size=(360, 40), href="Div-Backround.png", parent = self.homescreen)
        self.welc = avg.WordsNode(id="Welc", text="Herzlich Willkommen!" ,pos=(800, 370), alignment="right", font="Arial Black", fontsize=30, parent=self.homescreen)
        # description (blabla...)
        self.description = avg.ImageNode(id="Div-Background", href="Div-Backround.png", size=(740, 600), pos=(60, 420), parent = self.homescreen)
        self.descr = avg.WordsNode(id="descr", text="Sie befinden sich hier an einem multimedialen <br/> Geo-Caching Punkt. <br/> Um das Versteck zu finden muessen Sie 13 Level bestehen.<br/>Nachdem Sie das Spiel gestartet haben blinken die <br/>Solarzellen der Statur, die mit einem Level <br/>ausgestattet sind. Mit einem Klick auf eine <br/>dieser Zellen gelangen sie zum Level. <br/><br/> Viel Glueck!", pos=(70,425), size=(730, 595), font="Arial Black", fontsize=25, parent = self.homescreen)
        
        # koordinate-div
        self.end = avg.DivNode(id="end", pos=(0,-1080/2.4), size=(1920, 1080/2.4), opacity=0, parent=self.homescreen)
        self.left = avg.DivNode(id="left", pos=(60,100), size=(740, 900), parent=self.end)
        self.koord_bgr =  avg.ImageNode(id="brg_koord", pos=(0,0), size=(740, 900), href="Div-Backround.png", parent= self.left)
        self.koord_text = avg.WordsNode(id="k_t", text="Herzlichen Glueckwunsch!<br/><br/>Sie haben alle Level geloest und bekommen jetzt<br/>die Koordinaten, an denen sich das Logbuch<br/>befindet.<br/> Sie haben 10 min Zeit um sich die Koordinaten zu <br/>notieren. Danach wird das Spiel neugestartet.", font="Arial Black", fontsize=25, pos=(20,20), parent=self.left)
        avg.WordsNode(text="49.257798,7.0419", font="Arial Black", fontsize=25, pos=(250,370), parent=self.left)
        # statistic
        avg.WordsNode(text="Ihre Statistik", font="Arial Black", fontsize=25, pos=(20,500), parent=self.left)        
        avg.WordsNode(text="Gesamtzeit", font="Arial Black", fontsize=25, pos=(40,550), parent=self.left)
        self.oaTime = avg.WordsNode(text="0:0:0 h", font="Arial Black", fontsize=25, pos=(40,590), parent=self.left)
        avg.WordsNode(text="Frage zuerst falsch beantwortet?", font="Arial Black", fontsize=25, pos=(40,650), parent=self.left)
        self.qFalse = avg.WordsNode(text="0 mal", font="Arial Black", fontsize=25, pos=(40,690), parent=self.left)
        
        # Statur-Div
        self.statur = avg.DivNode(id="statur", pos=(self.size_root.x/2.2,0), size=(1004, 1200), parent=self.homescreen)
        avg.ImageNode(id="statur_pic", href="statur/statur.png", size=self.statur.size, pos=(0,0) ,parent=self.statur)
        # MenueBilder (statur)       
        # gotto level #
        self.goto_level1 = MenueImage(id="goto_level1", levelid="level1", sensitive = False, href="statur/tolevel/start/level1.png", presspic="statur/tolevel/press/level1.png", solvedpic="statur/tolevel/solved/level1.png",   pos=(452,36), size=(100,110),  parent = self.statur)  
        self.goto_level2 = MenueImage(id="goto_level2", levelid="level2", sensitive = False, href="statur/tolevel/start/level2.png", presspic="statur/tolevel/press/level2.png", solvedpic="statur/tolevel/solved/level2.png",   pos=(452,146), size=(100,110),  parent = self.statur)
        self.goto_level3 = MenueImage(id="goto_level3", levelid="level3", sensitive = False, href="statur/tolevel/start/level3.png", presspic="statur/tolevel/press/level3.png", solvedpic="statur/tolevel/solved/level3.png",   pos=(452,256), size=(100,110),  parent = self.statur)
        self.goto_level4 = MenueImage(id="goto_level4", levelid="level4", sensitive = False, href="statur/tolevel/start/level4.png", presspic="statur/tolevel/press/level4.png", solvedpic="statur/tolevel/solved/level4.png",   pos=(452,366), size=(100,110),  parent = self.statur)
        self.goto_level5 = MenueImage(id="goto_level5", levelid="level5", sensitive = False, href="statur/tolevel/start/level5.png", presspic="statur/tolevel/press/level5.png", solvedpic="statur/tolevel/solved/level5.png",   pos=(452,476), size=(100,110),  parent = self.statur)
        self.goto_level6 = MenueImage(id="goto_level6", levelid="level6", sensitive = False, href="statur/tolevel/start/level6.png", presspic="statur/tolevel/press/level6.png", solvedpic="statur/tolevel/solved/level6.png",   pos=(452,586), size=(100,110),  parent = self.statur)
        self.goto_level7 = MenueImage(id="goto_level7", levelid="level7", sensitive = False, href="statur/tolevel/start/level7.png", presspic="statur/tolevel/press/level7.png", solvedpic="statur/tolevel/solved/level7.png",   pos=(452,696), size=(100,110),  parent = self.statur)
        # left side
        self.goto_level8 = MenueImage(id="goto_level8", levelid="level8", sensitive = False, href="statur/tolevel/start/level8.png", presspic="statur/tolevel/press/level8.png", solvedpic="statur/tolevel/solved/level8.png",   pos=(352,428), size=(100,110),  parent = self.statur)
        self.goto_level9 = MenueImage(id="goto_level9", levelid="level9", sensitive = False, href="statur/tolevel/start/level9.png", presspic="statur/tolevel/press/level9.png", solvedpic="statur/tolevel/solved/level9.png",   pos=(260,499), size=(92,110),  parent = self.statur)
        self.goto_level10 = MenueImage(id="goto_level10", levelid="level10", sensitive = False, href="statur/tolevel/start/level10.png", presspic="statur/tolevel/press/level10.png", solvedpic="statur/tolevel/solved/level10.png",   pos=(152,575), size=(108,110),  parent = self.statur)
        # right side
        self.goto_level11 = MenueImage(id="goto_level11", levelid="level11", sensitive = False, href="statur/tolevel/start/level11.png", presspic="statur/tolevel/press/level11.png", solvedpic="statur/tolevel/solved/level11.png",   pos=(552,428), size=(100,110),  parent = self.statur)
        self.goto_level12 = MenueImage(id="goto_level12", levelid="level12", sensitive = False, href="statur/tolevel/start/level12.png", presspic="statur/tolevel/press/level12.png", solvedpic="statur/tolevel/solved/level12.png",   pos=(652,499), size=(100,110),  parent = self.statur)
        self.goto_level13 = MenueImage(id="goto_level13", levelid="level13", sensitive = False, href="statur/tolevel/start/level13.png", presspic="statur/tolevel/press/level13.png", solvedpic="statur/tolevel/solved/level13.png",   pos=(752,566), size=(100,110),  parent = self.statur)
        
        
        # Level(s)
        self.level1 = Question(id="level1", menue=self.goto_level1, pos=(1920,0), size=(self.size_root), question="Wer ist der Kuenstler?", answers=["Fred George", "Thomas Rupp", "Dennis Neumann", "Dastin Rosemann"], solution="a1", pics= [ "pics/fred_george4.jpg", "pics/fredundtoni.jpg", "pics/sps1.jpg", "pics/aufbau.jpg", "pics/skulptur_nahe.jpg"], infotext="In seiner 30-jaehrigen Karriere als ein Fotograf hat Fred George das trainierte Auge eines sozialen Voyeurs verwendet, um aussergewoehnliche Bilder fuer Werbeagenturen und architektonische Unternehmen, sowie in der Musik, Kunst und Mode zu schaffen. George kreierte Bilder fuer Kampagnen der Philharmonie von Los Angeles, fuer das Getty- Zentrum, das Metropolitan- Museum der Kunst, das Kunstinstitut fuer Chicago, das Clevelander Museum der Kunst, das Museum der Modernen Kunst (New York), das amerikanische Museum der Naturgeschichte und das Joyce- Theater. Korporative Kunden haben American Express, Cartier, IBM, ATandT, Chase Manhattan Bank, Philip Morris Corporate Contributions, Canon und Citicorp eingeschlossen.<br/><br/>Seine Arbeit ist in Europa und Amerika, einschliesslich Berlin, Amsterdam, Paris, New York, und Los Angeles gezeigt worden. Hauptausstellungen waren u.a. die Art Basel (2004), Art Miami (2005), Europaeischer Monat der Fotografie (Berlin, 2006) und eine internationale Show von Reise-Fotografie, die in der franzoesischen Botschaft in New York begann. Seine Fotos der Innenstadt New Yorks sind in mehreren privaten und oeffentlichen Sammlungen, und Bilder der Nachwirkungen von 9/11 sind in New Yorks Historischer Gesellschaft ausgestellt worden.<br/><br/>George schafft Kunstwerke in vielfachen Medien, drueckt seine Bedenken in Bezug auf Politik und Umwelt aus, indem er Meinungen ueber Krieg, Geschlecht und Religion aeussert und anzweifelt. Er kritisiert die Unfehlbarkeit etablierter Symbole. Der Ash Wednesday 9/11 , Jesus as a Suicide Bomber  und AK-47 Crucifix  sind eindrucksvolle Beispiele.", parent= self.root)   
        self.level2 = Puzzle(id="level2", menue=self.goto_level2, pos=(1920,0), size=(self.size_root), thumbnail="Puzzle/peace/thumbnail.jpg", pieces=["Puzzle/peace/7.png", "Puzzle/peace/1.png", "Puzzle/peace/3.png", "Puzzle/peace/16.png", "Puzzle/peace/12.png", "Puzzle/peace/8.png", "Puzzle/peace/2.png", "Puzzle/peace/9.png", "Puzzle/peace/15.png", "Puzzle/peace/14.png", "Puzzle/peace/4.png", "Puzzle/peace/10.png", "Puzzle/peace/13.png", "Puzzle/peace/5.png", "Puzzle/peace/11.png", "Puzzle/peace/6.png"], rfield=[7,1,3,16,12,8,2,9,15,14,4,10,13,5,11,6], parent= self.root)   
        self.level3 = QuestionHideSidebar(id="level3", menue=self.goto_level3, pos=(1920,0), size=(self.size_root), question="Eine weitere Skulptur von Fred George hat die Form eines Kreuzes,<br/>woraus wurde diese gebaut?", answers=["Rohrbomben", "Autoreifen", "Skateboards","AK-47's"], solution="a4" , pics= ["pics/ak47_cross_4.jpg", "pics/two_ak47_close.jpg", "pics/fred_george4.jpg"], infotext="Die AK-47 Sculpture, eine 4 Meter hohe, kreuzfoermige Skulptur gebaut aus 42 ausgedienten AK-47, welche aus dem Bosnien Krieg stammen, ist eine politisch sowie religioes motivierte Arbeit des Kuenstlers Fred George. Die Skulptur ist dabei eine Kritik ueber aktuelle Konflikte, die durch religioese Ansichten sowie politisch Ziele (z.B. Oel) motiviert sind und soll durch Verzerrung der normierten Symboliken zum Nachdenken und zur emotionalen Reaktion anregen. Zuletzt zu sehen war die Skulptur auf der Koelner Kunstmesse Art.Fair sowie in der Stiftung STARKE in Berlin.", parent= self.root)   
        self.level4 = SearchMistake(id="level4", menue=self.goto_level4, pos=(1920,0), size=(self.size_root), orgpic="mistake/solar_org.jpg", fakepic="mistake/solar_fehler.jpg", mPos=[(0,124), (330,720) ,(474,579), (652,334), (738,546)] , parent= self.root)
        self.level5 = Question(id="level5", menue=self.goto_level5, pos=(1920,0), size=(self.size_root), question="Wie hoch soll die naechste SPS werden?", answers=["10 m", "12,5 m", "14 m","16 m"], solution="a1" , pics= ["pics/sps1.jpg", "pics/sps3.jpg", "pics/sps6.jpg", "pics/skulptur_nahe.jpg", "pics/aufbau.jpg"], infotext="Vom Startschuss bis zur Fertigstellung des 6-Meter-Modells waren nur 3 Wochen Zeit. Die 6-Meter Solar Peace Sculpture wurde im Saarland von der Firma G. Becker GmbH, St.Ingbert gebaut und fuer die Vernissage der Kunstmesse ART.FAIR 21 nach Koeln gebracht.<br/>Die Ingenieurleistung fuer die 6-Meter-Version fuer die ART.FAIR 21 wurde von Dipl. Ing. (FH) Bernd Eichenseer, Hochschule fuer Technik und Wirtschaft HTW erbracht.<br/><br/>Die statischen Berchnungen der 15-Meter Solar Peace Sculpture (2008-2010) wurden von Prof. Dr. Guenter Schmidt-Goenner HTW, Dipl. Ing. (FH) Eugen Schneider, Dipl. Ing. (FH) Matthias Kreuz und HTW Studenten durchgefuehrt.<br/><br/>Das Construction-Management wurde von Marcus Feld, f:kom, feld kommunikation und design, Saarbruecken, Bernd Eichenseer, HTW and Peter Schmitt, Koeln koordiniert.<br/><br/>Fuer Public Relations und das Projektmanagement war Sabine Feld, f:kom, feld kommunikation und design, Saarbruecken verantwortlich.<br/><br/>Die grafische Gestaltung des Fusses der Skulptur entstand in einer Zusammenarbeit zwischen Fred George and Marcus Feld.<br/><br/>",parent= self.root)
        self.level6 = QuestionHideSidebar(id="level6", menue=self.goto_level6, pos=(1920,0), size=(self.size_root), question="Wo wurde die 6m-Version der SPS zuerst aufgestellt?", answers=["ART.FAIR 21", "ArtQuerfeld", "Bremer Kunstfruehling","Crynet Art"], solution="a1" , pics= ["pics/sps1.jpg", "pics/sps_in_ny.jpg", "pics/fred_george4.jpg"], infotext="Seit nunmehr neun Jahren setzt die Koelner Kunstmesse ART.FAIR mit internationalen Music Acts, Video Shows und der Creme de la Creme der Koelner Tanz- und Performancekunst Trends.<br/>Auch in 2011 werden die Veranstalter wieder praesentieren, welche Symbiosen Kunst mit den unterschiedlichsten Sparten eingehen kann und welche spannenden und erfrischenden Projekte dabei entstehen.<br/><br/>ART meets FASHION<br/>ART meets PERFORMANCE<br/>ART meets MULTIMEDIA<br/>ART meets MUSIC<br/><br/>Zudem wird im Rahmen der ART.FAIR auch wieder die Verleihung des 'Warsteiner BLOOM-Award' stattfinden, ein Kunst- und Kreativwettbewerb , welcher mit 615 Teilnehmern im letzten Jahr einen fulminanten Auftrakt hatte.", parent= self.root)
        self.level7 = Puzzle(id="level7", menue=self.goto_level7, pos=(1920,0), size=(self.size_root), thumbnail="Puzzle/sculpture/thumbnail.jpg", pieces=["Puzzle/sculpture/7.png", "Puzzle/sculpture/1.png", "Puzzle/sculpture/3.png", "Puzzle/sculpture/16.png", "Puzzle/sculpture/12.png", "Puzzle/sculpture/8.png", "Puzzle/sculpture/2.png", "Puzzle/sculpture/9.png", "Puzzle/sculpture/15.png", "Puzzle/sculpture/14.png", "Puzzle/sculpture/4.png", "Puzzle/sculpture/10.png", "Puzzle/sculpture/13.png", "Puzzle/sculpture/5.png", "Puzzle/sculpture/11.png", "Puzzle/sculpture/6.png"], rfield=[7,1,3,16,12,8,2,9,15,14,4,10,13,5,11,6], parent= self.root)   
        self.level8 = QuestionHideSidebar(id="level8", menue=self.goto_level8, pos=(1920,0), size=(self.size_root), question="Welcher Aufstellungsort gehoert nicht zu denen, der fuer <br/>die 15m Version vorgesehen ist?", answers=["Madison Square", "Battery Park", "Nanjing Lu","Alexanderplatz"], solution="a4" , pics= ["pics/madison-square.jpg","pics/madison-square2.jpg", "pics/nanjing-lu.jpg", "pics/sps_in_ny.jpg", "pics/sps1.jpg"], infotext="Madison Square Park<br/>Madison Square ist ein Platz in New York City im Flatiron District des Stadtbezirks Manhattan und liegt an der Kreuzung von Fifth Avenue und Broadway an der 23rd Street. Das Herz des Platzes ist der 2,5 ha grosse Madison Square Park.Im Westen begrenzt die Kreuzung aus Fifth Avenue und Broadway den Madison Square Park. Der Platz und der Park befinden sich am noerdlichen Ende des Flatiron District. Die Bezeichnung Madison Square als Name fuer das Viertel ist heute kaum noch gebraeuchlich.<br/><br/>Battery Park<br/>Der Battery Park ist eine 8,09 Hektar grosse Parkanlage auf der Suedspitze Manhattans.<br/>In der Parkanlage selbst befinden sich neben dem Castle Clinton noch viele Denkmaeler wie das temporaere 9/11-Mahnmal The Sphere von Fritz Koenig, das Netherlands Memorial, das East Coast War Memorial, die Denkmaeler von John Ericsson, Giovanni da Verrazano und der Dichterin Emma Lazarus sowie das Denkmal der ersten juedischen Immigranten.<br/>Der Park hat seinen Namen von den niederlaendischen Geschuetzen, die einst hier postiert waren, um den damaligen Hafen von Neu-Amsterdam zu verteidigen. <br/><br/>Nanjing Lu<br/>Die Nanjing Lu (engl. Nanjing Road) in Shanghai ist eine der groessten Einkaufsstrassen der Welt.<br/>Die Nanjing Lu liegt in der Stadtmitte und verlaeuft in Ost-West-Richtung.<br/>Der oestliche Teil (Nanjing Doeng Lu) liegt im Stadtbezirk Huangpu und reicht vom Bund bis zum Volksplatz (Renmin Guangchang). Im Ostteil befindet sich eine Fussgaengerzone mit Geschaeften, Restaurants und Cafes, die durch ihre ueppigen Leuchtreklamen zahlreiche Touristen und einheimische Besucher anlocken.", parent= self.root)
        self.level9 = Puzzle(id="level9", menue=self.goto_level9, pos=(1920,0), size=(self.size_root), thumbnail="Puzzle/sps_ny/thumbnail.jpg", pieces=["Puzzle/sps_ny/7.png", "Puzzle/sps_ny/1.png", "Puzzle/sps_ny/3.png", "Puzzle/sps_ny/16.png", "Puzzle/sps_ny/12.png", "Puzzle/sps_ny/8.png", "Puzzle/sps_ny/2.png", "Puzzle/sps_ny/9.png", "Puzzle/sps_ny/15.png", "Puzzle/sps_ny/14.png", "Puzzle/sps_ny/4.png", "Puzzle/sps_ny/10.png", "Puzzle/sps_ny/13.png", "Puzzle/sps_ny/5.png", "Puzzle/sps_ny/11.png", "Puzzle/sps_ny/6.png"], rfield=[7,1,3,16,12,8,2,9,15,14,4,10,13,5,11,6], parent= self.root)
        self.level10 = QuestionHideSidebar(id="level10", menue=self.goto_level10, pos=(1920,0), size=(self.size_root), question="Welcher Studiengang der UdS ist fuer das Mediale Design<br/>der Skulptur-Basis mitverantwortlich?", answers=["Medieninformatik", "Informatik", "Mediengestaltung","Media Art und Design"], solution="a1" , pics= ["pics/medieninfo.jpg", "pics/uni.jpg", "pics/uni-bib.jpg"], infotext="Die Medieninformatik ist eine anwendungsorientierte Spezialisierung der klassischen Informatik und is gekennzeichnet durch eine interdisziplinaere Praegung.<br/>Inhaltlich umfasst das Studium relevante Grundlagenveranstaltungen aus dem Informatikstudium.<br/>Medienfachspezifische Inhalte werdenin speziellen Veranstaltungen vorgestellt und aktuelle Problemstellungen in praktischen Aufgaben von den Studierenden bearbeitet. Im Zuge der Vorlesung Ubiquitous Media wurde auch dieses Projekt erarbeitet.<br/>Dabei beschaeftigt sich der praktische Teil des Studiums mit der Entwicklung, dem Einsatz und den Auswirkungen von digitalen Medien um gesellschaftlichen Kontext. Es wird ein intensiver Einblick in den Umgang mit Multimediatechnologien wie Audio- und Bildverarbeitung, sowie deren Einsatzmoeglichkeiten und Auswirkungen anhand von praktischen Beispielen gegeben.<br/>Die Studierenden waehlen darueber hinaus eine Spezialisierungsfachrichtung - entweder Medienpsychologie oder Media Art und Design (in Zusammenarbeit mit der HBKSaar).", parent= self.root)
        self.level11 = SearchMistake(id="level11", menue=self.goto_level11, pos=(1920,0), size=(self.size_root), orgpic="mistake/oil_org.jpg", fakepic="mistake/oil_fake.jpg", mPos=[(60,241),(260,174),(341,699),(341,399),(469,18)] , parent= self.root)
        self.level12 = SearchMistake(id="level12", menue=self.goto_level12, pos=(1920,0), size=(self.size_root), orgpic="mistake/sculpture_org.jpg", fakepic="mistake/sculpture_fake.jpg", mPos=[(258,261), (425,640), (517,698), (641,520)] , parent= self.root)
        self.level13 = Question(id="level13", menue=self.goto_level13, pos=(1920,0), size=(self.size_root), question="Welchen Beruf uebt Fred George nicht aus?", answers=["politischer Kuenstler", "Musiker", "Photograph","Pornoregisseur"], solution="a4" , pics= ["pics/fred_george4.jpg", "pics/fredundtoni.jpg", "pics/sps1.jpg"], infotext="In seiner 30-jaehrigen Karriere als ein Fotograf hat Fred George das trainierte Auge eines sozialen Voyeurs verwendet, um aussergewoehnliche Bilder fuer Werbeagenturen und architektonische Unternehmen, sowie in der Musik, Kunst und Mode zu schaffen. George kreierte Bilder fuer Kampagnen der Philharmonie von Los Angeles, fuer das Getty- Zentrum, das Metropolitan- Museum der Kunst, das Kunstinstitut fuer Chicago, das Clevelander Museum der Kunst, das Museum der Modernen Kunst (New York), das amerikanische Museum der Naturgeschichte und das Joyce- Theater. Korporative Kunden haben American Express, Cartier, IBM, ATandT, Chase Manhattan Bank, Philip Morris Corporate Contributions, Canon und Citicorp eingeschlossen.<br/><br/>Seine Arbeit ist in Europa und Amerika, einschliesslich Berlin, Amsterdam, Paris, New York, und Los Angeles gezeigt worden. Hauptausstellungen waren u.a. die Art Basel (2004), Art Miami (2005), Europaeischer Monat der Fotografie (Berlin, 2006) und eine internationale Show von Reise-Fotografie, die in der franzoesischen Botschaft in New York begann. Seine Fotos der Innenstadt New Yorks sind in mehreren privaten und oeffentlichen Sammlungen, und Bilder der Nachwirkungen von 9/11 sind in New Yorks Historischer Gesellschaft ausgestellt worden.<br/><br/>George schafft Kunstwerke in vielfachen Medien, drueckt seine Bedenken in Bezug auf Politik und Umwelt aus, indem er Meinungen ueber Krieg, Geschlecht und Religion aeussert und anzweifelt. Er kritisiert die Unfehlbarkeit etablierter Symbole. Der Ash Wednesday 9/11 , Jesus as a Suicide Bomber  und AK-47 Crucifix  sind eindrucksvolle Beispiele.", parent= self.root)   


        # all levels
        self.levels = [self.level1, self.level2, self.level3,  self.level4,  self.level5,  self.level6,  self.level7,  self.level8,  self.level9,  self.level10,  self.level11,  self.level12,  self.level13]
        # all menues
        self.menues=[self.goto_level1, self.goto_level2, self.goto_level3, self.goto_level4, self.goto_level5, self.goto_level6, self.goto_level7, self.goto_level8, self.goto_level9, self.goto_level10, self.goto_level11, self.goto_level12, self.goto_level13]
        
        # Overall Time
        # startet bei 1, da 0 % 60 = 0
        self.h = 1      # hours
        self.m = 1      # minutes
        self.s = 1      # seconds
        # Startbutton
        self.start = avg.WordsNode(text="press to start!",  pos=(300, 850), font="Arial Black", fontsize=30, parent=self.homescreen)
        self.start.setEventHandler(avg.CURSORUP, avg.MOUSE | avg.TOUCH, self.Starting)
        # information button
        self.info = avg.ImageNode(href="info.png", size=(40,35), pos=(80, 970), parent=self.homescreen)
        self.info.setEventHandler(avg.CURSORUP,  avg.MOUSE, self.showInfo)
        self.infoindex = 0
        self.infoindex2 = 0
        # restart
        self.restart = avg.WordsNode(text="neustarten |",  pos=(130, 970), font="Arial Black", fontsize=20, opacity=0, sensitive=False, parent=self.homescreen)
        self.restart.setEventHandler(avg.CURSORUP, avg.MOUSE | avg.TOUCH, self.reStarting)
        # Mitwirkende
        self.we = avg.WordsNode(text="Mitwirkende",  pos=(270, 970), font="Arial Black", fontsize=20, opacity=0, sensitive=False, parent=self.homescreen)
        self.we.setEventHandler(avg.CURSORUP, avg.MOUSE | avg.TOUCH, self.showWe)
        self.we_pic = avg.ImageNode(href="we.jpg", pos=(800,0), size=(1120,1080), opacity = 0, sensitive=False, parent= self.homescreen)
        
        # Button to target
        self.totarget = avg.WordsNode(text="zu den Koordinaten", pos=(250, 850), font="Arial Black", fontsize=30, opacity=0, sensitive=False, parent=self.homescreen)
        self.totarget.setEventHandler(avg.CURSORUP, avg.MOUSE | avg.TOUCH, self.gotoTarget)
        self.allSolved = False
        self.timerOn = False
        self.interval = self.player.setInterval(1000, self.isAllSolved)
        self.timer = None
        
        # blur FXNode
        """
        braucht zu viel Rechenleistung...und hat nicht zufreidenstellend funktioniert
        self.blur = avg.BlurFXNode()
        self.blur.setParam(10)
        self.background.setEffect(self.blur)
        """ 
        
    def Starting(self, event):
        # press Startbutton
        self.timerOn = True             # zeit wurde gestartet
        for m in self.menues:           # aktiviere das Menue
            #m.sensitive = True
            m.blinking()                 # blinken (Menue.blink())
        avg.fadeOut(self.start, 1000)    # Startbutton ausblenden
        self.start.sensitive = False     # Startbutton-Bereich "deaktivieren"
        self.timer = self.player.setInterval(1000, self.time)   # Zeitinterval starten


    def showInfo(self, event):
        # blendet neustarten und mitwirkende ein, (infoindex = 0) und aus (infoindex != 0)
        if self.infoindex == 0:
            avg.fadeIn(self.restart, 1000)
            self.restart.sensitive= True
            avg.fadeIn(self.we, 1000)
            self.we.sensitive = True
            self.infoindex = 1
        else:
            avg.fadeOut(self.restart, 800)
            self.restart.sensitive= False
            avg.fadeOut(self.we, 800)
            self.we.sensitive = False
            self.infoindex = 0
    
    def showWe(self, event):
        # blendet Mitwirkende ein/aus
        if self.infoindex2 == 0:
            avg.fadeIn(self.we_pic, 1000)
            self.infoindex2 = 1
            self.we.color = "bbbbbb"
        else:
            avg.fadeOut(self.we_pic, 1000)
            self.infoindex2 = 0
            self.we.color = "FFFFFF"
        
        
    def reStarting(self, event):
        if self.goto_level1.startanimOn == False:           # geht nur wenn das Blinken schon aufgehoert hat
            # restart the program
            for level in self.levels:
                level.reset()           # reset of every level
            for menue in self.menues:
                menue.reset()           # reset of ervery menue + sensitive = false
                menue.sensitive = False
            # deactivate the "to the coordinates"-button
            avg.fadeOut(self.totarget, 1000)
            self.totarget.sensitive = False
            avg.fadeIn(self.start, 1000)
            self.start.sensitive = True
            self.level1.qFalse = 0
            self.s = 1
            self.h = 1
            self.m = 1
            self.timerOn = False
            self.allSolved = False
            self.interval = self.player.setInterval(5000, self.isAllSolved)
            # infobutton ausbleden
            avg.fadeOut(self.restart, 800)
            avg.fadeOut(self.we, 800)
            # ausblenden von Mitwirkende, falls es eingeblendet wurde und dann neustart geklickt
            self.we_pic.opacity = 0
            self.infoindex2 = 0
            self.we.color = "FFFFFF"
        
    def isAllSolved(self):
        # is all solved?
        for level in self.levels:
            if level.solved:                            # solved field of every level
                self.allSolved = True 
            else:
                self.allSolved = False
                break
        if self.allSolved:
            # if all solved -> button to go to the coordinates
            self.fadeInTarget()
            self.player.clearInterval(self.interval)    # stop isSolved-interval
            self.player.clearInterval(self.timer)       # stop the time of the whole program
    
            
    
    def time(self):
        # time counter for the whole program
        if self.allSolved == False:
            if self.s % 60 == 0:
                self.m = self.m + 1
                self.s = 0
            if self.m % 60 == 0:
                self.h = self.h +1               
                self.m = 1
                self.s = 0
            else:
                self.s = self.s + 1
        else:
            self.player.clearInterval(self.timer)
        
    def OVTimeQFalse(self):
        # write down the time and the number of incorrectly answered questions to the coordinates-page
        i = 0
        for l in self.levels:
            i = i + l.qFalse
        self.qFalse.text = str(i) + " mal"
        self.oaTime.text = str(self.h -1 ) + ":" + str(self.m-1 ) + ":" + str(self.s-1) + " h"
    
    def fadeInTarget(self):
        # fade in button to go to the coordinates
        avg.fadeIn(self.totarget, 1000, 1)
        self.totarget.sensitive = True
            
    def gotoTarget(self, event):
        # slide homescreen out and coordinates-page in
        self.OVTimeQFalse()
        # slide to targetscreen 
        avg.EaseInOutAnim(self.homescreen, "y", 1500, self.homescreen.pos.y, self.homescreen.pos.y + self.homescreen.size.y/2.4 , 50, 1000).start()
        # blednet Titel + Beschreibung aus
        avg.fadeOut(self.title_bgr_G, 1000)
        avg.fadeOut(self.title_bgr_M, 1000)
        avg.fadeOut(self.title_bgr_P, 1000)
        avg.fadeOut(self.title1, 1000)
        avg.fadeOut(self.title2, 1000)
        avg.fadeOut(self.title3, 1000)
        avg.fadeOut(self.descr, 1000)
        avg.fadeOut(self.description, 1000)
        avg.fadeOut(self.welc, 1000)
        avg.fadeOut(self.welcome, 1000).setStopCallback(self.koordDivIn)
        
        # wait 19min to reset program
        self.timetoreset = self.player.setTimeout(600000,self.reset)
        for m in self.menues:           # deaktiviert dass man auf die Level gelant, wenn man auf der Koordinaten-Seite ist
            m.sensitive = False
            m.reset()                   # resetet das Menu
    
    def koordDivIn(self):
        avg.fadeIn(self.end,1000)
     
    def reset(self):
        # restet the program (after 10min)
        for level in self.levels:
            level.reset()
        for menue in self.menues:
            menue.reset()               # nur zur Sicherheit, eig. schon bei gotoTarget()
            menue.sensitive = False
        # slide to startScreen
        avg.EaseInOutAnim(self.homescreen, "y", 1500, self.homescreen.pos.y, self.homescreen.pos.y -  self.homescreen.size.y/2.4 , 50, 1000).start()
        # blendet alles wieder ein
        avg.fadeIn(self.title_bgr_G, 1000)
        avg.fadeIn(self.title_bgr_M, 1000)
        avg.fadeIn(self.title_bgr_P, 1000)
        avg.fadeIn(self.title1, 1000)
        avg.fadeIn(self.title2, 1000)
        avg.fadeIn(self.title3, 1000)
        avg.fadeIn(self.descr, 1000)
        avg.fadeIn(self.description, 1000)
        avg.fadeIn(self.welc, 1000)
        avg.fadeIn(self.welcome, 1000)
        avg.fadeOut(self.end,1000)
        # deactivate the "to the coordinates"-button
        avg.fadeOut(self.totarget, 1000)
        self.totarget.sensitive = False
        avg.fadeIn(self.start, 1000)
        self.start.sensitive = True
        self.s = 1
        self.h = 1
        self.m = 1
        self.timerOn = False
        self.allSolved = False
        self.interval = self.player.setInterval(5000, self.isAllSolved)
        # infobutton ausbleden
        avg.fadeOut(self.restart, 800)
        avg.fadeOut(self.we, 800)
        self.infoindex = 0
        # ausblenden von Mitwirkende, falls es eingeblendet wurde und nicht mehr ausgeblendet
        self.we_pic.opacity = 0
        self.infoindex2 = 0
        self.we.color = "FFFFFF"


# start all        
if __name__ == '__main__':
    Main.start(resolution=(1920, 1080))
    