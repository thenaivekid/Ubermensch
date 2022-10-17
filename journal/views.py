import markdown2

from django.shortcuts import render, redirect

from . import utils
import random

#Write your views here
def index(request):
    """Main page."""

    context = {
        "entries": utils.list_entries(),
        
    }
    
    return render(request, "journal/index.html", context)


def readjournal(request, entry_name):
    """Render entry page."""

    # convert markdown to html
    ef_content = utils.get_entry(entry_name)
    if ef_content:
        ef_content_html = markdown2.markdown(ef_content)
        

        return render(request, "journal/journal.html", {
            'entry_content': ef_content_html
        })
    else:
        return redirect("journal:index")


def search(request):
    """Search form."""

    keyword = request.GET['keyword']
    if keyword in utils.list_entries():
        return redirect('journal:readjournal', entry_name=keyword)
    else:
        return render(request,'journal/index.html',{
            'results':"No Journal Found for such date.",
            'entries': utils.list_entries()
        })
    
def newjournal(request):
    if request.method == 'POST':
        title = request.POST['title']
        highlights = request.POST['highlights']
        fun_stuffs = request.POST['fun_stuffs']
        emotions= request.POST["emotions"]
        what_went_right= request.POST["what_went_right"]
        what_went_wrong= request.POST["what_went_wrong"]
        rating= request.POST["rating"]
        utils.save_entry(title, f'# {title}\n\n## Highlights of the day \n {highlights}\n## Fun stuffs\n{fun_stuffs}\n## Emotions\n{emotions}\n## What went right\n{what_went_right}\n## What went wrong\n{what_went_wrong}\n## Rating: {rating}')
        return redirect('journal:readjournal', entry_name=title)
    return render(request, 'journal/newjournal.html')

def randomjournal(request):
    journals= utils.list_entries()
    journal = random.choice(journals)
    return redirect('journal:readjournal', entry_name=journal)