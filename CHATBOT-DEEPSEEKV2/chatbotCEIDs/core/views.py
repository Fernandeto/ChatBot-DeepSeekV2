from django.shortcuts import render
from openai import OpenAI



client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="[YOUR_API_KEY]",
)

messages = [{"role": "system", "content": "Funciona como un asistente que resuelve las dudas del usuario, responde en un solo parrafo sin caracteres especiales."}]


def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("message")

        if user_input:
            messages.append({"role": "user", "content": user_input})

            # Obtener respuesta del modelo
            response = client.chat.completions.create(
                model="deepseek/deepseek-prover-v2:free",
                messages=messages,
                max_tokens=300,
                temperature=0.7,

            )
            
            try:
                bot_reply = response.choices[0].message.content.strip()
            except Exception as e:
                bot_reply = f"Error: {e}"
                
            messages.append({"role": "assistant", "content": bot_reply})

    return render(request, "chatFront.html", {
        "messages": messages,
    })

