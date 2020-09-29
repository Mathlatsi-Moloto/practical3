import pyglet
from pyglet import text



window = pyglet.window.Window(1280,720)      
form_height = 720
form_width = 1280
image_height = 120
image_width = 160
picture_4x = (form_width/2) - (image_width/2)
picture_4y = (form_height/2) +50

previewLabel =pyglet.text.Label('Preview',font_name = 'Calibri',font_size = 36,x= 30,y=600)



image_10 = pyglet.image.load("background.jpg")
sprite_background = pyglet.sprite.Sprite(image_10,x=0,y=0)

image_11 = pyglet.image.load("images-1.jpg")
sprite_9 = pyglet.sprite.Sprite(image_11,x=30,y=350)



image_1 = pyglet.image.load("1.1.jpg")
sprite_1 = pyglet.sprite.Sprite(image_1,x=picture_4x,y=picture_4y + image_height+10)

image = pyglet.image.load("1.jpg")
sprite = pyglet.sprite.Sprite(image,x= picture_4x - image_width-10,y=sprite_1.y) #picture box is a sprite

image_2 = pyglet.image.load("3.jpg")
sprite_2 = pyglet.sprite.Sprite(image_2,x=picture_4x + image_width+10,y=sprite_1.y)

image_3 = pyglet.image.load("4.jpg")
sprite_3 = pyglet.sprite.Sprite(image_3,x=picture_4x - image_width-10,y=picture_4y)

image_4 = pyglet.image.load("5.jpg")
sprite_4 = pyglet.sprite.Sprite(image_4,x=(form_width/2) - (image_width/2),y=(form_height/2)+50)

image_5 = pyglet.image.load("6.jpg")
sprite_5 = pyglet.sprite.Sprite(image_5,x= picture_4x + image_width+10,y=picture_4y)

image_7 = pyglet.image.load("8.jpg")
sprite_7 = pyglet.sprite.Sprite(image_7,x=picture_4x,y=picture_4y-image_height-10)

image_6 = pyglet.image.load("7.jpg")
sprite_6 = pyglet.sprite.Sprite(image_6,x=picture_4x - image_width-10,y= sprite_7.y)

image_8 = pyglet.image.load("11.jpg")
sprite_8 = pyglet.sprite.Sprite(image_8,x=picture_4x + image_width+10,y= sprite_7.y)

f = open("intial_state.txt","r")
intial_State = eval(f.read())
f.close()
#goal_State = [390,540,560,540,730,540,390,410,560,410,730,410,390,280,560,280,730,280]

sprite.x = intial_State[0]
sprite.y = intial_State[1]
sprite_1.x = intial_State[2]
sprite_1.y = intial_State[3]
sprite_2.x = intial_State[4]
sprite_2.y = intial_State[5]
sprite_3.x = intial_State[6]
sprite_3.y = intial_State[7] 
sprite_4.x = intial_State[8]
sprite_4.y = intial_State[9]
sprite_5.x = intial_State[10]
sprite_5.y = intial_State[11]  
sprite_6.x = intial_State[12]
sprite_6.y = intial_State[13]
sprite_7.x = intial_State[14]
sprite_7.y = intial_State[15]
sprite_8.x = intial_State[16]
sprite_8.y = intial_State[17]

def check_solve():
     if(sprite.x != 390 and sprite.y !=540):
          print('false')
     elif(sprite_1.x !=560 and sprite_1.y != 540):
          print('false')
     elif(sprite_2.x !=730 and sprite_2.y != 540):
          print('false')
     elif(sprite_3.x !=390 and sprite_3.y != 410):
          print('false')
     elif(sprite_4.x !=560 and sprite_4.y != 410):
          print('false')
     elif(sprite_5.x !=730 and sprite_5.y != 410):
          print('false')
     elif(sprite_6.x !=390 and sprite_6.y != 280):
          print('false')
     elif(sprite_7.x !=560 and sprite_7.y != 280):
          print('false')
     elif(sprite_8.x != 730 and sprite_8.y != 280):
          print('false')
     else:
          print('Yayy you have won!') 
scoreLabel = pyglet.text.Label('Moves Made',font_name = 'Calibri',font_size = 36,x= 400,y=150)
sprite.moves = 0
def moves_made():
     sprite.moves = sprite.moves +1
     print (" Moves made " + str(sprite.moves))

     
def available_moves(move_available):
     if(sprite_8.x== 730 and sprite_8.y == 280):
        move_available = ['up','left']
     elif (sprite_8.x == 730 and sprite_8.y == 410):
        move_available = ['up','down','left']
     elif (sprite_8.x == 730 and sprite_8.y == 540):
        move_available = ['down','left']
     elif (sprite_8.x == 560 and sprite_8.y == 280):
        move_available = ['up','right','left']
     elif (sprite_8.x == 560 and sprite_8.y == 410):
        move_available = ['up','down','left','right']
     elif (sprite_8.x == 560 and sprite_8.y == 540):
        move_available = ['right','down','left']
     elif (sprite_8.x == 390 and sprite_8.y == 280):
        move_available = ['up','right']
     elif (sprite_8.x == 390 and sprite_8.y == 410):
        move_available = ['up','down','right']
     elif (sprite_8.x == 390 and sprite_8.y == 540):
        move_available = ['down','right']
     return move_available  


def available_moves_mouse(x,y,can_move):
     if(sprite_8.x== 730 and sprite_8.y ==280):
          if(x==560 and y==280) or (x ==730 and y ==410):
               can_move = True 
               moves_made()
               check_solve() 
     elif(sprite_8.x== 730 and sprite_8.y ==410):
          if (x==730 and y==540) or (x ==560 and y ==410) or(x==730 and y ==280):
               can_move = True
               moves_made()
               check_solve()
     elif(sprite_8.x== 730 and sprite_8.y ==540):
          if(x ==730 and y==410) or (x ==560 and y ==540):
               can_move = True
               moves_made()
               check_solve()
     elif(sprite_8.x == 560 and sprite_8.y ==280):
          if(x ==730 and y==280) or (x ==560 and y ==410) or (x ==390 and y ==280):
               can_move = True
               moves_made()
               check_solve()
     elif(sprite_8.x == 560 and sprite_8.y ==410):
          if(x== 390 and y==410) or (x == 560 and y==540) or (x==560 and y==280) or (x==730 and y== 410):
               can_move = True
               moves_made()
               check_solve()
     elif(sprite_8.x == 390 and sprite_8.y ==540):
          if(x== 560 and y==540) or (x == 390 and y==410):
               can_move = True
               moves_made()
               check_solve()
     elif(sprite_8.x == 390 and sprite_8.y ==280):
          if(x == 390 and y==410) or (x==560 and y==280) :
               can_move = True
               moves_made()
               check_solve()
     elif(sprite_8.x == 390 and sprite_8.y ==410):
          if(x== 390 and y==540) or (x == 560 and y==410) or (x == 390 and y==280):
               can_move = True
               moves_made()
               check_solve()
     elif(sprite_8.x == 560 and sprite_8.y ==540):
          if(x== 390 and y==540) or (x == 560 and y==410)or (x == 730 and y==540):
               can_move = True
               moves_made()
               check_solve()
     return can_move
@window.event
def on_mouse_press(x, y, button, modifiers):
    if x > sprite_5.x and x < (sprite_5.x + image_width) and y > sprite_5.y and y < (sprite_5.y + image_height):
        can_move = available_moves_mouse(sprite_5.x,sprite_5.y,False)
        if(can_move == True):
            x_Blank =sprite_8.x
            y_Blank=sprite_8.y
            sprite_8.x = sprite_5.x
            sprite_8.y = sprite_5.y
            sprite_5.x = x_Blank
            sprite_5.y = y_Blank
    elif x > sprite_2.x and x < (sprite_2.x + image_width) and y > sprite_2.y and y < (sprite_2.y + image_height):
        can_move = available_moves_mouse(sprite_2.x,sprite_2.y,False)
        if(can_move == True):
            x_Blank =sprite_8.x
            y_Blank=sprite_8.y
            sprite_8.x = sprite_2.x
            sprite_8.y = sprite_2.y
            sprite_2.x = x_Blank
            sprite_2.y = y_Blank
    elif x > sprite_3.x and x < (sprite_3.x + image_width) and y > sprite_3.y and y < (sprite_3.y + image_height):
        can_move = available_moves_mouse(sprite_3.x,sprite_3.y,False)
        if(can_move == True):
            x_Blank =sprite_8.x
            y_Blank=sprite_8.y
            sprite_8.x = sprite_3.x
            sprite_8.y = sprite_3.y
            sprite_3.x = x_Blank
            sprite_3.y = y_Blank
    elif x > sprite_4.x and x < (sprite_4.x + image_width) and y > sprite_4.y and y < (sprite_4.y + image_height):
        can_move = available_moves_mouse(sprite_4.x,sprite_4.y,False)
        if(can_move == True):
            x_Blank =sprite_8.x
            y_Blank=sprite_8.y
            sprite_8.x = sprite_4.x
            sprite_8.y = sprite_4.y
            sprite_4.x = x_Blank
            sprite_4.y = y_Blank
    elif x > sprite_6.x and x < (sprite_6.x + image_width) and y > sprite_6.y and y < (sprite_6.y + image_height):
        can_move = available_moves_mouse(sprite_6.x,sprite_6.y,False)
        if(can_move == True):
            x_Blank =sprite_8.x
            y_Blank=sprite_8.y
            sprite_8.x = sprite_6.x
            sprite_8.y = sprite_6.y
            sprite_6.x = x_Blank
            sprite_6.y = y_Blank
    elif x > sprite_7.x and x < (sprite_7.x + image_width) and y > sprite_7.y and y < (sprite_7.y + image_height):
        can_move = available_moves_mouse(sprite_7.x,sprite_7.y,False)
        if(can_move == True):
            x_Blank =sprite_8.x
            y_Blank=sprite_8.y
            sprite_8.x = sprite_7.x
            sprite_8.y = sprite_7.y
            sprite_7.x = x_Blank
            sprite_7.y = y_Blank
    elif x > sprite.x and x < (sprite.x + image_width) and y > sprite.y and y < (sprite.y + image_height):
        can_move = available_moves_mouse(sprite.x,sprite.y,False)
        if(can_move == True):
            x_Blank =sprite_8.x
            y_Blank=sprite_8.y
            sprite_8.x = sprite.x
            sprite_8.y = sprite.y
            sprite.x = x_Blank
            sprite.y = y_Blank
    elif x > sprite_1.x and x < (sprite_1.x + image_width) and y > sprite_1.y and y < (sprite_1.y + image_height):
        can_move = available_moves_mouse(sprite_1.x,sprite_1.y,False)
        if(can_move == True):
            x_Blank =sprite_8.x
            y_Blank=sprite_8.y
            sprite_8.x = sprite_1.x
            sprite_8.y = sprite_1.y
            sprite_1.x = x_Blank
            sprite_1.y = y_Blank
@window.event
def on_draw():
    window.clear()
    sprite_background.draw()
    sprite.draw()
    sprite_1.draw()
    sprite_2.draw()
    sprite_3.draw()
    sprite_4.draw()
    sprite_5.draw()
    sprite_6.draw()
    sprite_7.draw() 
    sprite_8.draw()
    sprite_9.draw()
    scoreLabel.draw()
    previewLabel.draw()
   
    
    print (' sprit 0 ' + str(sprite.x) + str( sprite.y))
    print (' sprit 1 ' + str(sprite_1.x) + str( sprite_1.y))
    print (' sprit 2 ' + str(sprite_2.x) + str( sprite_2.y))
    print (' sprit 3 ' + str(sprite_3.x) + str(sprite_3.y))
    print (' sprit 4 ' + str(sprite_4.x) + str(sprite_4.y))
    print (' sprit 5 ' + str(sprite_5.x) + str(sprite_5.y))
    print (' sprit 6 ' + str(sprite_6.x) + str(sprite_6.y))
    print (' sprit 7 ' + str(sprite_7.x) + str(sprite_7.y))
    print (' sprit 8 ' + str(sprite_8.x) + str(sprite_8.y))
        
          #position of pinter to detemine pointer compare x and y of boundarysprrite 
@window.event
def on_key_press(key,modifiers):
     move_available = []
     move_available = available_moves(move_available)

     if (key == pyglet.window.key.UP) and ('up' in move_available):
          new_x = sprite_8.x
          new_y = sprite_8.y + 130
          if(sprite.x == new_x and sprite.y == new_y):
               sprite.x = sprite_8.x
               sprite.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_1.x == new_x and sprite_1.y == new_y):
               sprite_1.x = sprite_8.x
               sprite_1.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_2.x == new_x and sprite_2.y == new_y):
               sprite_2.x = sprite_8.x
               sprite_2.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_3.x == new_x and sprite_3.y == new_y):
               sprite_3.x = sprite_8.x
               sprite_3.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_4.x == new_x and sprite_4.y == new_y):
               sprite_4.x = sprite_8.x
               sprite_4.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_5.x == new_x and sprite_5.y == new_y):
               sprite_5.x = sprite_8.x
               sprite_5.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_6.x == new_x and sprite_6.y == new_y):
               sprite_6.x = sprite_8.x
               sprite_6.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_7.x == new_x and sprite_7.y == new_y):
               sprite_7.x = sprite_8.x
               sprite_7.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
     elif (key == pyglet.window.key.DOWN) and ('down' in move_available):
          new_x = sprite_8.x
          new_y = sprite_8.y - 130
          if(sprite.x == new_x and sprite.y == new_y):
               sprite.x = sprite_8.x
               sprite.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_1.x == new_x and sprite_1.y == new_y):
               sprite_1.x = sprite_8.x
               sprite_1.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_2.x == new_x and sprite_2.y == new_y):
               sprite_2.x = sprite_8.x
               sprite_2.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_3.x == new_x and sprite_3.y == new_y):
               sprite_3.x = sprite_8.x
               sprite_3.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_4.x == new_x and sprite_4.y == new_y):
               sprite_4.x = sprite_8.x
               sprite_4.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_5.x == new_x and sprite_5.y == new_y):
               sprite_5.x = sprite_8.x
               sprite_5.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_6.x == new_x and sprite_6.y == new_y):
               sprite_6.x = sprite_8.x
               sprite_6.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_7.x == new_x and sprite_7.y == new_y):
               sprite_7.x = sprite_8.x
               sprite_7.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
     elif (key == pyglet.window.key.LEFT) and ('left' in move_available):
          new_x = sprite_8.x - 170
          new_y = sprite_8.y
          if(sprite.x == new_x and sprite.y == new_y):
               sprite.x = sprite_8.x
               sprite.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_1.x == new_x and sprite_1.y == new_y):
               sprite_1.x = sprite_8.x
               sprite_1.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_2.x == new_x and sprite_2.y == new_y):
               sprite_2.x = sprite_8.x
               sprite_2.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_3.x == new_x and sprite_3.y == new_y):
               sprite_3.x = sprite_8.x
               sprite_3.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_4.x == new_x and sprite_4.y == new_y):
               sprite_4.x = sprite_8.x
               sprite_4.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_5.x == new_x and sprite_5.y == new_y):
               sprite_5.x = sprite_8.x
               sprite_5.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_6.x == new_x and sprite_6.y == new_y):
               sprite_6.x = sprite_8.x
               sprite_6.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_7.x == new_x and sprite_7.y == new_y):
               sprite_7.x = sprite_8.x
               sprite_7.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
     elif (key == pyglet.window.key.RIGHT) and ('right' in move_available):
          new_x = sprite_8.x + 170
          new_y = sprite_8.y
          if(sprite.x == new_x and sprite.y == new_y):
               sprite.x = sprite_8.x
               sprite.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_1.x == new_x and sprite_1.y == new_y):
               sprite_1.x = sprite_8.x
               sprite_1.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_2.x == new_x and sprite_2.y == new_y):
               sprite_2.x = sprite_8.x
               sprite_2.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_3.x == new_x and sprite_3.y == new_y):
               sprite_3.x = sprite_8.x
               sprite_3.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_4.x == new_x and sprite_4.y == new_y):
               sprite_4.x = sprite_8.x
               sprite_4.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_5.x == new_x and sprite_5.y == new_y):
               sprite_5.x = sprite_8.x
               sprite_5.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_6.x == new_x and sprite_6.y == new_y):
               sprite_6.x = sprite_8.x
               sprite_6.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
          elif(sprite_7.x == new_x and sprite_7.y == new_y):
               sprite_7.x = sprite_8.x
               sprite_7.y = sprite_8.y
               sprite_8.x = new_x
               sprite_8.y = new_y
           
           
            
            


                

                
            
            
       
        

           
            
            


                

                
            
            
           
           
            
            


                

                
            
            
       
        

           
            
            


                

                
            
            
       
        

     #def available_moves():  # check location of empty block and give coordinates of movement it can mak
pyglet.app.run() # excexction
    

          

