def on_button_pressed_a():
    global caret
    if caret > 0 and playing:
        led.unplot(caret + 1, 4)
        caret += -1
        led.plot(caret, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global caret
    if caret < 3 and playing:
        led.unplot(caret, 4)
        caret += 1
        led.plot(caret + 1, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global ball_x, ball_y, caret, ball_x_direction, ball_y_direction, playing, score
    for index in range(3):
        basic.show_number(3 - index)
        basic.pause(100)
    basic.clear_screen()
    ball_x = 2
    ball_y = 3
    caret = 2
    ball_x_direction = 1
    ball_y_direction = -1
    playing = 1
    score = 0
    led.plot(caret, 4)
    led.plot(caret + 1, 4)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

score = 0
ball_y_direction = 0
ball_x_direction = 0
ball_y = 0
ball_x = 0
caret = 0
playing = 0
serial.redirect_to_usb()
playing = 0
basic.show_icon(IconNames.ANGRY)

def on_forever():
    global ball_x, ball_y, ball_x_direction, ball_y_direction, score, playing
    if playing:
        led.plot(ball_x, ball_y)
        basic.pause(200)
        led.unplot(ball_x, ball_y)
        ball_x += ball_x_direction
        ball_y += ball_y_direction
        if ball_x < 1 or ball_x > 3:
            ball_x_direction = ball_x_direction * -1
            music.play_tone(698, music.beat(BeatFraction.QUARTER))
        if ball_y < 1:
            ball_y_direction = ball_y_direction * -1
            music.play_tone(698, music.beat(BeatFraction.QUARTER))
        else:
            if ball_y == 3:
                if ball_x == caret or ball_x == caret + 1:
                    score += 1
                    ball_y_direction = ball_y_direction * -1
                    music.play_tone(698, music.beat(BeatFraction.QUARTER))
                else:
                    playing = 0
                    basic.clear_screen()
                    basic.show_icon(IconNames.TORTOISE)
                    basic.pause(500)
                    basic.show_string("Score: " + str(score))
                    serial.write_line("Score: " + str(score))
                    basic.show_icon(IconNames.ANGRY)
basic.forever(on_forever)
