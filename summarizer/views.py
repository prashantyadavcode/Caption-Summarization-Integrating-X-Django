from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import summarize_caption, post_tweet

@csrf_exempt
def summarize_and_tweet(request):
    """
    API endpoint to summarize a caption and post it as a tweet.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            caption = data.get("caption", "")

            if not caption:
                return JsonResponse({"success": False, "error": "Caption is required."}, status=400)

            summary = summarize_caption(caption)
            tweet_response = post_tweet(summary)

            return JsonResponse(tweet_response)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)