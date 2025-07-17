import svgwrite
dwg = svgwrite.Drawing('result.svg', size=('800px', '600px'), profile='tiny')
dwg.add(dwg.circle(center=(100, 100), r=50, fill='rgb(255,0,0)'))
dwg.save()