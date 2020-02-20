import matplotlib.pyplot as plt

brackets_2020 = [
    ( 41725,  0.0506),
    ( 83451,  0.0770),
    ( 95812,  0.1050),
    (116344,  0.1229),
    (157748,  0.1470),
    (220000,  0.1680),
    (  None,  0.205),
    ]

brackets_2019 = [
    ( 40707,  0.0506),
    ( 81416,  0.0770),
    ( 93476,  0.1050),
    (113506,  0.1229),
    (153900,  0.1470),
    (None,    0.1680),
    ]

def get_taxes(x, brackets):
    taxes = 0
    prev_bracket = 0
    for (bracket, rate) in brackets:
        xx = x - prev_bracket
        if xx > 0:
            if bracket is None or x < bracket:
                taxes += xx * rate
            else:
                taxes += (bracket-prev_bracket) * rate
        prev_bracket = bracket
    return taxes

for (test_income, expected_taxes) in (
    ( 20000  , 20000 * 0.0506),
    ( 80000  , 40707 * 0.0506 + (80000 - 40707) * 0.0770),
    ( 90000 , 40707 * 0.0506 + (81416 - 40707) * 0.0770 + (90000 - 81416) * 0.1050),
    ):
    taxes = get_taxes(test_income, brackets_2019)
    diff = taxes - expected_taxes
    print(f'{test_income}: {diff}')
    assert abs(diff) < 1

end = 250000
income = list(range(1, end, 1000))
taxes2019 = list(get_taxes(x, brackets_2019) / x for x in income)
taxes2020 = list(get_taxes(x, brackets_2020) / x for x in income)
taxes_diff = list(get_taxes(x, brackets_2020) - get_taxes(x, brackets_2019) for x in income)
taxes_diff_percentage = list((get_taxes(x, brackets_2020)-get_taxes(x, brackets_2019)) / get_taxes(x, brackets_2019) for x in income)

plt.plot(income, taxes2019, '.', label=2019)
plt.plot(income, taxes2020, '.', label=2020)
plt.ylabel('taxes')
plt.xlabel('income')
plt.legend()
plt.savefig('taxes_2019_and_2020.png', bbox_inches='tight')
plt.cla()

plt.plot(income, taxes_diff, '.')
plt.ylabel('taxes')
plt.xlabel('income')
plt.title('difference between 2019 and 2020 taxes')
plt.savefig('taxes_diff.png', bbox_inches='tight')
plt.cla()

plt.plot(income, taxes_diff_percentage, '.')
plt.ylabel('taxes')
plt.xlabel('income')
plt.title('difference between 2019 and 2020 taxes as percentage')
plt.savefig('taxes_diff_pct.png', bbox_inches='tight')
plt.cla()

#plt.show()

