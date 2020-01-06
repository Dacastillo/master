(define-param dan 0.5) ; Parámetros de separación de los bultos
(define-param dan1 -0.5)
(define-param d 0.5) ; the hole radius
(define-param d1 -0.5) ; the hole radius
(define-param pos (+ dan (/ d 2 )))
(define-param pos1 (+ dan1 (/ d1 2 )))
(set! geometry-lattice (make lattice (size (+ 18 (* 2 pos)) (+ 7 (* 2 pos)) no-size)
                         )) ; Tamaño de la caja
(set! default-material (make dielectric (epsilon 1))) ; Material por defecto: Aire
(set! geometry 
      (append
       (list 
        (make block (center pos) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center pos1 ) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 1 pos)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -1 pos1)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 2 pos)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -2 pos1)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 3 pos)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -3 pos1)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 4 pos)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -4 pos1)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 5 pos)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -5 pos1)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ 6 pos)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -6 pos1)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12)))) 
        (make block (center (+ 7 pos)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12))))
        (make block (center (+ -7 pos1)) (size d (+ 3 (* 2 pos)) infinity) (material (make dielectric (epsilon 12)))) ))) ; Arreglo de bultos para armar Bragg
(set! pml-layers (list (make pml (thickness 1.6))))
(begin
  (set! sources (list
	  (make source
	     (src (make gaussian-src (frequency 0.46) (fwidth 0.1)))
	     (component Ey) (center 0 0 0))))
  (run-sources+ 1000
		(at-beginning output-epsilon)
		(after-sources (harminv Ey (vector3 0 0 0) 0.46 0.1)))
  (run-until 1000 (at-every 100 output-dpwr output-efield-x output-efield-y output-efield-z output-hfield-x output-hfield-y output-hfield-z))      
)


