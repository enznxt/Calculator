from django.shortcuts import render


def calculator(request):
    result = None

    num1 = request.GET.get("num1", "")
    num2 = request.GET.get("num2", "")
    operator = request.GET.get("operator", "")

    if num1 != "" and num2 != "" and operator != "":

        num1 =int(num1)
        num2 = int(num2)

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero!"

    return render(request, "core/index.html", context = {
        "result": result,
        "num1": num1,
        "num2": num2
    })