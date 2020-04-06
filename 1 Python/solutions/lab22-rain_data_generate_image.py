
from PIL import Image



def clamp(v, low, high):
    return low if v < low else high if v > high else v

def get_color(v):
    if v == -1:
        return (0, 0, 64)
    v /= .6
    v *= 255
    v = clamp(v, 0, 255)
    v = int(v)
    return (v, v, v)

data = []
with open('../data/rain_output.csv', 'r') as f:
    contents = f.read()
    lines = contents.split('\n')
    lines.pop(0) # remove header
    for line in lines:
        if line == '':
            continue
        line = line.split(',')
        line.pop(0) # remove date
        data.append([float(v) if v != '' else -1 for v in line])



width = len(data[0])
height = len(data)
img = Image.new('RGB', (width, height))
pixels = img.load()
for j in range(height):
    for i in range(width):
        v = data[j][i]
        color = get_color(v)
        pixels[i, j] = color
        # if i > len(data[j]):
        #     pixels[i, j] = (0, 0, 0)
        # else:
        #     pixels[i, j] = get_color(data[j][i])


img = img.resize((8*width, 8*height))
img.show()

