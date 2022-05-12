from django.shortcuts import render,redirect
from polls.models import PollingUnit,AnnouncedPuResults,Lga
from polls.forms import PollingUnitForm,PollingUnitResultForm
from django.contrib import messages



def display_polling_units(request):
    p_units = PollingUnit.objects.all()
    return render(request, 'pollunit.html', {'p_units': p_units})

def display_individual_result(request,_id):
    p_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=_id)
    return render(request, 'display.html', {'p_results': p_results})

def display_lga(request):
    lga  = Lga.objects.all()
    return render(request, 'lgadisplay.html', {'lgas':lga})

def display_lga_result(request,lga_id):
    units = []
    party = []
    scores = []
    final_sum = []
    party_list = []
    lga_p_results_list = []
    RvsD = dict()
    p_units = PollingUnit.objects.filter(lga_id=lga_id)
    for p_unit in p_units:
        units.append(p_unit.uniqueid)
    for unit_id in units:
        lga_p_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit_id)
        lga_p_results_list.append(lga_p_results)
    for lga_p_results in lga_p_results_list:
        ans = lga_p_results
        for i in ans:
            party.append(i.party_abbreviation)
            scores.append(i.party_score)
    my_dict = dict(((y, x) for x, y in tuple(zip(party,scores))))
    for k,v in my_dict.items():
        RvsD.setdefault(v, []).append(k)
    for party in RvsD.keys():
        if party=='LABOUR':
            party = 'LABO'
        party_list.append(party)   
        final_sum.append(sum(RvsD[party]))
    votes = (dict(zip(party_list,final_sum)))
    return render(request, 'lgaresults.html', {'votes':votes})

def register_new_polling_unit(request):
    if request.method == 'POST':
        form = PollingUnitForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.save()
            print(forms)
            unique_id = forms.uniqueid
            messages.success(request, 'Successfully created Polling unit')
            return redirect('newresults', unique_id)
    else:
        form = PollingUnitForm()
        return render(request,'registerpollunit.html',{'form':form})
    
def record_new_polling_result(request,uniqueid=None):
    if request.method == 'POST':
        empty_form = PollingUnitResultForm()
        form = PollingUnitResultForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Successfully recoded results')
        return render(request,'recordpollresults.html',{'form':empty_form,'uniqueid':uniqueid})
    else:
        form = PollingUnitResultForm()
        return render(request,'recordpollresults.html',{'form':form,'uniqueid':uniqueid})