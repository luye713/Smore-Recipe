def html_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    # if not pdf.err:
    return HttpResponse(result.getvalue(), content_type='application/pdf')
    # return None

def recipe_download(request, recipe_id):

    def get(request, *args, **kwargs):
        print('lallal')
        # recipe = Recipe.objects.get(id=recipe_id)
        open('main_app/temp.html', "w").write(render_to_string('main_app/temp.html'))

        pdf = html_to_pdf('main_app/temp.html')
        print(f"mmmmmm {pdf}")
        return HttpResponse(pdf, content_type='application/pdf')
    
    return get(request)