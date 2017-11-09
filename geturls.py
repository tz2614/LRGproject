print "The URL is: ", response/geturl()
def homepage(request):
    file = urllib2.urlopen('http://www.lrg-sequence.org/downloads')
    data = file.read()
    file.close()

    data = xmltodict.parse(data)
    return render_to_response('my_template.html', {'data': data})
