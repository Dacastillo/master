#!/bin/bash
#inicializar los distintos potenciales con sus respectivos script
for potential in airebom bop comb rebo rebolj reboljtor rebotor tersoff
do
    mkdir $potential
    awk "/#script $potential/,/#fin script $potential/" scriptgen.sh > $potential/in.marks
    for numb in 5 10 15
        do
          mkdir num=$numb
          sed "s/region bulto block -5 5 -5 5 -5 5/region bulto block -$numb $numb -$numb $numb -$numb $numb/g" $potential/in.marks > $potential/num=$numb/in.marks
          for dist in 1.2 1.4 1.6 1.8
          do
            mkdir dist=$dist
            sed "s/lattice sc 1.84 /lattice sc $dist /g" $potential/num=$numb/in.marks > $potential/num=$numb/dist=d/in.marks
            for file in in.melting in.elastic coordination.py BNC.tersoff CCu_v2.bop.table CH.airebo CH.airebo-m ffield.comb3 lib.comb3  
            do
                cp $file $potential/num=$numb/dist=$dist/$file
            done
            cd $potential/num=$numb/dist=$dist
            for script in marks melting elastic
            do
                mpirun -np 8 lmp_mpi -in in.$script > out.$script
            done
            python coordination.py
            mv log.lammps log.melting
            mv average.dat average_melting.dat 
          done
        done
done
