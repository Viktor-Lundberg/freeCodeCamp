def arithmetic_arranger(problems, answers=None):
    firstlinevalues = []
    secondlineoperators = []
    dashline = []
    forthlineanswers = []

    if len(problems) > 5:
        return "Error: Too many problems."


    for problem in problems:
        tal = problem.split()
        firstvalue = tal[0]
        secondvalue = tal[2]
        operand = tal[1]
        if not secondvalue.isdecimal() or not firstvalue.isdecimal():
            return "Error: Numbers must only contain digits."
        if len(firstvalue) > 4 or len(secondvalue) > 4:
            return "Error: Numbers cannot be more than four digits."
        if (operand != '+') and (operand != '-'):
            return "Error: Operator must be '+' or '-'."

        if operand == '+':
            answer = int(firstvalue) + int(secondvalue)

        else:
            answer = int(firstvalue) - int(secondvalue)


        lenghtofline = max(len(firstvalue), len(secondvalue))
        space = ' ' * 3
        dashes = '-' * lenghtofline + '--' + space
        dashline.append(dashes)
        operands = operand + ' ' + secondvalue.rjust(lenghtofline) + space
        secondlineoperators.append(operands)

        firstvalues = firstvalue.rjust(lenghtofline + 2) + space
        firstlinevalues.append(firstvalues)
        results = str(answer).rjust(lenghtofline + 2) + space
        forthlineanswers.append(results)


    if answers == True:
        return ' '.join(firstlinevalues).rstrip() + '\n' + ' '.join(secondlineoperators).rstrip() + '\n' + ' '.join(dashline).rstrip() + '\n' + ' '.join(forthlineanswers).rstrip()
    else:
        return ' '.join(firstlinevalues).rstrip() + '\n' + ' '.join(secondlineoperators).rstrip() + '\n' + ' '.join(dashline).rstrip()


