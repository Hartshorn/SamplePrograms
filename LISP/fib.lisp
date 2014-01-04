(defun fib (n)
	(if (eql n 0)
		0
		(if (or (eql n 1) (eql n 2))
			1
			(+ (fib (- n 1)) (fib (- n 2))))))

(defun fiblist (n)
	(if (eq n 0)
		nil
		(cons (fib n) (fiblist (- n 1)))))
		

		  