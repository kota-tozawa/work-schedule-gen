from xlwt import Formula


SUM_WORKING_DAYS = Formula('COUNTA(C7:C37)&"日"')
SUM_WORKING_HOURS = Formula('TEXT(SUM(F7:F37), "h:mm")')
SUM_OVERTIME_HOURS = Formula('TEXT(SUM(G7:G37), "h:mm")')

# 日々の実働時間を計算するためのエクセル関数を作成
wh_formulas = []
for i in range(7, 37):
    c = 'C{i}'.format(i=i)
    d = 'D{i}'.format(i=i)
    e = 'E{i}'.format(i=i)

    wh_formula = 'TEXT(IF(OR({Ci}="", {Di}=""), "", {Di}-{Ci}-{Ei}), "h:mm")'.format(
        Ci=c, Di=d, Ei=e
    )

    wh_formulas.append(wh_formula)

CALC_WORKING_HOURS = [Formula(f) for f in wh_formulas]
