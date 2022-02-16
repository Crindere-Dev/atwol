screen girll_hover:
    image "girll_hover.png"

screen boyl_hover:
    image "boyl_hover.png"

screen nbl_hover:
    image "nbl_hover.png"

screen gender:
    imagemap:
        ground "img buttons.png"

        hotspot (124, 57, 522, 886) hovered ShowTransient ("girll_hover") unhovered Hide("girll_hover") clicked Jump("girl")
        hotspot (674, 80, 520, 856)  hovered ShowTransient ("boyl_hover") unhovered Hide("boyl_hover") clicked Jump("boy")
        hotspot (1244, 70, 575, 917) hovered ShowTransient ("nbl_hover") unhovered Hide("nbl_hover") clicked Jump("nb")

        