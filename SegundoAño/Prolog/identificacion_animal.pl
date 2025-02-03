%Proposiciones
% Preguntas
prop(1,' es un canido',p).
prop(2,' es grande',p).
prop(3, ' es pequeño',p).
prop(4,' es domestico',p).
prop(5,' es fiel a su amo',p).
prop(6,' es un felido',p).
prop(7,' es un ave',p).
prop(8,' habla',p).

% Intermedios
prop(11,'grande o pequeño',i).

% Objetivos
prop(101,' es un PERRO.',i).
prop(102,' es un GATO.',i).
prop(103,' es una COTORRA.',i).

clase(1,objetivos,[101,102,103]).

% Reglas
regla(1,o,[2,3],11,1.0).
regla(2,y,[1,11,4],101,0.6).
regla(3,y,[5],101,0.8).
regla(4,y,[6,3,4],102,0.8).
regla(5,y,[7,3,8],103,1.0).

%Predicados
%Función para calculcar el mínimo
min(A, B, C, Min) :- Min is min(A, B, C).
%Función para calcular el máximo
max(A, B, Max) :- Max is max(A, B).
%Función de contribución prop.
ctr(A, B, Ctr) :- Ctr is A * B.
%Función de globalidad
glob(A, B, Glob) :- Glob is (A + B) / (1 + A * B).
%Predicado principal para calcular el peso
peso_prop(ID, W) :-
    ID = 101 -> write('Diga el grado de certeza de es un cánido: '),
    read(P1),
    write('Diga el grado de certeza de es grande: '),
    read(P2),
    write('Diga el grado de certeza de es pequeño: '),
    read(P3),
    write('Diga el grado de certeza de es doméstico: '),
    read(P4),
    write('Diga el grado de certeza de es fiel a su amo: '),
    read(P5),
%Cálculo del mínimo y ctr
    regla(1,o,[2,3],11,P11),
    min(P1, P11, P4, MinW),
    regla(2,y,[1,11,4],101,Ctr1),
    ctr(MinW, Ctr1, R1),
    regla(3,y,[5],101,Ctr2),
    ctr(P5, Ctr2, R2),
    ctr(R1, 0.6, R3),
    ctr(R2, 0.8, R4),
%Cálculo de la función de globalidad
    glob(R3, R4, W)
    ;
    ID = 102 -> write('Diga el grado de certeza de es pequeño: '),
    read(P3),
    write('Diga el grado de certeza de es doméstico: '),
    read(P4),
    write('Diga el grado de certeza de es un félido: '),
    read(P6),
%Cálculo del mínimo y ctr
    min(P6, P3, P4, MinW),
    regla(4,y,[6,3,4],102,Ctr1),
    ctr(MinW, Ctr1, R1),
    ctr(R1, 0.8, R2),
%Cálculo de la función de globalidad
    glob(R2, 0, W)
    ;
    ID = 103 -> write('Diga el grado de certeza de es pequeño: '),
    read(P3),
    write('Diga el grado de certeza de es un ave: '),
    read(P7),
    write('Diga el grado de certeza de habla: '),
    read(P8),
%Cálculo del mínimo y ctr
    min(P7, P3, P8, MinW),
    regla(5,y,[7,3,8],103,Ctr1),
    ctr(MinW, Ctr1, R1),
    ctr(R1, 1.0, R2),
%Cálculo de la función de globalidad
    glob(R2, 0, W).

%Programa Principal
main :- nl, write('Consulta'),
   nl, nl,
   write('Entre el ID de la prop. a investigar: '),
   read(I),
   peso_prop(I, W),
   nl, nl, write('El peso calculado para el ID '), write(ID), write(' es: '), write(W), nl.