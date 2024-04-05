from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=2)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screenp

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class RenaOpening(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        welcome = Text("Hello World!", font_size=100,color=WHITE)

        self.play(Write(welcome),runtime=1)
        self.play(FadeOut(welcome),Create(circle),runtime=1)

        square = Square(color=RED).set_fill(BLACK, opacity=0)
        square.rotate(PI / 4)

        self.play(Transform(circle, square),runtime=1)
        
        text = Text("東郷レナ Vtuber", font_size=100,color=WHITE)
        self.play(square.animate.set_fill(RED, opacity=0.6))
        self.remove(circle)
        self.play(ReplacementTransform(square, text),runtime=1)
        self.wait(2)

class TestOp(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))