(define-param dan 0.5)
(define-param dan1 -0.5)
(define-param d 0.5) ; the hole radius
(define-param d1 -0.5) ; the hole radius
(define-param pos (+ dan (/ d 2 )))
(define-param pos1 (+ dan1 (/ d1 2 )))
(set! geometry-lattice (make lattice (size (+ 14 (* 2 pos)) no-size no-size)
                         ))
(define-param kz 0) 
(set! k-points (list (vector3 0 0 kz)        
                     (vector3 0.5 0 kz)))       
(define-param k-interp 10)
(set! k-points (interpolate k-interp k-points))
(define-param eps 1) 
(set! default-material (make dielectric (epsilon eps)))

(set! geometry 
      (append
       (list 
        (make block (center pos) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center pos1 ) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 1 pos)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -1 pos1)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 2 pos)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -2 pos1)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 3 pos)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -3 pos1)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 4 pos)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -4 pos1)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 5 pos)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -5 pos1)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 6 pos)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -6 pos1)) (size d infinity infinity) (material (make dielectric (epsilon 12)))) 
        (make block (center (+ 7 pos)) (size d infinity infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -7 pos1)) (size d infinity infinity) (material (make dielectric (epsilon 12)))) )))
(set-param! resolution 32)
(set-param! num-bands 60)
(run-te        (output-at-kpoint (vector3 0.5 0 0)
                          fix-efield-phase output-efield-y output-hfield-z output-dpwr)); 
