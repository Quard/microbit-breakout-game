input.onButtonPressed(Button.A, function () {
    if (caret > 0 && playing) {
        led.unplot(caret + 1, 4)
        caret += -1
        led.plot(caret, 4)
    }
})
input.onButtonPressed(Button.B, function () {
    if (caret < 3 && playing) {
        led.unplot(caret, 4)
        caret += 1
        led.plot(caret + 1, 4)
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    for (let index = 0; index <= 2; index++) {
        basic.showNumber(3 - index)
        basic.pause(100)
    }
    basic.clearScreen()
    ball_x = 2
    ball_y = 3
    caret = 2
    ball_x_direction = 1
    ball_y_direction = -1
    playing = 1
    score = 0
    led.plot(caret, 4)
    led.plot(caret + 1, 4)
})
let score = 0
let ball_y_direction = 0
let ball_x_direction = 0
let ball_y = 0
let ball_x = 0
let caret = 0
let playing = 0
serial.redirectToUSB()
playing = 0
basic.showIcon(IconNames.Angry)
basic.forever(function () {
    if (playing) {
        led.plot(ball_x, ball_y)
        basic.pause(200)
        led.unplot(ball_x, ball_y)
        ball_x += ball_x_direction
        ball_y += ball_y_direction
        if (ball_x < 1 || ball_x > 3) {
            ball_x_direction = ball_x_direction * -1
            music.playTone(698, music.beat(BeatFraction.Quarter))
        }
        if (ball_y < 1) {
            ball_y_direction = ball_y_direction * -1
            music.playTone(698, music.beat(BeatFraction.Quarter))
        } else if (ball_y == 3) {
            if (ball_x == caret || ball_x == caret + 1) {
                score += 1
                ball_y_direction = ball_y_direction * -1
                music.playTone(698, music.beat(BeatFraction.Quarter))
            } else {
                playing = 0
                basic.clearScreen()
                basic.showIcon(IconNames.Tortoise)
                basic.pause(500)
                basic.showString("Score: " + ("" + score))
                serial.writeLine("Score: " + ("" + score))
                basic.showIcon(IconNames.Angry)
            }
        }
    }
})
