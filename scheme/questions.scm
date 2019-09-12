(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))



;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (helper s index)
    (if (null? s) '()
    (cons (cons index (cons (car s) nil )) (helper (cdr s) (+ index 1)))
  ))
  (helper s 0)
  )
  ; END PROBLEM 17

;; Problem 18

(define (zip pairs)
  ; BEGIN PROBLEM 18
  (if (eq? '() pairs) '(() ())
  (cons (map car pairs) (cons (map cadr pairs) nil))
  ))
  ; END PROBLEM 18


;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons form (cons params (let-to-lambda body)))
           ;`(,form ,params ,(let-to-lambda body))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           ;car of zip variables
           ;cdr of zip is going to be the numbers
           (cons (let-to-lambda(cons 'lambda (cons (car(zip values)) (let-to-lambda body)))) (let-to-lambda(cadr (zip values))))
           ;(cons 'lambda (cons (car(zip values)) (cons (let-to-lambda body) nil) (cdr(zip values))))
           ;`((lamdba ,(car(zip values)) ,(let-to-lambda body)) ,(cdr(zip values)))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
