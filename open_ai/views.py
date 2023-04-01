from rest_framework.response import Response
from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated

from SmartFriend.helpers import serialize_dump_json, serialize_load_json
from auth_app.models import Profile
from open_ai.tasks import start_conversation, get_response


class OpenAIResponseView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        profile = Profile.objects.get(user_id=request.user.id)

        profile.current_conversation_messages = serialize_load_json(
            profile.current_conversation_messages
        )

        if not profile.current_conversation_messages:
            profile.current_conversation_messages = start_conversation(
                profile.summary_conversation
            )

        print("The req data", request.data.get("text"))

        if request.data.get("text"):
            profile.current_conversation_messages.append({
                'role': 'user',
                'content': request.data.get('text'),
            })

        response = get_response(profile.current_conversation_messages)

        profile.current_conversation_messages = serialize_dump_json(
            profile.current_conversation_messages
        )
        profile.save()

        print("the conv is ", profile.current_conversation_messages)

        return Response({"response": response}, status=status.HTTP_200_OK)
