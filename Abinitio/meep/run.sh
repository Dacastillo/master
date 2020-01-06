#!/bin/bash
for freq in 0.21 0.46
do
#   mkdir freq=$freq
#   sed  's/0.2)/'$freq')/g' cav.ctl > freq=$freq/cav.ctl2
#   sed  's/ 0.2 / '$freq' /g' cav.ctl > freq=$freq/cav.ctl2
   cd freq=$freq
#   mv cav.ctl2 cav.ctl
   mpirun -np 8 meep cav.ctl > cav.out
   h5topng -c bluered *.h5
   grep harminv cav.out > cav.quf
   cd ..
done

