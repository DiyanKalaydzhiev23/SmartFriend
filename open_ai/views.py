from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated

from SmartFriend.helpers import BONUS_CONDITION
from auth_app.models import Profile
from open_ai.tasks import get_response_from_text


class OpenAIResponseView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        profile = Profile.objects.get(user_id=request.user.id)

        profile.current_conversation_messages.append({
            'role': 'user',
            'content': request.data.get('text'),
        })

        # if text:
        #     text += " " + BONUS_CONDITION

        # text = text.replace("\n", "")

        response = get_response_from_text(profile.current_conversation_messages)

        profile.current_conversation_messages.append({
            'role': 'user',
            'content': response,
        })

        profile.save()

        print("the conv is ", profile.current_conversation_messages)

        return Response({"response": response}, status=status.HTTP_200_OK)
