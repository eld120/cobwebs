from django.shortcuts import render


def bad_request_400(request, exception):
    return render(request, "400.html", context={})


def forbidden_403(request, exception):
    return render(request, "403.html", context={})


def not_found_404(request, exception):
    return render(request, "404.html", context={})


def server_error_500(request):
    return render(request, "500.html", context={})
