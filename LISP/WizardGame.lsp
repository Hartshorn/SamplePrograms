; wizard text adventure game

; global parameters
; each parameter starts with defparameter, then the parameter name with * (convention)
; and then the list of items starting with '.
; So '((1(a b))(2(c d))(3 (e f)))
; says make a long list
; containing three smaller lists
; which each contain a value and a list
; List 1 contains a and b . . . etc . . .
; all of this is held under the variable name
(defparameter *nodes* '((living-room (you are in the living-room.
							a wizard is snoring loudly on the couch.))
						(garden (you are in a beautiful garden.
							there is a well in front of you.))
						(attic (you are in the attic.
							there is a giant welding torch in the corner.))))
							
(defparameter *edges* '((living-room (garden west door)
									(attic upstairs ladder))
						(garden (living-room east door))
						(attic (living-room downstairs ladder))))

(defparameter *object-locations* '((whiskey living-room)
									(bucket living-room)
									(chain garden)
									(frog garden)))

(defparameter *objects* '(whiskey bucket frog chain))

(defparameter *location* 'living-room)

(defparameter *allowed-commands* '(look walk pickup inventory))

(defparameter *max-label-length* 30)

; function definitions
; each function begins with defun, and then the function name
; right after that are the parameters it takes
; followed by what the function does when executed.
; so the first one here:
; begins with defun
; is called describe-location
; and takes two parameters, a location and the nodes list
; what this function does is return the cadr (or second value)
; of the list generated by the assoc function (which takes two
; parameters, and we pass into it a location and the nodes list)
; assoc will search the nodes list for our provided location,
; and return the full list it finds from nodes. cadr will then
; cut out the second value in that list
; so when we say (describe-location 'living-room *nodes*)
; assoc searches *nodes* for living-room
; when it finds it, it returns the who list entry for living-room
; cadr then cuts out the second value (which is a list with two values)
(defun describe-location (location nodes)
	(cadr (assoc location nodes)))
; describe-path takes one parameter and
; it returns a sentence with two data pulls in it
; the first is the third entry in the parameter
; the second is the second entry in the parameter,
; both incorporated into a sentence using quasi-quoting (`)
; we pass into this function a list, not a variable name
; so, for example, (describe-path 'nodes) will not work
; but, (describe-path '(garden west door)) will
(defun describe-path (edge)
	`(there is a ,(caddr edge) going ,(cadr edge) from here.))
; the first part of the inside of the function
; (assoc location edges)
; does the same as the last function: it searches for the given location
; in the given edges list. it returns a key and value, and cdr cuts off the key
; and just gives the value. So: assoc '1 list returns (1 ( a ))
; and cdr cuts it to (a).
; because the (cdr(assoc loc edg)) might return more than one list
; (cdr cuts the head off, so if (1 (a) (b)) then cdr returns (a) and (b))
; we pass it through the describe-path function, but because it could 
; have more than one list we use mapcar (which takes a function and one or
; more lists as parameters) to pass each list through.
; append will print out the lists as lines, and apply will help
; more in separating the lists.  What apply #'append does is make the output
; more readable. Everything after mapcar comes out as expected, just separated
; into lists.
(defun describe-paths (location edges)
	(apply #'append (mapcar #'describe-path (cdr (assoc location edges)))))
; we defined the parameters for objects and their locations above
; this means that the function here objects-at will take three parameters:
; a location, a list of objects, and a list of objects paired with their locations.
; inside we define a new function called at-loc-p that takes one parameter:
; an object, and looks for a match between the possible objects and the location
; specified. (eq (cadr (assoc obj obj-locs)) loc) the two parameters are:
; (cadr (assoc obj obj-locs)) it returns the second value of the match of 
; 								the obj in the obj-locs list (which is the location of the object
; and loc, which is the specified location.
; eq will return t or nil for all comparisons (not just t)
; the next part (remove-if-not) takes two parameters:
; the newly defined function and the list of objects, and takes out any objects that don't
; return t.
(defun objects-at (loc objs obj-locs)
	(labels ((at-loc-p (obj)
				(eq (cadr (assoc obj obj-locs)) loc)))
		(remove-if-not #'at-loc-p objs)))
; this function, called describe-objects, takes three parameters:
; a location, a list of objects, and a list of objects paired with their locations.
; inside the function is another local function called describe-obj.
; this function describes each object, and we use apply / append to 
; print all of the objects described.		
(defun describe-objects (loc objs obj-loc)
	(labels ((describe-obj (obj)
				`(you see a ,obj on the floor.)))
		(apply #'append (mapcar #'describe-obj (objects-at loc objs obj-loc)))))
; this function is not a traditional functional type. The parameters it takes
; will vary depending on the player's location. All that it does is call the other
; functions we have created, passing the current location as the first parameter
; this location variable is updated by the next function 'walk' each time it is used.
(defun look ()
	(append (describe-location *location* *nodes*)
			(describe-paths *location* *edges*)
			(describe-objects *location* *objects* *object-locations*)))
; this function is used by the player to move around. First it checks
; to see if the passed direction parameter is available, and if it is,
; it resets the location variable and calls the look function; if it isnt
; it tells the player that it can not go that way.
(defun walk (direction)
	(let ((next (find direction
						(cdr (assoc *location* *edges*))
							:key #'cadr)))
	(if next
		(progn (setf *location* (car next))
				(look))
		'(you cannot go that way.))))
; this function is used by the player to remove objects from rooms.
; first the room is checked for the item, then the item, if it is present,
; is moved onto the object locations list to the first index, with "body" set
; as it's value. This function does not remove the old location key-value pair
; but since the assoc function only runs until the first match, it will not 
; move past the key-value pair of object-"body" to object-"former location"
(defun pickup (object)
	(cond ((member object
					(objects-at *location* *objects* *object-locations*))
			(push (list object 'body) *object-locations*)
				`(you are now carring the ,object))
			(t '(you cannot get that.))))
; this function lists all the currently held items. it does this by calling the
; objects-at function and passing 'body as the location parameter. It then makes a
; new list (cons) and begins it with "items"
(defun inventory ()
	(cons 'items- (objects-at 'body *objects* *object-locations*)))
; this function takes a user input (their name)
; and prints out a greeting
(defun say-hello ()
	(princ "Please type your name:")
	(let ((name (read-line)))
		(princ "Nice to meet you, ")
		(princ name)))
; this function is the new game-repl: it will loop for us
; as long as we want it to (until the new cmd variable eq 'quit
(defun game-repl ()
	(let ((cmd (game-read)))
		(unless (eq (car cmd) 'quit)
			(game-print (game-eval cmd))
			(game-repl))))
; this is the game-read function definition
; read-from-string reads a syntax expression from a string
; instead of directly from the console
; the input to read-from-string is the read-line we would expect, surrounded
; by parentheses.
; flet is a local function definition (simpler than lables)
; the quote it function takes one parameter and makes list
; out of it preceded by the word quote (which is a command 
; and is the same as ', so 'mine = quote mine)
; following the local function definition,
; a new list is created with car cmd (the first value of cmd)
; and each cdr cmd value (all the rest) with a quote before them
; in the end, we get a value for the cmd in game-repl that the 
; computer understands
(defun game-read ()
	(let ((cmd (read-from-string
					(concatenate 'string "(" (read-line) ")"))))
		(flet ((quote-it (x)
						(list 'quote x)))
				(cons (car cmd) (mapcar #'quote-it (cdr cmd))))))
; this is the game-eval function, which replaces the standard
; eval function
; this function takes one parameter and checks to see if it is
; in our allowed list of commands
; if it is, the parameter is evaluated using standard eval
; otherwise - error message
(defun game-eval (sexp) 
	(if (member (car sexp) *allowed-commands*)
		(eval sexp)
		'(I do not know that command.)))
; this is the helper function and the game-print function section, 
; replacing standard print
(defun tweak-text (lst caps lit)
	(when lst
	(let ((item (car lst))
		 (rest (cdr lst)))
	(cond ((eq item #\space) (cons item (tweak-text rest caps lit)))
		  ((member item '(#\! #\? #\.)) (cons item (tweak-text rest t lit)))
		  ((eq item #\") (tweak-text rest caps (not lit)))
		   (lit (cons item (tweak-text rest nil lit)))
		  ((or caps lit) (cons (char-upcase item) (tweak-text rest nil lit)))
		  (t (cons (char-downcase item) (tweak-text rest nil nil)))))))
; first inside is prin1-to-string, changing the input to a string and returning it
; next the coerce function changes the new string to a list of individual characters
; next the list goes to the helper function
; the helper function. item is the first value (car), and rest are all of the others (cdr)
; each value is checked and flags are set
; then the returned list is coerced back to a string and princ-ed
; fresh-line does what it sounds like
(defun game-print (lst)
	(princ (coerce (tweak-text (coerce (string-trim "() "
											(prin1-to-string lst))
									'list)
							t
							nil)
				'string))
	(fresh-line))
; this function is working with the graphing utility gvedit
; it will take any string, look for anything that isnt a
; letter or number, and change it to an underscore
; the function alphanumericp returns t if there is a non letter/number
; the function compliment returns the opposite of the returned value (f)
; the substitute-if function substitutes values based on the results
; of a test function:
; if the letters in the string exp are not alphanumeric, make it an _.
; or: substitute _ if (not) letters/numbers string value exp
(defun dot-name (exp)
	(substitute-if #\_ (complement #'alphanumericp) (prin1-to-string exp)))
; this function makes a label. if the length of the passed string is too
; long, it makes the end ...
(defun dot-label (exp)
	(if exp
		(let ((s (write-to-string exp :pretty nil)))
			(if (> (length s) *max-label-length*)
				(concatenate 'string (subseq s 0 (- *max-label-length* 3)) "...")
				s))
		""))
; this function converts our nodes data to DOT format
(defun nodes->dot (nodes)
	(mapc (lambda (node)
			(fresh-line)
			(princ (dot-name (car node)))
			(princ "[label=\"")
			(princ (dot-label node))
			(princ "\"];"))
		nodes))
; this function converts our edges data to DOT format
(defun edges->dot (edges)
	(mapc (lambda (node)
			(mapc (lambda (edge)
					(fresh-line)
					(princ (dot-name (car node)))
					(princ "->")
					(princ (dot-name (car edge)))
					(princ "[label=\"")
					(princ (dot-label (cdr edge)))
					(princ "\"];"))
				(cdr node)))
		edges))
; putting the last two functions together to make a file 
; that will create a graph
(defun graph->dot (nodes edges)
	(princ "digraph{")
	(nodes->dot nodes)
	(edges->dot edges)
		(princ "}"))


(defun dot->png (fname thunk)
	(with-open-file (*standard-output*
						fname
						:direction :output
						:if-exists :supersede)
		(funcall thunk))
	(ext:shell (concatenate 'string "dot -Tpng -O " fname)))

(defun graph->png (fname nodes edges)
	(dot->png fname
				(lambda ()
					(graph->dot nodes edges))))
; these next three function create an undirected graph	
(defun uedges->dot (edges)
	(maplist (lambda (lst)
				(mapc (lambda (edge)
						(unless (assoc (car edge) (cdr lst))
							(fresh-line)
							(princ (dot-name (caar lst)))
							(princ "--")
							(princ (dot-name (car edge)))
							(princ "[label=\"")
							(princ (dot-label (cdr edge)))
							(princ "\"];")))
						(cdar lst)))
				edges))
				
(defun ugraph->dot (nodes edges)
	(princ "graph{")
	(nodes->dot nodes)
	(uedges->dot edges)
	(princ "}"))
	
(defun ugraph->png (fname nodes edges)
	(dot->png fname
			(lambda ()
				(ugraph->dot nodes edges))))
