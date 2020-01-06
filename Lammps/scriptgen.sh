#script airebom
newton on 
units metal 
dimension 3 
boundary p p p 
atom_style charge 
restart 10000 restart_file 
lattice sc 1.84 
region bulto block -5 5 -5 5 -5 5 
create_box 1 bulto 
create_atoms 1 region bulto 
mass * 12.0107 
group C type 1 
neighbor 0.5 bin 
neigh_modify delay 5 every 1 
pair_style airebo/morse 3.0
pair_coeff * * CH.airebo-m C
comm_modify cutoff 12.0
variable p_now equal press/1.e6 
thermo 10 
variable etotalatom equal etotal/atoms 
compute msd all msd 
compute Stress all stress/atom NULL virial 
compute pe all pe/atom 
compute ke all ke/atom 
thermo_style custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now 
dump mydump all xyz 100 dump.xyz 
dump_modify mydump element C  first yes 
dump mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  q
dump_modify mydump2 element C first yes
timestep 0.001 
velocity all create 5000.0 4193182 rot yes mom yes dist gaussian
fix nve all nve
fix vel_scale all temp/rescale 1 5000 5000 500 1.0
run 1000
unfix nve
unfix vel_scale
variable t_now equal time
variable t0 equal ${t_now} 
variable Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix nve all nve
fix vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run 500 
unfix nve
unfix vel_scale
fix nve all nve
fix vel_scale all temp/rescale 1 300 300 20 1.0
run 1000 
write_data marks_airebom.out
#fin script airebom
#script bop
newton on 
units metal 
dimension 3 
boundary p p p 
atom_style charge 
restart 10000 restart_file 
lattice sc 1.84 
region bulto block -5 5 -5 5 -5 5 
create_box 1 bulto 
create_atoms 1 region bulto
mass * 12.0107 
group C type 1 
neighbor 0.5 bin
neigh_modify delay 5 every 1 
pair_style bop
pair_coeff * * CCu_v2.bop.table C
comm_modify cutoff 12.0
variable p_now equal press/1.e6 
thermo 10 
variable etotalatom equal etotal/atoms 
compute msd all msd
compute Stress all stress/atom NULL virial 
compute pe all pe/atom 
compute ke all ke/atom
thermo_style custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now 
dump mydump all xyz 100 dump.xyz 
dump_modify mydump element C  first yes 
dump mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  q
dump_modify mydump2 element C first yes
timestep 0.001  
velocity all create 5000.0 4193182 rot yes mom yes dist gaussian
fix nve all nve
fix vel_scale all temp/rescale 1 5000 5000 500 1.0
run 1000
unfix nve
unfix vel_scale
variable t_now equal time
variable t0 equal ${t_now} 
variable Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix nve all nve
fix vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run 500 
unfix nve
unfix vel_scale
fix nve all nve
fix vel_scale all temp/rescale 1 300 300 20 1.0
run 1000 
write_data marks_bop.out
#fin script bop
#script comb
newton on 
units metal 
dimension 3
boundary p p p 
atom_style charge 
restart 10000 restart_file 
lattice sc 1.84 
region bulto block -5 5 -5 5 -5 5 
create_box 1 bulto 
create_atoms 1 region bulto
mass * 12.0107 
group C type 1 
neighbor 0.5 bin
neigh_modify delay 5 every 1 
pair_style comb3 polar_off
pair_coeff * * ffield.comb3 C 
comm_modify cutoff 12.0
variable p_now equal press/1.e6 
thermo 10 
variable etotalatom equal etotal/atoms 
compute msd all msd 
compute Stress all stress/atom NULL virial 
compute pe all pe/atom 
compute ke all ke/atom 
thermo_style custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now
dump mydump all xyz 100 dump.xyz
dump_modify mydump element C  first yes
dump mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  q
dump_modify mydump2 element C first yes
timestep 0.001 
velocity all create 5000.0 4193182 rot yes mom yes dist gaussian
fix nve all nve
fix vel_scale all temp/rescale 1 5000 5000 500 1.0
run 1000
unfix nve
unfix vel_scale
variable t_now equal time
variable t0 equal ${t_now} 
variable Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix nve all nve
fix vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run 500 
unfix nve
unfix vel_scale
fix nve all nve
fix vel_scale all temp/rescale 1 300 300 20 1.0
run 1000 
write_data marks_comb.out
#fin script comb
#script reax
newton on 
units metal 
dimension 3 
boundary p p p 
atom_style charge 
restart 10000 restart_file 
lattice sc 1.84 
region bulto block -5 5 -5 5 -5 5 
create_box 1 bulto 
create_atoms 1 region bulto 
mass * 12.0107 
group C type 1 
neighbor 0.5 bin 
neigh_modify delay 5 every 1 
pair_style reax/c NULL
pair_coeff * * ffield.reax C    
fix 1 all qeq/reax 1 0.0 10.0 1.0e-6 reax/c
comm_modify cutoff 12.0
variable p_now equal press/1.e6 
thermo 10 
variable etotalatom equal etotal/atoms 
compute msd all msd 
compute Stress all stress/atom NULL virial 
compute pe all pe/atom 
compute ke all ke/atom 
thermo_style custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now 
dump mydump all xyz 100 dump.xyz 
dump_modify mydump element C  first yes
dump mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  q
dump_modify mydump2 element C first yes
timestep 0.001 
velocity all create 5000.0 4193182 rot yes mom yes dist gaussian
fix nve all nve
fix vel_scale all temp/rescale 1 5000 5000 500 1.0
run 1000 
unfix nve
unfix vel_scale
variable t_now equal time
variable t0 equal ${t_now} 
variable Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix nve all nve
fix vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run 500 
unfix nve
unfix vel_scale
fix nve all nve
fix vel_scale all temp/rescale 1 300 300 20 1.0
run 1000 
write_data marks_reax.out
#fin script reax
#script edip
units           metal
dimension       3
boundary        p p p
atom_style      atomic
restart         10000 restart_file
lattice 	sc 2.152
region		bulto block -4 4 -4 4 -4 4
create_box      1 bulto
create_atoms	1 region bulto
mass		* 12.0107  
group           C type 1
neighbor	    0.5 bin
neigh_modify	    delay 5 every 1
pair_style cedip
pair_coeff * * C
variable        p_now equal press/1.e6
thermo          10
variable        etotalatom equal etotal/atoms
compute         msd all msd
compute         Stress all stress/atom NULL virial
compute         pe all pe/atom
compute         ke all ke/atom
thermo_style    custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now
dump            mydump all xyz 100 dump.xyz
dump_modify     mydump element C  first yes
dump            mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  
dump_modify     mydump2 element C first yes
timestep        0.001 
velocity        all create 5000.0 4193182 rot yes mom yes dist gaussian
fix             nve all nve
fix             vel_scale all temp/rescale 1 5000 5000 500 1.0
run             1000
unfix           nve
unfix           vel_scale
variable       t_now equal time
variable       t0  equal ${t_now} 
variable       Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix            nve all nve
fix            vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run            500 
unfix          nve
unfix          vel_scale
fix            nve all nve
fix            vel_scale all temp/rescale 1 300 300 20 1.0
run             1000 
write_data      marks_edip.out
#fin script edip
#script rebo
newton on 
units metal 
dimension 3 
boundary p p p 
atom_style charge 
restart 10000 restart_file 
lattice sc 1.84 
region bulto block -5 5 -5 5 -5 5 
create_box 1 bulto 
create_atoms 1 region bulto 
mass * 12.0107 
group C type 1 
neighbor 0.5 bin 
neigh_modify delay 5 every 1
pair_style rebo
pair_coeff * * CH.airebo C
comm_modify cutoff 12.0
variable p_now equal press/1.e6 
thermo 10 
variable etotalatom equal etotal/atoms 
compute msd all msd 
compute Stress all stress/atom NULL virial 
compute pe all pe/atom 
compute ke all ke/atom 
thermo_style custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now 
dump mydump all xyz 100 dump.xyz 
dump_modify mydump element C  first yes 
dump mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  q
dump_modify mydump2 element C first yes
timestep 0.001
velocity all create 5000.0 4193182 rot yes mom yes dist gaussian
fix nve all nve
fix vel_scale all temp/rescale 1 5000 5000 500 1.0
run 1000 
unfix nve
unfix vel_scale
variable t_now equal time
variable t0 equal ${t_now} 
variable Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix nve all nve
fix vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run 500 
unfix nve
unfix vel_scale
fix nve all nve
fix vel_scale all temp/rescale 1 300 300 20 1.0
run 1000 
write_data marks_rebo.out
#fin script rebolj
#script rebolj
newton on 
units metal 
dimension 3 
boundary p p p 
atom_style charge 
restart 10000 restart_file 
lattice sc 1.84 
region bulto block -5 5 -5 5 -5 5 
create_box 1 bulto 
create_atoms 1 region bulto 
mass * 12.0107 
group C type 1 
neighbor 0.5 bin 
neigh_modify delay 5 every 1 
pair_style airebo 2.5 0 1
pair_coeff * * CH.airebo C 
comm_modify cutoff 12.0
variable p_now equal press/1.e6 
thermo 10
variable etotalatom equal etotal/atoms 
compute msd all msd 
compute Stress all stress/atom NULL virial 
compute pe all pe/atom 
compute ke all ke/atom 
thermo_style custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now 
dump mydump all xyz 100 dump.xyz 
dump_modify mydump element C  first yes 
dump mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  q
dump_modify mydump2 element C first yes
timestep 0.001  
velocity all create 5000.0 4193182 rot yes mom yes dist gaussian
fix nve all nve
fix vel_scale all temp/rescale 1 5000 5000 500 1.0
run 1000 
unfix nve
unfix vel_scale
variable t_now equal time
variable t0 equal ${t_now} 
variable Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix nve all nve
fix vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run 500
unfix nve
unfix vel_scale
fix nve all nve
fix vel_scale all temp/rescale 1 300 300 20 1.0
run 1000 
write_data marks_rebolj.out
#fin script rebolj
#script reboljtor
newton on 
units metal 
dimension 3 
boundary p p p 
atom_style charge 
restart 10000 restart_file 
lattice sc 1.84 
region bulto block -5 5 -5 5 -5 5 
create_box 1 bulto 
create_atoms 1 region bulto 
mass * 12.0107 
group C type 1 
neighbor 0.5 bin 
neigh_modify delay 5 every 1 
pair_style airebo 2.5 1 1
pair_coeff * * CH.airebo C 
comm_modify cutoff 12.0
variable p_now equal press/1.e6 
thermo 10 
variable etotalatom equal etotal/atoms 
compute msd all msd 
compute Stress all stress/atom NULL virial 
compute pe all pe/atom 
compute ke all ke/atom 
thermo_style custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now 
dump mydump all xyz 100 dump.xyz 
dump_modify mydump element C  first yes 
dump mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  q
dump_modify mydump2 element C first yes
timestep 0.001  
velocity all create 5000.0 4193182 rot yes mom yes dist gaussian
fix nve all nve
fix vel_scale all temp/rescale 1 5000 5000 500 1.0
run 1000 
unfix nve
unfix vel_scale
variable t_now equal time
variable t0 equal ${t_now} 
variable Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix nve all nve
fix vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run 500 
unfix nve
unfix vel_scale
fix nve all nve
fix vel_scale all temp/rescale 1 300 300 20 1.0
run 1000 
write_data marks_reboljtor.out
#fin script reboljtor
#script rebotor
newton on 
units metal 
dimension 3 
boundary p p p 
atom_style charge 
restart 10000 restart_file 
lattice sc 1.84 
region bulto block -5 5 -5 5 -5 5 
create_box 1 bulto 
create_atoms 1 region bulto 
mass * 12.0107 
group C type 1 
neighbor 0.5 bin 
neigh_modify delay 5 every 1 
pair_style airebo  2.5 1 0
pair_coeff * * CH.airebo C
comm_modify cutoff 12.0
variable p_now equal press/1.e6 
thermo 10 
variable etotalatom equal etotal/atoms 
compute msd all msd 
compute Stress all stress/atom NULL virial 
compute pe all pe/atom 
compute ke all ke/atom 
thermo_style custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now 
dump mydump all xyz 100 dump.xyz 
dump_modify mydump element C  first yes 
dump mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  q
dump_modify mydump2 element C first yes
timestep 0.001  
velocity all create 5000.0 4193182 rot yes mom yes dist gaussian
fix nve all nve
fix vel_scale all temp/rescale 1 5000 5000 500 1.0
run 1000
unfix nve
unfix vel_scale
variable t_now equal time
variable t0 equal ${t_now}
variable Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix nve all nve
fix vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run 500 
unfix nve
unfix vel_scale
fix nve all nve
fix vel_scale all temp/rescale 1 300 300 20 1.0
run 1000 
write_data marks_rebotor.out
#fin script rebotor
#script tersoff
newton on 
units metal 
dimension 3 
boundary p p p
atom_style charge
restart 10000 restart_file 
lattice sc 1.84 
region bulto block -5 5 -5 5 -5 5 
create_box 1 bulto 
create_atoms 1 region bulto
mass * 12.0107 
group C type 1 
neighbor 0.5 bin 
neigh_modify delay 5 every 1 
pair_style tersoff
pair_coeff * * BNC.tersoff C
comm_modify cutoff 12.0
variable p_now equal press/1.e6 
thermo 10 
variable etotalatom equal etotal/atoms 
compute msd all msd 
compute Stress all stress/atom NULL virial
compute pe all pe/atom
compute ke all ke/atom 
thermo_style custom step temp v_etotalatom ke pe etotal press pxx pyy pzz  vol lx ly lz c_msd[4] v_p_now 
dump mydump all xyz 100 dump.xyz 
dump_modify mydump element C  first yes 
dump mydump2 all custom 10 dump_custom.xyz id element x y z vx vy vz c_pe c_ke c_Stress[1] c_Stress[2] c_Stress[3]  q
dump_modify mydump2 element C first yes
timestep 0.001  
velocity all create 5000.0 4193182 rot yes mom yes dist gaussian
fix nve all nve
fix vel_scale all temp/rescale 1 5000 5000 500 1.0
run 1000 
unfix nve
unfix vel_scale
variable t_now equal time
variable t0 equal ${t_now} 
variable Temp_now equal 5000*exp(-5.63*(time-v_t0))
fix nve all nve
fix vel_scale all temp/rescale 1 v_Temp_now 300 20 1.0
run 500 
unfix nve
unfix vel_scale
fix nve all nve
fix vel_scale all temp/rescale 1 300 300 20 1.0
run 1000 
write_data marks_tersoff.out
#fin script tersoff


