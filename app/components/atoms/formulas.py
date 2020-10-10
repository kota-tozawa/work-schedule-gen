from xlwt import Formula


SUM_WORKING_DAYS = Formula('COUNTA(C7:C37)&"日"')
SUM_WORKING_HOURS = Formula('TEXT(SUM(N7:N37), "[h]:mm")')
SUM_OVERTIME_HOURS = Formula('TEXT(SUM(O7:O37), "[h]:mm")')

# 日々の実働時間を計算するためのエクセル関数を作成
wh_formulas_display = []
wh_formulas_calc = []
for i in range(7, 38):
    # TODO 時間を表示するのと計算を可能にするのがうまく両立できない
    # 現状の対応：見た目用の時間（黒文字白背景）と計算用の時間（白文字白背景）を別に用意する
    c = 'C{i}'.format(i=i)
    d = 'D{i}'.format(i=i)
    e = 'E{i}'.format(i=i)
    wh_formula_display = 'TEXT(IF(OR({Ci}="", {Di}=""), "", {Di}-{Ci}-{Ei}), "h:mm")'.format(
        Ci=c, Di=d, Ei=e
    )
    wh_formulas_display.append(wh_formula_display)

    f = 'F{i}'.format(i=i)
    wh_formula_calc = 'IF({Fi}="", 0, VALUE({Fi}))'.format(Fi=f)
    wh_formulas_calc.append(wh_formula_calc)

DISPLAY_WORKING_HOURS = [Formula(f) for f in wh_formulas_display]
CALC_WORKING_HOURS = [Formula(f) for f in wh_formulas_calc]

# 日々の残業時間を計算するためのエクセル関数を作成
oh_formulas_display = []
oh_formulas_calc = []
for i in range(7, 38):
    # TODO 時間を表示するのと計算を可能にするのがうまく両立できない
    # 現状の対応：見た目用の時間（黒文字白背景）と計算用の時間（白文字白背景）を別に用意する
    f = 'F{i}'.format(i=i)
    oh_formula_display = 'TEXT(IF({Fi}="","",IF(TIMEVALUE({Fi})>TIME(8,0,0),TIMEVALUE({Fi})-TIME(8,0,0),"")), "h:mm")'.format(
        Fi=f
    )
    oh_formulas_display.append(oh_formula_display)

    g = 'G{i}'.format(i=i)
    oh_formula_calc = 'IF({Gi}="", 0, VALUE({Gi}))'.format(Gi=g)
    oh_formulas_calc.append(oh_formula_calc)

DISPLAY_OVERTIME_HOURS = [Formula(f) for f in oh_formulas_display]
CALC_OVERTIME_HOURS = [Formula(f) for f in oh_formulas_calc]
