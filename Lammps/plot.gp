set terminal png
set output 'plot.png'
set xlabel 'temperature (K)'
set ylabel 'volume (A^3)'
p 'average.dat' u 2:3 w l title 'Marks'
