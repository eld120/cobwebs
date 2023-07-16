from django.shortcuts import render


def bad_request_400(request, exception):
    return render(request, "errors/400.html", context={})


def forbidden_403(request, exception):
    return render(request, "errors/403.html", context={})


def not_found_404(request, exception):
    return render(request, "errors/404.html", context={})


def server_error_500(request):
    return render(request, "errors/500.html", context={})
