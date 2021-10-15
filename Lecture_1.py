from manim import *


class Functions(Scene):
    def __init__(
            self,
            renderer=None,
            camera_class=Camera,
            always_update_mobjects=False,
            random_seed=None,
            skip_animations=False,
    ):
        super().__init__(renderer, camera_class, always_update_mobjects, random_seed, skip_animations)
        self.ellipse_2 = Ellipse(width=2.0, height=4.0, color=BLUE_D)
        self.ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)

    def construct(self):
        self.ellipse_group = Group(self.ellipse_1, self.ellipse_2).arrange(buff=1).to_edge(LEFT)

        set_A = []
        set_A.append(Tex("1").shift(UP))
        set_A.append(Tex("2"))
        set_A.append(Tex("3").shift(DOWN))
        set_A_text = Group(*set_A).move_to(self.ellipse_1.get_center())

        set_B = []
        set_B.append(Tex("1").shift(UP))
        set_B.append(Tex("0"))
        set_B_text = Group(*set_B).move_to(self.ellipse_2.get_center())

        arrows = []
        for i in range(3):
            arrows.append(Arrow(start=set_A[i], end=set_B[0], color=RED))

        self.play(FadeIn(self.ellipse_group),
                  FadeIn(set_A_text),
                  FadeIn(set_B_text))

        self.add(*arrows)
        text = Tex('Number of Functions from A to B').scale(0.7)
        text.to_corner(RIGHT + UP, buff=1)
        self.add(text)
        self.wait(1)
