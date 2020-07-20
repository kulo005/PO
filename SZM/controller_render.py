from django.shortcuts import render


class ControllerRender:

    def render_func(self, request, html=None, dict=None):
        return render(request, html, dict)