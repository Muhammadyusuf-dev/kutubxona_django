from django.shortcuts import render, get_object_or_404, redirect
from .models import Muallif, Kitob, Record, Talaba


def home(request):
    return render(request, 'index.html')


def barcha_kitoblar(request):
    kitoblar = Kitob.objects.all()
    nom_soz = request.GET.get('qidiruv')
    janr_soz = request.GET.get('janr')

    if nom_soz:
        kitoblar = kitoblar.filter(nom__icontains=nom_soz)
    if janr_soz:
        kitoblar = kitoblar.filter(janr__icontains=janr_soz)

    return render(request, 'kitoblar_royxati.html', {'kitoblar': kitoblar})


def kitob_detail(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    return render(request, 'kitob_detail.html', {'kitob': kitob})


def barcha_mualliflar(request):
    mualliflar = Muallif.objects.all()
    ism_soz = request.GET.get('qidiruv')

    if ism_soz:
        mualliflar = mualliflar.filter(ism__icontains=ism_soz)

    return render(request, 'mualliflar_royxati.html', {'mualliflar': mualliflar})


def muallif_detail(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)
    return render(request, 'muallif_detail.html', {'muallif': muallif})


def muallif_ochirish(request, pk):
    muallif = get_object_or_404(Muallif, id=pk)
    muallif.delete()
    return redirect('barcha_mualliflar')


def barcha_recordlar(request):
    recordlar = Record.objects.all()
    talaba_ismi = request.GET.get('talaba_ismi')

    if talaba_ismi:
        recordlar = recordlar.filter(talaba__ism__icontains=talaba_ismi)

    return render(request, 'recordlar_royxati.html', {'recordlar': recordlar})


def record_detail(request, pk):
    record = get_object_or_404(Record, id=pk)
    return render(request, 'record_detail.html', {'record': record})


def record_ochirish(request, pk):
    record = get_object_or_404(Record, id=pk)
    record.delete()
    return redirect('barcha_recordlar')


def barcha_talabalar(request):
    talabalar = Talaba.objects.all()
    tartib = request.GET.get('tartib')

    if tartib == 'ism':
        talabalar = talabalar.order_by('ism')
    elif tartib == 'kurs':
        talabalar = talabalar.order_by('kurs')

    return render(request, 'talabalar_royxati.html', {'talabalar': talabalar})


def tirik_mualliflar(request):
    mualliflar = Muallif.objects.filter(tirik=True)
    return render(request, 'mualliflar_royxati.html', {'mualliflar': mualliflar})


def top_sahifali_kitoblar(request):
    kitoblar = Kitob.objects.order_by('-sahifa')[:3]
    return render(request, 'kitoblar_royxati.html', {'kitoblar': kitoblar})


def top_kitobli_mualliflar(request):
    mualliflar = Muallif.objects.order_by('-kitob_soni')[:3]
    return render(request, 'mualliflar_royxati.html', {'mualliflar': mualliflar})


def oxirgi_recordlar(request):
    recordlar = Record.objects.order_by('-olingan_sana')[:3]
    return render(request, 'recordlar_royxati.html', {'recordlar': recordlar})


def tirik_muallif_kitoblari(request):
    kitoblar = Kitob.objects.filter(muallif__tirik=True)
    return render(request, 'kitoblar_royxati.html', {'kitoblar': kitoblar})


def badiiy_kitoblar(request):
    kitoblar = Kitob.objects.filter(janr__icontains='badiiy')
    return render(request, 'kitoblar_royxati.html', {'kitoblar': kitoblar})


def yoshi_katta_mualliflar(request):
    mualliflar = Muallif.objects.order_by('tugilgan_sana')[:3]
    return render(request, 'mualliflar_royxati.html', {'mualliflar': mualliflar})


def kam_kitobli_muallif_kitoblari(request):
    kitoblar = Kitob.objects.filter(muallif__kitob_soni__lt=10)
    return render(request, 'kitoblar_royxati.html', {'kitoblar': kitoblar})


def bitiruvchi_recordlari(request):
    recordlar = Record.objects.filter(talaba__kurs__icontains='4')
    return render(request, 'recordlar_royxati.html', {'recordlar': recordlar})