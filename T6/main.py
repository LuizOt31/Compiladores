import svgwrite

dwg = svgwrite.Drawing('output.svg', size=('800px', '600px'))

# Círculo
dwg.add(dwg.circle(center=(100, 100), r=50, fill='red'))

# Retângulo
dwg.add(dwg.rect(insert=(200, 150), size=(100, 80), fill='blue'))

# Linha
dwg.add(dwg.line(start=(50, 50), end=(300, 300), stroke='green'))

dwg.save()
