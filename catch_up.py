from pygame import *

#создай окно игры
win = display.set_mode((700,500))
display.set_caption('Догони меня пивасик (версия для БУТУСОВЫХ)')

#задай фон сцены
background = transform.scale(image.load('картинка пиваса.jpg'),(700,500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load('pivasic.png'),(100,100))
sprite2 = transform.scale(image.load('sprite2.png'),(100,100))

clock = time.Clock()
FPS = 40
 
game = True

x1,y1 = 130, 100
x2,y2 = 300, 300


while game:
    # проверка нажатия на кнопку выход
    for e in event.get():
        if e.type == QUIT:
            game = False
    key_pressed = key.get_pressed()
    if key_pressed[K_UP] and y1>0:
        y1-= 5 
    if key_pressed[K_DOWN] and y1<400:
        y1+= 5
    if key_pressed[K_LEFT] and x1>0:
        x1-= 5 
    if key_pressed[K_RIGHT] and x1<600:
        x1+= 5
    if key_pressed[K_w] and y2>0:
        y2-= 5 
    if key_pressed[K_s] and y2<400:
        y2+= 5
    if key_pressed[K_a] and x2>0:
        x2-= 5 
    if key_pressed[K_d] and x2<600:
        x2+= 5
    # отображение фона
    win.blit(background,(0,0))
    win.blit(sprite1,(x1,y1))
    win.blit(sprite2,(x2,y2))
    # обновление окна игры
    display.update()
    clock.tick(FPS)




#обработай событие «клик по кнопке "Закрыть окно"»