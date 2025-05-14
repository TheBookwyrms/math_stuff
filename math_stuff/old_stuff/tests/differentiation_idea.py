# notes:
#       takes monomials with the number first (as a single number),
#       the only accepted variable is x
#       all variables must be written individually and in lowercase:
#           examples: 3xxxx, 0.438x

def monomial_with_x_deriver(monomial):
    print(monomial)
    nums = float("".join(num for num in [num for num in monomial if num != "x"] if num != "X"))
    x_s = "".join([x for x in monomial if x == "x"])
    power = (len(x_s))

    new_x_s = ""
    for x in range(len(x_s)-1):
        new_x_s += "x"


    if int(nums*power) == nums*power:
        derivative = str(f'{int(nums*power)}{new_x_s}')
    else:
        derivative = str(f'{nums*power}{new_x_s}')

    return(derivative)

def polynomial_addition_subtraction_deriver(polynomial):
    separated_plus = polynomial.split("+")
    print(separated_plus)
    
    separated_removed = []

    blank0 = ""
    for i in range(0,5):
        for item in separated_plus:
            if "-" in item:
                print(separated_plus)
                print(f'{separated_removed}+"removed"')
                sep = item.split("-")
                print(sep)
                separated_plus.remove(item)
                if sep[0] != blank0:
                    separated_plus.append(sep[0])
                sep.pop(0)
                for item in sep:
                    separated_removed.append(item)

    print(separated_plus)
    print(separated_removed)

    separated = separated_plus+separated_removed

    derived_polynomial = ""
    for term in separated:
        if term in separated_removed:
            derived_polynomial += "-"+monomial_with_x_deriver(term)
        else:
            derived_polynomial += "+"+monomial_with_x_deriver(term)
    derived_polynomial = derived_polynomial.lstrip("+")

    return(derived_polynomial)

print(polynomial_addition_subtraction_deriver("-3xx+2-2.2x+3-4.8xxx-1xx+3x"))