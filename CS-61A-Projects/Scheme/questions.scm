(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cddr x) (cdr (cdr x)))
(define (cadar x) (car (cdr (car x))))

; Some utility functions that you may find useful to implement.
(define (map proc items)
        (if (equal? items nil)
            '()
            (cons (proc (car items)) (map proc (cdr items)))))

(define (cons-all first rests)
        (cond ((equal? '() rests) (list (cons first nil)))
              ((equal? '() (cdr rests)) (list (cons first (car rests))))
              (else (cons (cons first (car rests)) 
                          (cons-all first (cdr rests))))))

(define (zip pairs)
        (cond ((equal? '() pairs) '(() ()))
              ((equal? '() (cdr pairs)) (map (lambda (x) (cons x nil)) (car pairs)))
              ((equal? '() (car pairs)) nil)
              (else (cons (map (lambda (x) (car x)) pairs)
                          (zip (map (lambda (x) (cdr x)) pairs))))))

;; Problem 18
;; Returns a list of two-element lists
(define (enumerate s)
        (define (enumerate2 s start_index)
                (if (null? s) 
                    '()
                    (cons (list start_index (car s)) (enumerate2 (cdr s) (+ start_index 1)))))
        (enumerate2 s 0))


;; Problem 19
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN Question 19
  (cond ((equal? denoms '()) '())
        ((= 1 total) '((1)))
        ((< total (car denoms)) (list-change total (cdr denoms)))
        (else (append (cons-all (car denoms) 
                                (list-change (- total (car denoms)) denoms))
                      (list-change total (cdr denoms))))))


;; Problem 20
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (analyze expr)
  (cond ((atom? expr)
          expr ; Michael: if atoms, return itself
         )
        ((quoted? expr)
         expr ; Michael: if quoted, do nothing
        )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN Question 20
           (append (list form params) (map analyze body))))
           ; END Question 20
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN Question 20
           (define zipped (zip values)) ; Michael: separate params and values

           (define params (car zipped)) ; Michael: get parameters
           (define args (map analyze (cadr zipped))) ; Michael: get new argument values
           
           (define fn (append (list 'lambda params) (map analyze body)))
           
           (cons fn args)
          ))
        (else
         (map analyze expr) ; Michael: otherwise, analyze everything in the expr
         ))))


