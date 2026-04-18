def hex_to_hsl(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    delta = max_color - min_color
    if max_color == min_color:
        h = 0
    elif max_color == r:
        h = (60 * ((g - b) / delta) + 360) % 360
    elif max_color == g:
        h = (60 * ((b - r) / delta) + 120) % 360
    else:
        h = (60 * ((r - g) / delta) + 240) % 360
    if max_color == 0:
        s = 0
    else:
        s = delta / max_color
    l = (max_color + min_color) / 2
    return f"hsl({h}, {s*100}%, {l*100}%)"

hex_colors = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"]
hsl_colors = list(map(hex_to_hsl, hex_colors))
print(hsl_colors)
