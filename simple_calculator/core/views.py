from django.http import JsonResponse
from django.shortcuts import render


def calculator(request):
    # Handle AJAX calculation requests
    if request.GET.get("ajax") == "true":
        num1 = request.GET.get("num1", "")
        num2 = request.GET.get("num2", "")
        operator = request.GET.get("operator", "")

        result = None

        if num1 != "" and num2 != "" and operator != "":
            try:
                f_num1 = float(num1)
                f_num2 = float(num2)

                if operator == "+":
                    result = f_num1 + f_num2

                elif operator == "-":
                    result = f_num1 - f_num2

                elif operator == "*":
                    result = f_num1 * f_num2

                elif operator == "/":
                    if f_num2 == 0:
                        result = "Cannot divide by zero!"
                    else:
                        result = f_num1 / f_num2

                else:
                    result = "Invalid operator!"

                # Convert whole-number floats to integers
                if type(result) is float and result % 1 == 0:
                    result = int(result)

            except ValueError:
                result = "Invalid input!"

        return JsonResponse({"result": result})

    return render(request, "core/index.html")
