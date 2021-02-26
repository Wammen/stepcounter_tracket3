input.onButtonPressed(Button.B, function () {
    control.reset()
})
let steps = 0
basic.showNumber(0)
radio.setGroup(90)
basic.forever(function () {
    radio.sendValue("x", input.acceleration(Dimension.X))
    radio.sendValue("y", input.acceleration(Dimension.Y))
    radio.sendValue("z", input.acceleration(Dimension.Z))
    if (input.acceleration(Dimension.Strength) > 2100) {
        steps += 1
        basic.showNumber(steps)
    }
})
