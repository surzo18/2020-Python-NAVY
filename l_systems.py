import turtle


def apply_rule(prev, rule):
    new = ""
    for letter in prev:
        new += rule if letter == 'F' else letter
    return new


def draw_L_system(t, axiom, rule, iterations, angle):
    instructions = ""
    for i in range(iterations):
        instructions = apply_rule(axiom, rule)
        axiom = instructions

    stack = []

    for ins in instructions:
        if ins == 'F':
            t.forward(5)
        elif ins == 'B':
            t.backward(5)
        elif ins == '+':
            t.right(angle)
        elif ins == '-':
            t.left(angle)
        elif ins == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif ins == ']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.setposition(position)
            turtle.setheading(heading)
            turtle.pendown()


t = turtle.Turtle()
wn = turtle.Screen()
t.speed(9)
draw_L_system(t, "F", "F-F++F-F", 5, 60)
wn.exitonclick()

# 1.
# Axiom: F + F + F + F
# Rule: F -> F + F - F - FF + F + F - F
# Angle: 90°
#
# 2.
# Axiom: F + +F + +F
# Rule: F -> F + F - -F + F
# Angle: 60°
#
# 3.
# Axiom: F
# Rule: F -> F[+F]
# F[-F]
# F
# Angle: pi / 7
#
# 4.
# Axiom: F
# Rule: F -> FF + [+F - F - F] - [-F + F + F]
# Angle: pi / 8