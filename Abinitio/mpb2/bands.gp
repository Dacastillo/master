unset key
set yrange[0:0.8]
plot for [c=7:81] '1dim.dat' u 3:c w l lt rgb 'blue', for [d=7:456] 'ndef.dat' u 3:d w l lt rgb 'red', 0.21 w l lt rgb 'green', 0.46 w l lt rgb 'green'

