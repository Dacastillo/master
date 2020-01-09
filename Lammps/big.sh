#!/bin/bash
for potential in airebom bop comb rebo rebolj reboljtor rebotor tersoff
do
    mkdir $potential
    awk "/#script $potential/,/#fin script $potential/" scriptgen.sh > $potential/in.marks
    for numb in 5 10 15
        do
          cd $potential && mkdir num=$numb && cd .. 
          sed "s/region bulto block -5 5 -5 5 -5 5/region bulto block -$numb $numb -$numb $numb -$numb $numb/g" $potential/in.marks > $potential/num=$numb/in.marks
          for dist in 1.2 1.4 1.6 1.8
          do
            cd $potential/num=$numb && mkdir dist=$dist && cd .. && cd ..
            sed "s/lattice sc 1.84 /lattice sc $dist /g" $potential/num=$numb/in.marks > $potential/num=$numb/dist=$dist/in.marks
            for file in in.melting in.elastic coordination.py BNC.tersoff CCu_v2.bop.table CH.airebo CH.airebo-m ffield.comb3 lib.comb3  
            do
                cp $file $potential/num=$numb/dist=$dist/$file
            done
            cd $potential/num=$numb/dist=$dist
            for script in marks melting elastic
            do
                mpirun -np 4 /home/dcastillo/lammps-7Aug19/src/lmp_mpi -in in.$script > out.$script
            done
            python coordination.py
            cd .. && cd .. && cd ..
          done
        done
done
