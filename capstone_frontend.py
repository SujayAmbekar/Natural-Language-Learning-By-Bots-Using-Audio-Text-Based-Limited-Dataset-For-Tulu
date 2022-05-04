# capstone_frontend (pyStage, converted from Scratch 3)

from pystage.core import CoreSprite, CoreStage

stage = CoreStage()
stage.pystage_addbackdrop('backdrop1')
stage.pystage_makevariable('my variable')
stage.pystage_makevariable('English')
stage.pystage_makevariable('Tulu')
stage.data_showvariable("English")
stage.pystage_setmonitorposition("English", -235, 175)
stage.data_showvariable("Tulu")
stage.pystage_setmonitorposition("Tulu", 148, 174)
giga = stage.pystage_createsprite(None)
giga.motion_setx(-49)
giga.motion_sety(-27)
giga.looks_gotofrontback_back()
giga.looks_goforwardbackwardlayers_forward(1)
giga.pystage_addcostume('giga_a', center_x=72, center_y=96)
giga.pystage_addcostume('giga_b', center_x=72, center_y=96)
giga.pystage_addcostume('giga_c', center_x=73, center_y=96)
giga.pystage_addcostume('giga_d', center_x=73, center_y=96)
giga.pystage_addsound('pop')

def event_whenflagclicked_1(self):
    self.data_setvariableto("Tulu", "x")
    self.data_setvariableto("English", "x")
    self.looks_sayforsecs("Hello!", 2.0)
    self.control_stop_this()

giga.event_whenflagclicked(event_whenflagclicked_1)

def event_whenkeypressed_2(self):
    self.sensing_askandwait("Add a sentence in English.")
    self.data_setvariableto("English", self.sensing_answer())
    self.data_showvariable("English")
    "NO TRANSLATION: data_addtolist"
    self.sensing_askandwait("Add a sentence in Tulu.")
    self.data_setvariableto("Tulu", self.sensing_answer())
    self.data_showvariable("Tulu")
    "NO TRANSLATION: data_addtolist"

giga.event_whenkeypressed("space", event_whenkeypressed_2)

def event_whenflagclicked_3(self):
    self.looks_switchcostumeto("giga_c")
    self.control_wait(2.0)
    self.looks_switchcostumeto("giga_a")
    self.control_stop_this()

giga.event_whenflagclicked(event_whenflagclicked_3)

stage.pystage_play()
