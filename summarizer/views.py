from django.shortcuts import render
from django.http import JsonResponse
from .forms import TextSummaryForm
from .models import TextSummary
from .summarizer import TextSummarizer
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    form = TextSummaryForm()
    return render(request, 'summarizer/index.html', {'form': form})

@csrf_exempt
def summarize_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            num_sentences = int(data.get('num_sentences', 3))
            
            # Initialize summarizer and generate summary
            summarizer = TextSummarizer()
            summary = summarizer.generate_summary(text, num_sentences)
            
            # Save to database
            text_summary = TextSummary.objects.create(
                original_text=text,
                summary=summary
            )
            
            return JsonResponse({
                'success': True,
                'summary': summary,
                'summary_id': text_summary.pk
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
