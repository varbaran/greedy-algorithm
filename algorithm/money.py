data = {
    "p1": [
        ("p2",-1000),
        ("p4", 2500),
        ("p5", -500),
        ("p3", 1000)
    ],
    "p2": [
        ("p1", 1000),
        ("p3", -1000),
        ("p4", -2000),
    ],
    "p3": [
        ("p1", -1000),
        ("p4", -500),
        ("p2", 1000),
    ],
    "p4": [
        ("p2", 2000),
        ("p3", 500),
        ("p1", -2500),
        ("p5", 1000)
    ],
    "p5": [
        ("p1", 500),
        ("p4", -1000),
    ]
}
processed_data = []
for key,value in data.items():
    print(f"processing {key}")
    debt_or_credit = 0
    for t in value:
        debt_or_credit += t[1]
    print(f"debt or credit for {key} is {debt_or_credit}")
    processed_data.append([key,debt_or_credit])
print(processed_data)
processed_data.sort(key=lambda x: x[1])
print(processed_data)
while any([x[1] != 0 for x in processed_data]):
    max_creditor = processed_data[0]
    max_debtor= processed_data[-1]
    r = max_creditor[1] + max_debtor[1]
    print(f"remaining from {max_creditor[0]} and {max_debtor[0]} is {r}")
    if r < 0:
        processed_data[-1][1] = 0
        processed_data[0][1] = r
    else:
        processed_data[-1][1] = r
        processed_data[0][1] = 0
    processed_data.sort(key=lambda x: x[1])
