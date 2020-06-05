from django.shortcuts import render
from django.views.generic.base import View

from .models import Machine, CombatNutrion


class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')

class MachinesView(View):

    def get(self, request):
        machines = Machine.objects.all()
        return render(request, 'machines/machine_list.html', {'machine_list': machines})

class MachineDetailView(View):

    def get(self, request, slug):
        machine = Machine.objects.get(url=slug)
        return render(request, 'machines/machine_detail.html', {'machine': machine})

class CombatNutrionView(View):

    def get(self, request):
        products = CombatNutrion.objects.all()
        return render(request, 'combat_nutrion/combat_nutrion_list.html', {'products': products})

class CombatNutrionDetailView(View):

    def get(self, request, slug):
        product = CombatNutrion.objects.get(url=slug)
        return render(request, 'combat_nutrion/combat_nutrion_detail.html', {'product': product})

class BuyView(View):

    def get(self, request):
        return render(request, 'buy.html')

