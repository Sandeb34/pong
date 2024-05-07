# from turtle import Turtle
#
# # Constant variables
# # Tweak variables here:
# STARTING_POSITIONS = [(350, -20), (350, 0), (350, 20), (350, 40), (350, 60)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
#
#
# # __init__(self): is used for attributes
# class Paddle:
#     # What will happen when we initialize a new snake object.
#     def __init__(self):
#         """Add Attributes for Snake class"""
#         # New ATTRIBUTES (has)
#         self.segments = []
#         self.create_paddle()
#
#     # METHOD because it does
#     def create_paddle(self):
#         """Creates a 3-segment snake"""
#         for position in STARTING_POSITIONS:
#             self.add_segment(position)
#
#     def add_segment(self, position):
#         new_segment = Turtle(shape="square")
#         new_segment.color("white")
#         new_segment.penup()
#         new_segment.goto(position)
#         self.segments.append(new_segment)
#
#     def move(self):
#         """Moves the segments of the snake each segment taking the coordinate
#         of the previous segment except segment 1st """
#         for seg_numb in range(len(self.segments) - 1, 0, -1):
#             new_y = self.segments[seg_numb - 1].ycor()
#
#     def up(self):
#         # If current heading pointed "down" cant move "up".
#         # Heading as method so use ( ) to check value with constant variables DOWN, UP, RIGHT, and LEFT.
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)
#
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)
#
