import pyautogui as pag

pag.moveTo(10,10, duration=1.5)

pag.moveRel(20,0)

pag.moveRel(200,0, duration=2)
pag.position()
pag.click() #can also doubleClick, rightClick, middleClick

dragRel()
pag.dragTo()

pag.typewrite()