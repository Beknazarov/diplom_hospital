# coding=utf-8
import cStringIO

from django.utils.encoding import smart_text

from hospital import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.template import Context
from django.template.loader import get_template, render_to_string

import xhtml2pdf.pisa as pisa


def create_pdf(request):
    template = get_template('test_report.html')
    media = settings.MEDIA_ROOT
    context = Context({'eng':'english','rus':'русский','media':media})

    html = template.render(context)
    result = cStringIO.StringIO()
    pdf = pisa.CreatePDF(cStringIO.StringIO(html.encode('utf-8')), result, show_error_as_pdf=True,
                         encoding='UTF-8')
    if not pdf.err:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Desposition'] = 'attachment; filename=file.pdf'
        response.write(result.getvalue())
        result.close()
        return response


def show_render_html(request):
    template = 'test_report.html'
    media = settings.MEDIA_ROOT
    context = Context({'eng': 'english', 'rus': 'русский', 'media': media})
    return render_to_response(template, context)

def render_pdf(request):
    template = get_template('test_report.html')
    media = settings.MEDIA_ROOT
    context = {'eng': 'english', 'rus': 'русский', 'media': media}
    html = template.render(context)
    result = cStringIO.StringIO()
    pdf = pisa.pisaDocument(cStringIO.StringIO(html.encode('utf-8')), result, show_error_as_pdf=True, encoding='UTF-8')
    if not pdf.err:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Desposition'] = 'attachment; filename=file.pdf'
        response.write(result.getvalue())
        result.close()
        return response
    else:
        redirect('/')


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = cStringIO.StringIO()
    pdf = pisa.pisaDocument(cStringIO.StringIO(html.encode('utf-8')), result, show_error_as_pdf=True, encoding='UTF-8')
    if not pdf.err:
        return result.getvalue()
    return False


def rendering_pdf(request):
    template = 'test_report.html'
    media = settings.MEDIA_ROOT
    context = {'eng': 'english', 'rus': 'русский', 'media': media}
    pdf = render_to_pdf(template, context)
    if pdf:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Desposition'] = 'attachment; filename=file.pdf'
        response.write(pdf)
        return response
    else:
        redirect('/')