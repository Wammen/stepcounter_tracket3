def on_button_pressed_b():
    control.reset()
input.on_button_pressed(Button.B, on_button_pressed_b)

steps = 0
basic.show_number(0)
radio.set_group(90)

def on_forever():
    global steps
    radio.send_value("x", input.acceleration(Dimension.X))
    radio.send_value("y", input.acceleration(Dimension.Y))
    radio.send_value("z", input.acceleration(Dimension.Z))
    if input.acceleration(Dimension.STRENGTH) > 2100:
        steps += 1
        basic.show_number(steps)
basic.forever(on_forever)
