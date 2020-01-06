#!/bin/bash
for dan in dan6 dan7 dan8
do
     for fold in mpb2 mpb3
     do
        cd $fold/$dan
        mpb ndef.ctl > ndef.out && grep tefreqs ndef.out > ndef.dat
        mpb ndef.ctl
        ./h5.sh
        rm *.h5
        cd ..
    done
done

