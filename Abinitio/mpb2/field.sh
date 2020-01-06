#!/bin/bash
#mkdir real
#mkdir imag
mpb 1dim.ctl
for band in b45 b46 b47 b48
do
   h5topng -c bluered 1dim-dpwr.k12.$band.te.h5
   h5topng -c bluered -d y.r 1dim-e.k12.$band.y.te.h5
   h5topng -c bluered -d z.r 1dim-h.k12.$band.z.te.h5
   mv 1dim-e.k12.$band.y.te.png real
   mv 1dim-h.k12.$band.z.te.png real
   h5topng -c bluered -d y.i 1dim-e.k12.$band.y.te.h5
   h5topng -c bluered -d z.i 1dim-h.k12.$band.z.te.h5
   mv 1dim-e.k12.$band.y.te.png imag
   mv 1dim-h.k12.$band.z.te.png imag
   h5topng -c bluered 1dim-epsilon.h5
done

mpb ndef.ctl
for band in b315 b316 b317 b318 b319 b320
do
   h5topng -c bluered ndef-dpwr.k12.$band.te.h5
   h5topng -c bluered -d y.r ndef-e.k12.$band.y.te.h5
   h5topng -c bluered -d z.r ndef-h.k12.$band.z.te.h5
   mv ndef-e.k12.$band.y.te.png real
   mv ndef-h.k12.$band.z.te.png real
   h5topng -c bluered -d y.i ndef-e.k12.$band.y.te.h5
   h5topng -c bluered -d z.i ndef-h.k12.$band.z.te.h5
   mv ndef-e.k12.$band.y.te.png imag
   mv ndef-h.k12.$band.z.te.png imag
   h5topng -c bluered ndef-epsilon.h5
done

rm *.h5
cd ..

