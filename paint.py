# -*- coding: utf-8 -*- 

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import cv2

class VGPaint:
    def __init__(self):
        self.font_file = "font/font1.otf"
        self.font_size = 18
        self.font = ImageFont.truetype(self.font_file, self.font_size)

    def paint_picture(self, method = "display"):
        im = Image.open("comment_template.png")
        draw = ImageDraw.Draw(im)

        # origin text
        box_position = (70, 15)
        box_width = 550
        box_height = 150

        text = "介護は過酷労働。\
親族すら投げ出し施設に入れるんだから。 \
介護が世界で一番稼げる職業ならまだしも下から数えた方が早い低賃金職業でしょ。\
お金抜きになると、本当に介護という職業に覚悟と誇りと使命感があるから。\
それらがない人は絶対にやらない方がいい。\
いつしか殺意に変わり人の命を奪ってしまう。\
不幸しか生まれない。"

        self.paint_box(draw, box_position, box_width, box_height, "black")
        self.paint_textbox(draw, box_position, box_width, box_height, text, "black", self.font)
        
        if method == "display":

            im.show()
        elif method == "file":
            pass

    def paint_box(self, draw, position, width, height, color):
        xy = (position[0], position[1], position[0] + width, position[1] + height)
        draw.rectangle(xy, outline = color)

    def paint_textbox(self, draw, position, width, height, text, color, font):

        import textwrap

        lines = textwrap.fill(text, width = 30)

        draw.multiline_text(position, lines, color, font)





# import textwrap
# lines = textwrap.wrap(text, width=40)
# y_text = h
# for line in lines:
#     width, height = font.getsize(line)
#     draw.text(((w - width) / 2, y_text), line, font=font, fill=FOREGROUND)
#     y_text += height
