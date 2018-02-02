from kb import KB, Boolean, Integer

# Initialise all variables that you need for you strategies and game knowledge.
# First all possible cards:
J0 = Boolean('j0')
J1 = Boolean('j1')
J2 = Boolean('j2')
J3 = Boolean('j3')
J4 = Boolean('j4')
J5 = Boolean('j5')
J6 = Boolean('j6')
J7 = Boolean('j7')
J8 = Boolean('j8')
J9 = Boolean('j9')
J10 = Boolean('j10')
J11 = Boolean('j11')
J12 = Boolean('j12')
J13 = Boolean('j13')
J14 = Boolean('j14')
J15 = Boolean('j15')
J16 = Boolean('j16')
J17 = Boolean('j17')
J18 = Boolean('j18')
J19 = Boolean('j19')

Q0 = Boolean('q0')
Q1 = Boolean('q1')
Q2 = Boolean('q2')
Q3 = Boolean('q3')
Q4 = Boolean('q4')
Q5 = Boolean('q5')
Q6 = Boolean('q6')
Q7 = Boolean('q7')
Q8 = Boolean('q8')
Q9 = Boolean('q9')
Q10 = Boolean('q10')
Q11 = Boolean('q11')
Q12 = Boolean('q12')
Q13 = Boolean('q13')
Q14 = Boolean('q14')
Q15 = Boolean('q15')
Q16 = Boolean('q16')
Q17 = Boolean('q17')
Q18 = Boolean('q18')
Q19 = Boolean('q19')

K0 = Boolean('k0')
K1 = Boolean('k1')
K2 = Boolean('k2')
K3 = Boolean('k3')
K4 = Boolean('k4')
K5 = Boolean('k5')
K6 = Boolean('k6')
K7 = Boolean('k7')
K8 = Boolean('k8')
K9 = Boolean('k9')
K10 = Boolean('k10')
K11 = Boolean('k11')
K12 = Boolean('k12')
K13 = Boolean('k13')
K14 = Boolean('k14')
K15 = Boolean('k15')
K16 = Boolean('k16')
K17 = Boolean('k17')
K18 = Boolean('k18')
K19 = Boolean('k19')

T0 = Boolean('t0')
T1 = Boolean('t1')
T2 = Boolean('t2')
T3 = Boolean('t3')
T4 = Boolean('t4')
T5 = Boolean('t5')
T6 = Boolean('t6')
T7 = Boolean('t7')
T8 = Boolean('t8')
T9 = Boolean('t9')
T10 = Boolean('t10')
T11 = Boolean('t11')
T12 = Boolean('t12')
T13 = Boolean('t13')
T14 = Boolean('t14')
T15 = Boolean('t15')
T16 = Boolean('t16')
T17 = Boolean('t17')
T18 = Boolean('t18')
T19 = Boolean('t19')

A0 = Boolean('a0')
A1 = Boolean('a1')
A2 = Boolean('a2')
A3 = Boolean('a3')
A4 = Boolean('a4')
A5 = Boolean('a5')
A6 = Boolean('a6')
A7 = Boolean('a7')
A8 = Boolean('a8')
A9 = Boolean('a9')
A10 = Boolean('a10')
A11 = Boolean('a11')
A12 = Boolean('a12')
A13 = Boolean('a13')
A14 = Boolean('a14')
A15 = Boolean('a15')
A16 = Boolean('a16')
A17 = Boolean('a17')
A18 = Boolean('a18')
A19 = Boolean('a19')

M23 = Boolean('m23')
M78 = Boolean('m78')
M1213 = Boolean('m1213')
M1718 = Boolean('m1718')
M32 = Boolean('m32')
M87 = Boolean('m87')
M1312 = Boolean('m1312')
M1817 = Boolean('m1817')

WTTCC = Boolean('wttCC')
WTTDD = Boolean('wttDD')
WTTHH = Boolean('wttHH')
WTTSS = Boolean('wttSS')

#Play Jack
PJ0 = Boolean('pj0')
PJ1 = Boolean('pj1')
PJ2 = Boolean('pj2')
PJ3 = Boolean('pj3')
PJ4 = Boolean('pj4')
PJ5 = Boolean('pj5')
PJ6 = Boolean('pj6')
PJ7 = Boolean('pj7')
PJ8 = Boolean('pj8')
PJ9 = Boolean('pj9')
PJ10 = Boolean('pj10')
PJ11 = Boolean('pj11')
PJ12 = Boolean('pj12')
PJ13 = Boolean('pj13')
PJ14 = Boolean('pj14')
PJ15 = Boolean('pj15')
PJ16 = Boolean('pj16')
PJ17 = Boolean('pj17')
PJ18 = Boolean('pj18')
PJ19 = Boolean('pj19')

#Play Queen
PQ0 = Boolean('pq0')
PQ1 = Boolean('pq1')
PQ2 = Boolean('pq2')
PQ3 = Boolean('pq3')
PQ4 = Boolean('pq4')
PQ5 = Boolean('pq5')
PQ6 = Boolean('pq6')
PQ7 = Boolean('pq7')
PQ8 = Boolean('pq8')
PQ9 = Boolean('pq9')
PQ10 = Boolean('pq10')
PQ11 = Boolean('pq11')
PQ12 = Boolean('pq12')
PQ13 = Boolean('pq13')
PQ14 = Boolean('pq14')
PQ15 = Boolean('pq15')
PQ16 = Boolean('pq16')
PQ17 = Boolean('pq17')
PQ18 = Boolean('pq18')
PQ19 = Boolean('pq19')

#Play King
PK0 = Boolean('pk0')
PK1 = Boolean('pk1')
PK2 = Boolean('pk2')
PK3 = Boolean('pk3')
PK4 = Boolean('pk4')
PK5 = Boolean('pk5')
PK6 = Boolean('pk6')
PK7 = Boolean('pk7')
PK8 = Boolean('pk8')
PK9 = Boolean('pk9')
PK10 = Boolean('pk10')
PK11 = Boolean('pk11')
PK12 = Boolean('pk12')
PK13 = Boolean('pk13')
PK14 = Boolean('pk14')
PK15 = Boolean('pk15')
PK16 = Boolean('pk16')
PK17 = Boolean('pk17')
PK18 = Boolean('pk18')
PK19 = Boolean('pk19')

#Play Ten
PT0 = Boolean('pt0')
PT1 = Boolean('pt1')
PT2 = Boolean('pt2')
PT3 = Boolean('pt3')
PT4 = Boolean('pt4')
PT5 = Boolean('pt5')
PT6 = Boolean('pt6')
PT7 = Boolean('pt7')
PT8 = Boolean('pt8')
PT9 = Boolean('pt9')
PT10 = Boolean('j10')
PT11 = Boolean('pt11')
PT12 = Boolean('pt12')
PT13 = Boolean('pt13')
PT14 = Boolean('pt14')
PT15 = Boolean('pt15')
PT16 = Boolean('p16')
PT17 = Boolean('pt17')
PT18 = Boolean('pt18')
PT19 = Boolean('pt19')

PA0 = Boolean('pa0')
PA1 = Boolean('pa1')
PA2 = Boolean('pa2')
PA3 = Boolean('pa3')
PA4 = Boolean('pa4')
PA5 = Boolean('pa5')
PA6 = Boolean('pa6')
PA7 = Boolean('pa7')
PA8 = Boolean('pa8')
PA9 = Boolean('pa9')
PA10 = Boolean('pa10')
PA11 = Boolean('pa11')
PA12 = Boolean('pa12')
PA13 = Boolean('pa13')
PA14 = Boolean('pa14')
PA15 = Boolean('pa15')
PA16 = Boolean('pa16')
PA17 = Boolean('pa17')
PA18 = Boolean('pa18')
PA19 = Boolean('pa19')

#Trump Kings
TK0 = Boolean('tk0')
TK1 = Boolean('tk1')
TK2 = Boolean('tk2')
TK3 = Boolean('tk3')
TK4 = Boolean('tk4')
TK5 = Boolean('tk5')
TK6 = Boolean('tk6')
TK7 = Boolean('tk7')
TK8 = Boolean('tk8')
TK9 = Boolean('tk9')
TK10 = Boolean('tk10')
TK11 = Boolean('tk11')
TK12 = Boolean('tk12')
TK13 = Boolean('tk13')
TK14 = Boolean('tk14')
TK15 = Boolean('tk15')
TK16 = Boolean('tk16')
TK17 = Boolean('tk17')
TK18 = Boolean('tk18')
TK19 = Boolean('tk19')

#Trump Queens
TQ0 = Boolean('tq0')
TQ1 = Boolean('tq1')
TQ2 = Boolean('tq2')
TQ3 = Boolean('tq3')
TQ4 = Boolean('tq4')
TQ5 = Boolean('tq5')
TQ6 = Boolean('tq6')
TQ7 = Boolean('tq7')
TQ8 = Boolean('tq8')
TQ9 = Boolean('tq9')
TQ10 = Boolean('tq10')
TQ11 = Boolean('tq11')
TQ12 = Boolean('tq12')
TQ13 = Boolean('tq13')
TQ14 = Boolean('tq14')
TQ15 = Boolean('tq15')
TQ16 = Boolean('tq16')
TQ17 = Boolean('tq17')
TQ18 = Boolean('tq18')
TQ19 = Boolean('tq19')

#Trump Ace
TA0 = Boolean('ta0')
TA1 = Boolean('ta1')
TA2 = Boolean('ta2')
TA3 = Boolean('ta3')
TA4 = Boolean('ta4')
TA5 = Boolean('ta5')
TA6 = Boolean('ta6')
TA7 = Boolean('ta7')
TA8 = Boolean('ta8')
TA9 = Boolean('ta9')
TA10 = Boolean('ta10')
TA11 = Boolean('ta11')
TA12 = Boolean('ta12')
TA13 = Boolean('ta13')
TA14 = Boolean('ta14')
TA15 = Boolean('ta15')
TA16 = Boolean('ta16')
TA17 = Boolean('ta17')
TA18 = Boolean('ta18')
TA19 = Boolean('ta19')

#Trump Ten
TT0 = Boolean('tt0')
TT1 = Boolean('tt1')
TT2 = Boolean('tt2')
TT3 = Boolean('tt3')
TT4 = Boolean('tt4')
TT5 = Boolean('tt5')
TT6 = Boolean('tt6')
TT7 = Boolean('tt7')
TT8 = Boolean('tt8')
TT9 = Boolean('tt9')
TT10 = Boolean('tt10')
TT11 = Boolean('tt11')
TT12 = Boolean('tt12')
TT13 = Boolean('tt13')
TT14 = Boolean('tt14')
TT15 = Boolean('tt15')
TT16 = Boolean('tt16')
TT17 = Boolean('tt17')
TT18 = Boolean('tt18')
TT19 = Boolean('tt19')

#Trump Jack
TJ0 = Boolean('tj0')
TJ1 = Boolean('tj1')
TJ2 = Boolean('tj2')
TJ3 = Boolean('tj3')
TJ4 = Boolean('tj4')
TJ5 = Boolean('tj5')
TJ6 = Boolean('tj6')
TJ7 = Boolean('tj7')
TJ8 = Boolean('tj8')
TJ9 = Boolean('tj9')
TJ10 = Boolean('tj10')
TJ11 = Boolean('tj11')
TJ12 = Boolean('tj12')
TJ13 = Boolean('tj13')
TJ14 = Boolean('tj14')
TJ15 = Boolean('tj15')
TJ16 = Boolean('tj16')
TJ17 = Boolean('tj17')
TJ18 = Boolean('tj18')
TJ19 = Boolean('tj19')

#Play Trump Tens
PTT0 = Boolean('ptt0')
PTT1 = Boolean('ptt1')
PTT2 = Boolean('ptt2')
PTT3 = Boolean('ptt3')
PTT4 = Boolean('ptt4')
PTT5 = Boolean('ptt5')
PTT6 = Boolean('ptt6')
PTT7 = Boolean('ptt7')
PTT8 = Boolean('ptt8')
PTT9 = Boolean('ptt9')
PTT10 = Boolean('ptt10')
PTT11 = Boolean('ptt11')
PTT12 = Boolean('ptt12')
PTT13 = Boolean('ptt13')
PTT14 = Boolean('ptt14')
PTT15 = Boolean('ptt15')
PTT16 = Boolean('ptt16')
PTT17 = Boolean('ptt17')
PTT18 = Boolean('ptt18')
PTT19 = Boolean('ptt19')

#Play Trump Aces
PTA0 = Boolean('pta0')
PTA1 = Boolean('pta1')
PTA2 = Boolean('pta2')
PTA3 = Boolean('pta3')
PTA4 = Boolean('pta4')
PTA5 = Boolean('pta5')
PTA6 = Boolean('pta6')
PTA7 = Boolean('pta7')
PTA8 = Boolean('pta8')
PTA9 = Boolean('pta9')
PTA10 = Boolean('pta10')
PTA11 = Boolean('pta11')
PTA12 = Boolean('pta12')
PTA13 = Boolean('pta13')
PTA14 = Boolean('pta14')
PTA15 = Boolean('pta15')
PTA16 = Boolean('pta16')
PTA17 = Boolean('pta17')
PTA18 = Boolean('pta18')
PTA19 = Boolean('pta19')

#Play Trump Kings
PTK0 = Boolean('ptk0')
PTK1 = Boolean('ptk1')
PTK2 = Boolean('ptk2')
PTK3 = Boolean('ptk3')
PTK4 = Boolean('ptk4')
PTK5 = Boolean('ptk5')
PTK6 = Boolean('ptk6')
PTK7 = Boolean('ptk7')
PTK8 = Boolean('ptk8')
PTK9 = Boolean('ptk9')
PTK10 = Boolean('ptk10')
PTK11 = Boolean('ptk11')
PTK12 = Boolean('ptk12')
PTK13 = Boolean('ptk13')
PTK14 = Boolean('ptk14')
PTK15 = Boolean('ptk15')
PTK16 = Boolean('ptk16')
PTK17 = Boolean('ptk17')
PTK18 = Boolean('ptk18')
PTK19 = Boolean('ptk19')

#Play Trump Queen
PTQ0 = Boolean('ptq0')
PTQ1 = Boolean('ptq1')
PTQ2 = Boolean('ptq2')
PTQ3 = Boolean('ptq3')
PTQ4 = Boolean('ptq4')
PTQ5 = Boolean('ptq5')
PTQ6 = Boolean('ptq6')
PTQ7 = Boolean('ptq7')
PTQ8 = Boolean('ptq8')
PTQ9 = Boolean('ptq9')
PTQ10 = Boolean('ptq10')
PTQ11 = Boolean('ptq11')
PTQ12 = Boolean('ptq12')
PTQ13 = Boolean('ptq13')
PTQ14 = Boolean('ptq14')
PTQ15 = Boolean('ptq15')
PTQ16 = Boolean('ptq16')
PTQ17 = Boolean('ptq17')
PTQ18 = Boolean('ptq18')
PTQ19 = Boolean('ptq19')

#Play Trump Jack
PTJ0 = Boolean('ptj0')
PTJ1 = Boolean('ptj1')
PTJ2 = Boolean('ptj2')
PTJ3 = Boolean('ptj3')
PTJ4 = Boolean('ptj4')
PTJ5 = Boolean('ptj5')
PTJ6 = Boolean('ptj6')
PTJ7 = Boolean('ptj7')
PTJ8 = Boolean('ptj8')
PTJ9 = Boolean('ptj9')
PTJ10 = Boolean('ptj10')
PTJ11 = Boolean('ptj11')
PTJ12 = Boolean('ptj12')
PTJ13 = Boolean('ptj13')
PTJ14 = Boolean('ptj14')
PTJ15 = Boolean('ptj15')
PTJ16 = Boolean('ptj16')
PTJ17 = Boolean('ptj17')
PTJ18 = Boolean('ptj18')
PTJ19 = Boolean('ptj19')



def general_information(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    kb.add_clause(J4)
    kb.add_clause(J9)
    kb.add_clause(J14)
    kb.add_clause(J19)

    kb.add_clause(Q3)
    kb.add_clause(Q8)
    kb.add_clause(Q13)
    kb.add_clause(Q18)

    kb.add_clause(K2)
    kb.add_clause(K7)
    kb.add_clause(K12)
    kb.add_clause(K17)

    kb.add_clause(T1)
    kb.add_clause(T6)
    kb.add_clause(T11)
    kb.add_clause(T16)

    kb.add_clause(A0)
    kb.add_clause(A5)
    kb.add_clause(A10)
    kb.add_clause(A15)


def strategy_knowledge(kb):
    # Knowledge base for marriages
    kb.add_clause(M23)
    kb.add_clause(M78)
    kb.add_clause(M1213)
    kb.add_clause(M1718)

    kb.add_clause(M32)
    kb.add_clause(M87)
    kb.add_clause(M1312)
    kb.add_clause(M1817)

    # Use Trump card to win trick
    kb.add_clause(WTTCC)
    kb.add_clause(WTTSS)
    kb.add_clause(WTTHH)
    kb.add_clause(WTTDD)

    #aces
    kb.add_clause(~A0, PA0)
    kb.add_clause(~A5, PA5)
    kb.add_clause(~A10, PA10)
    kb.add_clause(~A15, PA15)
    kb.add_clause(~PA0, A0)
    kb.add_clause(~PA5, A5)
    kb.add_clause(~PA10, A10)
    kb.add_clause(~PA15, A15)

    #tens

    kb.add_clause(~T1, PT1)
    kb.add_clause(~T6, PT6)
    kb.add_clause(~T11, PT11)
    kb.add_clause(~T16, PT16)
    kb.add_clause(~PT1, T1)
    kb.add_clause(~PT6, T6)
    kb.add_clause(~PT11, T11)
    kb.add_clause(~PT16, T16)

    #kings
    kb.add_clause(~K2, PK2)
    kb.add_clause(~K7, PK7)
    kb.add_clause(~K12, PK12)
    kb.add_clause(~K17, PK17)
    kb.add_clause(~PK2, K2)
    kb.add_clause(~PK7, K7)
    kb.add_clause(~PK12, K12)
    kb.add_clause(~PK17, K17)

    #Queens

    kb.add_clause(~Q3, PQ3)
    kb.add_clause(~Q8, PQ8)
    kb.add_clause(~Q13, PQ13)
    kb.add_clause(~Q18, PQ18)
    kb.add_clause(~PQ3, Q3)
    kb.add_clause(~PQ8, Q8)
    kb.add_clause(~PQ13, Q13)
    kb.add_clause(~PQ18, Q18)

    #Jack
    kb.add_clause(~J4, PJ4)
    kb.add_clause(~J9, PJ9)
    kb.add_clause(~J14, PJ14)
    kb.add_clause(~J19, PJ19)
    kb.add_clause(~PJ4, J4)
    kb.add_clause(~PJ9, J9)
    kb.add_clause(~PJ14, J14)
    kb.add_clause(~PJ19, J19)

    # PLAY TRUMP ACE
    kb.add_clause(~TA0, PTA0)
    kb.add_clause(~TA5, PTA5)
    kb.add_clause(~TA10, PTA10)
    kb.add_clause(~TA15, PTA15)
    kb.add_clause(~PTA0, TA0)
    kb.add_clause(~PTA5, TA5)
    kb.add_clause(~PTA10, TA10)
    kb.add_clause(~PTA15, TA15)

    # PLAY TRUMP TEN
    kb.add_clause(~TT1, PTT1)
    kb.add_clause(~TT6, PTT6)
    kb.add_clause(~TT11, PTT11)
    kb.add_clause(~TT16, PTT16)
    kb.add_clause(~PTT1, TT1)
    kb.add_clause(~PTT6, TT6)
    kb.add_clause(~PTT11, TT11)
    kb.add_clause(~PTT16, TT16)

    # PLAY TRUMP KING
    kb.add_clause(~TK2, PTK2)
    kb.add_clause(~TK7, PTK7)
    kb.add_clause(~TK12, PTK12)
    kb.add_clause(~TK17, PTK17)
    kb.add_clause(~PTK2, TK2)
    kb.add_clause(~PTK7, TK7)
    kb.add_clause(~PTK12, TK12)
    kb.add_clause(~PTK17, TK17)

    # PLAY TRUMP QUEEN
    kb.add_clause(~TQ3, PTQ3)
    kb.add_clause(~TQ8, PTQ8)
    kb.add_clause(~TQ13, PTQ13)
    kb.add_clause(~TQ18, PTQ18)
    kb.add_clause(~PTQ3, TQ3)
    kb.add_clause(~PTQ8, TQ8)
    kb.add_clause(~PTQ13, TQ13)
    kb.add_clause(~PTQ18, TQ18)

    # PLAY TRUMP JACK
    kb.add_clause(~TJ4, PTJ4)
    kb.add_clause(~TJ9, PTJ9)
    kb.add_clause(~TJ14, PTJ14)
    kb.add_clause(~TJ19, PTJ19)
    kb.add_clause(~PTJ4, TJ4)
    kb.add_clause(~PTJ9, TJ9)
    kb.add_clause(~PTJ14, TJ14)
    kb.add_clause(~PTJ19, TJ19)

    kb.add_clause(WTTCC)
    kb.add_clause(WTTSS)
    kb.add_clause(WTTHH)
    kb.add_clause(WTTDD)

    # Knowledge base for marriages
    kb.add_clause(M23)
    kb.add_clause(M78)
    kb.add_clause(M1213)
    kb.add_clause(M1718)

    kb.add_clause(M32)
    kb.add_clause(M87)
    kb.add_clause(M1312)
    kb.add_clause(M1817)

    kb.add_clause(~A0, PA0)
    kb.add_clause(~A5, PA5)
    kb.add_clause(~A10, PA10)
    kb.add_clause(~A15, PA15)
    kb.add_clause(~PA0, A0)
    kb.add_clause(~PA5, A5)
    kb.add_clause(~PA10, A10)
    kb.add_clause(~PA15, A15)
