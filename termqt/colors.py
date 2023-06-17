from Qt.QtGui import QColor

# This file stores all xterm-256 colors.
# See https://jonasjacek.github.io/colors/


colors8 = {
    # follows xterm standard
    30: QColor(0, 0, 0),         # Black
    31: QColor(205, 0, 0),       # Red
    32: QColor(0, 205, 0),       # Green
    33: QColor(205, 205, 0),     # Yellow
    34: QColor(0, 0, 238),       # Blue
    35: QColor(205, 0, 205),     # Magenta
    36: QColor(0, 205, 205),     # Cyan
    37: QColor(229, 229, 229)    # White
}


colors16 = {
    30: QColor(127, 127, 127),   # Bright Black
    31: QColor(255, 0, 0),       # Bright Red
    32: QColor(0, 255, 0),       # Bright Green
    33: QColor(255, 255, 0),     # Bright Yellow
    34: QColor(92, 92, 255),      # Bright Blue
    35: QColor(255, 0, 255),     # Magenta
    36: QColor(0, 255, 255),     # Bright Cyan
    37: QColor(255, 255, 255)    # Bright White
}


colors256 = [
    QColor(0, 0, 0),          # 0, Black
    QColor(128, 0, 0),        # 1, Maroon
    QColor(0, 128, 0),        # 2, Green
    QColor(128, 128, 0),      # 3, Olive
    QColor(0, 0, 128),        # 4, Navy
    QColor(128, 0, 128),      # 5, Purple
    QColor(0, 128, 128),      # 6, Teal
    QColor(192, 192, 192),    # 7, Silver
    QColor(128, 128, 128),    # 8, Grey
    QColor(255, 0, 0),        # 9, Red
    QColor(0, 255, 0),        # 10, Lime
    QColor(255, 255, 0),      # 11, Yellow
    QColor(0, 0, 255),        # 12, Blue
    QColor(255, 0, 255),      # 13, Fuchsia
    QColor(0, 255, 255),      # 14, Aqua
    QColor(255, 255, 255),    # 15, White
    QColor(0, 0, 0),          # 16, Grey0
    QColor(0, 0, 95),         # 17, NavyBlue
    QColor(0, 0, 135),        # 18, DarkBlue
    QColor(0, 0, 175),        # 19, Blue3
    QColor(0, 0, 215),        # 20, Blue3
    QColor(0, 0, 255),        # 21, Blue1
    QColor(0, 95, 0),         # 22, DarkGreen
    QColor(0, 95, 95),        # 23, DeepSkyBlue4
    QColor(0, 95, 135),       # 24, DeepSkyBlue4
    QColor(0, 95, 175),       # 25, DeepSkyBlue4
    QColor(0, 95, 215),       # 26, DodgerBlue3
    QColor(0, 95, 255),       # 27, DodgerBlue2
    QColor(0, 135, 0),        # 28, Green4
    QColor(0, 135, 95),       # 29, SpringGreen4
    QColor(0, 135, 135),      # 30, Turquoise4
    QColor(0, 135, 175),      # 31, DeepSkyBlue3
    QColor(0, 135, 215),      # 32, DeepSkyBlue3
    QColor(0, 135, 255),      # 33, DodgerBlue1
    QColor(0, 175, 0),        # 34, Green3
    QColor(0, 175, 95),       # 35, SpringGreen3
    QColor(0, 175, 135),      # 36, DarkCyan
    QColor(0, 175, 175),      # 37, LightSeaGreen
    QColor(0, 175, 215),      # 38, DeepSkyBlue2
    QColor(0, 175, 255),      # 39, DeepSkyBlue1
    QColor(0, 215, 0),        # 40, Green3
    QColor(0, 215, 95),       # 41, SpringGreen3
    QColor(0, 215, 135),      # 42, SpringGreen2
    QColor(0, 215, 175),      # 43, Cyan3
    QColor(0, 215, 215),      # 44, DarkTurquoise
    QColor(0, 215, 255),      # 45, Turquoise2
    QColor(0, 255, 0),        # 46, Green1
    QColor(0, 255, 95),       # 47, SpringGreen2
    QColor(0, 255, 135),      # 48, SpringGreen1
    QColor(0, 255, 175),      # 49, MediumSpringGreen
    QColor(0, 255, 215),      # 50, Cyan2
    QColor(0, 255, 255),      # 51, Cyan1
    QColor(95, 0, 0),         # 52, DarkRed
    QColor(95, 0, 95),        # 53, DeepPink4
    QColor(95, 0, 135),       # 54, Purple4
    QColor(95, 0, 175),       # 55, Purple4
    QColor(95, 0, 215),       # 56, Purple3
    QColor(95, 0, 255),       # 57, BlueViolet
    QColor(95, 95, 0),        # 58, Orange4
    QColor(95, 95, 95),       # 59, Grey37
    QColor(95, 95, 135),      # 60, MediumPurple4
    QColor(95, 95, 175),      # 61, SlateBlue3
    QColor(95, 95, 215),      # 62, SlateBlue3
    QColor(95, 95, 255),      # 63, RoyalBlue1
    QColor(95, 135, 0),       # 64, Chartreuse4
    QColor(95, 135, 95),      # 65, DarkSeaGreen4
    QColor(95, 135, 135),     # 66, PaleTurquoise4
    QColor(95, 135, 175),     # 67, SteelBlue
    QColor(95, 135, 215),     # 68, SteelBlue3
    QColor(95, 135, 255),     # 69, CornflowerBlue
    QColor(95, 175, 0),       # 70, Chartreuse3
    QColor(95, 175, 95),      # 71, DarkSeaGreen4
    QColor(95, 175, 135),     # 72, CadetBlue
    QColor(95, 175, 175),     # 73, CadetBlue
    QColor(95, 175, 215),     # 74, SkyBlue3
    QColor(95, 175, 255),     # 75, SteelBlue1
    QColor(95, 215, 0),       # 76, Chartreuse3
    QColor(95, 215, 95),      # 77, PaleGreen3
    QColor(95, 215, 135),     # 78, SeaGreen3
    QColor(95, 215, 175),     # 79, Aquamarine3
    QColor(95, 215, 215),     # 80, MediumTurquoise
    QColor(95, 215, 255),     # 81, SteelBlue1
    QColor(95, 255, 0),       # 82, Chartreuse2
    QColor(95, 255, 95),      # 83, SeaGreen2
    QColor(95, 255, 135),     # 84, SeaGreen1
    QColor(95, 255, 175),     # 85, SeaGreen1
    QColor(95, 255, 215),     # 86, Aquamarine1
    QColor(95, 255, 255),     # 87, DarkSlateGray2
    QColor(135, 0, 0),        # 88, DarkRed
    QColor(135, 0, 95),       # 89, DeepPink4
    QColor(135, 0, 135),      # 90, DarkMagenta
    QColor(135, 0, 175),      # 91, DarkMagenta
    QColor(135, 0, 215),      # 92, DarkViolet
    QColor(135, 0, 255),      # 93, Purple
    QColor(135, 95, 0),       # 94, Orange4
    QColor(135, 95, 95),      # 95, LightPink4
    QColor(135, 95, 135),     # 96, Plum4
    QColor(135, 95, 175),     # 97, MediumPurple3
    QColor(135, 95, 215),     # 98, MediumPurple3
    QColor(135, 95, 255),     # 99, SlateBlue1
    QColor(135, 135, 0),      # 100, Yellow4
    QColor(135, 135, 95),     # 101, Wheat4
    QColor(135, 135, 135),    # 102, Grey53
    QColor(135, 135, 175),    # 103, LightSlateGrey
    QColor(135, 135, 215),    # 104, MediumPurple
    QColor(135, 135, 255),    # 105, LightSlateBlue
    QColor(135, 175, 0),      # 106, Yellow4
    QColor(135, 175, 95),     # 107, DarkOliveGreen3
    QColor(135, 175, 135),    # 108, DarkSeaGreen
    QColor(135, 175, 175),    # 109, LightSkyBlue3
    QColor(135, 175, 215),    # 110, LightSkyBlue3
    QColor(135, 175, 255),    # 111, SkyBlue2
    QColor(135, 215, 0),      # 112, Chartreuse2
    QColor(135, 215, 95),     # 113, DarkOliveGreen3
    QColor(135, 215, 135),    # 114, PaleGreen3
    QColor(135, 215, 175),    # 115, DarkSeaGreen3
    QColor(135, 215, 215),    # 116, DarkSlateGray3
    QColor(135, 215, 255),    # 117, SkyBlue1
    QColor(135, 255, 0),      # 118, Chartreuse1
    QColor(135, 255, 95),     # 119, LightGreen
    QColor(135, 255, 135),    # 120, LightGreen
    QColor(135, 255, 175),    # 121, PaleGreen1
    QColor(135, 255, 215),    # 122, Aquamarine1
    QColor(135, 255, 255),    # 123, DarkSlateGray1
    QColor(175, 0, 0),        # 124, Red3
    QColor(175, 0, 95),       # 125, DeepPink4
    QColor(175, 0, 135),      # 126, MediumVioletRed
    QColor(175, 0, 175),      # 127, Magenta3
    QColor(175, 0, 215),      # 128, DarkViolet
    QColor(175, 0, 255),      # 129, Purple
    QColor(175, 95, 0),       # 130, DarkOrange3
    QColor(175, 95, 95),      # 131, IndianRed
    QColor(175, 95, 135),     # 132, HotPink3
    QColor(175, 95, 175),     # 133, MediumOrchid3
    QColor(175, 95, 215),     # 134, MediumOrchid
    QColor(175, 95, 255),     # 135, MediumPurple2
    QColor(175, 135, 0),      # 136, DarkGoldenrod
    QColor(175, 135, 95),     # 137, LightSalmon3
    QColor(175, 135, 135),    # 138, RosyBrown
    QColor(175, 135, 175),    # 139, Grey63
    QColor(175, 135, 215),    # 140, MediumPurple2
    QColor(175, 135, 255),    # 141, MediumPurple1
    QColor(175, 175, 0),      # 142, Gold3
    QColor(175, 175, 95),     # 143, DarkKhaki
    QColor(175, 175, 135),    # 144, NavajoWhite3
    QColor(175, 175, 175),    # 145, Grey69
    QColor(175, 175, 215),    # 146, LightSteelBlue3
    QColor(175, 175, 255),    # 147, LightSteelBlue
    QColor(175, 215, 0),      # 148, Yellow3
    QColor(175, 215, 95),     # 149, DarkOliveGreen3
    QColor(175, 215, 135),    # 150, DarkSeaGreen3
    QColor(175, 215, 175),    # 151, DarkSeaGreen2
    QColor(175, 215, 215),    # 152, LightCyan3
    QColor(175, 215, 255),    # 153, LightSkyBlue1
    QColor(175, 255, 0),      # 154, GreenYellow
    QColor(175, 255, 95),     # 155, DarkOliveGreen2
    QColor(175, 255, 135),    # 156, PaleGreen1
    QColor(175, 255, 175),    # 157, DarkSeaGreen2
    QColor(175, 255, 215),    # 158, DarkSeaGreen1
    QColor(175, 255, 255),    # 159, PaleTurquoise1
    QColor(215, 0, 0),        # 160, Red3
    QColor(215, 0, 95),       # 161, DeepPink3
    QColor(215, 0, 135),      # 162, DeepPink3
    QColor(215, 0, 175),      # 163, Magenta3
    QColor(215, 0, 215),      # 164, Magenta3
    QColor(215, 0, 255),      # 165, Magenta2
    QColor(215, 95, 0),       # 166, DarkOrange3
    QColor(215, 95, 95),      # 167, IndianRed
    QColor(215, 95, 135),     # 168, HotPink3
    QColor(215, 95, 175),     # 169, HotPink2
    QColor(215, 95, 215),     # 170, Orchid
    QColor(215, 95, 255),     # 171, MediumOrchid1
    QColor(215, 135, 0),      # 172, Orange3
    QColor(215, 135, 95),     # 173, LightSalmon3
    QColor(215, 135, 135),    # 174, LightPink3
    QColor(215, 135, 175),    # 175, Pink3
    QColor(215, 135, 215),    # 176, Plum3
    QColor(215, 135, 255),    # 177, Violet
    QColor(215, 175, 0),      # 178, Gold3
    QColor(215, 175, 95),     # 179, LightGoldenrod3
    QColor(215, 175, 135),    # 180, Tan
    QColor(215, 175, 175),    # 181, MistyRose3
    QColor(215, 175, 215),    # 182, Thistle3
    QColor(215, 175, 255),    # 183, Plum2
    QColor(215, 215, 0),      # 184, Yellow3
    QColor(215, 215, 95),     # 185, Khaki3
    QColor(215, 215, 135),    # 186, LightGoldenrod2
    QColor(215, 215, 175),    # 187, LightYellow3
    QColor(215, 215, 215),    # 188, Grey84
    QColor(215, 215, 255),    # 189, LightSteelBlue1
    QColor(215, 255, 0),      # 190, Yellow2
    QColor(215, 255, 95),     # 191, DarkOliveGreen1
    QColor(215, 255, 135),    # 192, DarkOliveGreen1
    QColor(215, 255, 175),    # 193, DarkSeaGreen1
    QColor(215, 255, 215),    # 194, Honeydew2
    QColor(215, 255, 255),    # 195, LightCyan1
    QColor(255, 0, 0),        # 196, Red1
    QColor(255, 0, 95),       # 197, DeepPink2
    QColor(255, 0, 135),      # 198, DeepPink1
    QColor(255, 0, 175),      # 199, DeepPink1
    QColor(255, 0, 215),      # 200, Magenta2
    QColor(255, 0, 255),      # 201, Magenta1
    QColor(255, 95, 0),       # 202, OrangeRed1
    QColor(255, 95, 95),      # 203, IndianRed1
    QColor(255, 95, 135),     # 204, IndianRed1
    QColor(255, 95, 175),     # 205, HotPink
    QColor(255, 95, 215),     # 206, HotPink
    QColor(255, 95, 255),     # 207, MediumOrchid1
    QColor(255, 135, 0),      # 208, DarkOrange
    QColor(255, 135, 95),     # 209, Salmon1
    QColor(255, 135, 135),    # 210, LightCoral
    QColor(255, 135, 175),    # 211, PaleVioletRed1
    QColor(255, 135, 215),    # 212, Orchid2
    QColor(255, 135, 255),    # 213, Orchid1
    QColor(255, 175, 0),      # 214, Orange1
    QColor(255, 175, 95),     # 215, SandyBrown
    QColor(255, 175, 135),    # 216, LightSalmon1
    QColor(255, 175, 175),    # 217, LightPink1
    QColor(255, 175, 215),    # 218, Pink1
    QColor(255, 175, 255),    # 219, Plum1
    QColor(255, 215, 0),      # 220, Gold1
    QColor(255, 215, 95),     # 221, LightGoldenrod2
    QColor(255, 215, 135),    # 222, LightGoldenrod2
    QColor(255, 215, 175),    # 223, NavajoWhite1
    QColor(255, 215, 215),    # 224, MistyRose1
    QColor(255, 215, 255),    # 225, Thistle1
    QColor(255, 255, 0),      # 226, Yellow1
    QColor(255, 255, 95),     # 227, LightGoldenrod1
    QColor(255, 255, 135),    # 228, Khaki1
    QColor(255, 255, 175),    # 229, Wheat1
    QColor(255, 255, 215),    # 230, Cornsilk1
    QColor(255, 255, 255),    # 231, Grey100
    QColor(8, 8, 8),          # 232, Grey3
    QColor(18, 18, 18),       # 233, Grey7
    QColor(28, 28, 28),       # 234, Grey11
    QColor(38, 38, 38),       # 235, Grey15
    QColor(48, 48, 48),       # 236, Grey19
    QColor(58, 58, 58),       # 237, Grey23
    QColor(68, 68, 68),       # 238, Grey27
    QColor(78, 78, 78),       # 239, Grey30
    QColor(88, 88, 88),       # 240, Grey35
    QColor(98, 98, 98),       # 241, Grey39
    QColor(108, 108, 108),    # 242, Grey42
    QColor(118, 118, 118),    # 243, Grey46
    QColor(128, 128, 128),    # 244, Grey50
    QColor(138, 138, 138),    # 245, Grey54
    QColor(148, 148, 148),    # 246, Grey58
    QColor(158, 158, 158),    # 247, Grey62
    QColor(168, 168, 168),    # 248, Grey66
    QColor(178, 178, 178),    # 249, Grey70
    QColor(188, 188, 188),    # 250, Grey74
    QColor(198, 198, 198),    # 251, Grey78
    QColor(208, 208, 208),    # 252, Grey82
    QColor(218, 218, 218),    # 253, Grey85
    QColor(228, 228, 228),    # 254, Grey89
    QColor(238, 238, 238)     # 255, Grey93
]
