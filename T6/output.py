import svgwrite
dwg = svgwrite.Drawing('output.svg', size=('500px', '500px'), profile='tiny')
dwg.add(dwg.rect(insert=(0, 0), size=('10000px', '10000px'), fill='rgb(30,144,255)'))
dwg.add(dwg.circle(center=(420, 80), r=50, fill='rgb(255,215,0)'))
dwg.add(dwg.rect(insert=(150, 250), size=('200px', '200px'), fill='rgb(210,180,140)'))
dwg.add(dwg.line(start=(140, 260), end=(250, 180), stroke='rgb(139,69,19)'))
dwg.add(dwg.line(start=(250, 180), end=(360, 260), stroke='rgb(139,69,19)'))
dwg.add(dwg.rect(insert=(225, 350), size=('50px', '100px'), fill='rgb(110,70,20)'))
dwg.save()