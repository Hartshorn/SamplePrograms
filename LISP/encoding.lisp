; run length encoding with lisp

(defun compress (x)
	(if (consp x)
		(compr (car x) 1 (cdr x))
		x))
		
(defun compr (elt n lst)
	(if (null lst)
		(list (n-elts elt n))
		(let ((next (car lst)))
			(if (eql next elt)
				(compr elt (+ n 1) (cdr lst))
				(cons (n-elts elt n) (compr next 1 (cdr lst)))))))

(defun n-elts (elt n)
	(if (> n 1)
		(list n elt)
		elt))

; Most of the work is done by the recursive compr. 
; This function takes three arguments: e l t , the 
; element we last saw; n, the number of times in a
; row we've seen it; and 1st, the part of the list 
; we've yet to examine. If there is nothing left to
; examine, we just call n - e l t s to get something 
; representing n e l t s . If the first element of 
; 1st is still e l t , we increment n and keep going.
; Otherwise we get a compressed list of what we've 
; seen so far, and cons that onto whatever compr returns 
; for the rest of the list.

(defun uncompress (lst)
	(if (null lst)
		nil
		(let ((elt (car lst))
			  (rest (uncompress (cdr lst))))
			(if (consp elt)
				(append (apply #'list-of elt)
						rest)
				(cons elt rest)))))

(defun list-of (n elt)
	(if (zerop n)
		nil
		(cons elt (list-of (- n 1) elt))))
		
		
; This function works recursively through the compressed list,
; copying atoms verbatim and expanding lists by calling l i s t - o f

