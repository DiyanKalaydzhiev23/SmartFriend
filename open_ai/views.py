from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated

from auth_app.models import Profile
from open_ai.tasks import get_response_from_text


class OpenAIResponseView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        profile = Profile.objects.get(user_id=request.user.id)

        text = profile.current_conversation_messages
        text.append(request.data.get('text'))
        text = ". ".join(text)  # start new sentence

        response = get_response_from_text(text)

        profile.current_conversation_messages.append(response)
        profile.save()

        return Response({"response": response}, status=status.HTTP_200_OK)
