# ChatbotV1

This is the first iteration of a chatbot built from the ground up using the chatterbot library. The chatbot currently cannot hold up a continuous conversation, but if the prompt is within the training data set, the model will respond with the recorded correct response. There are several logic adapters commented out in the model. At the moment, all 4 adapters do not work together, but work individually as the sole logic adapter. Below are some pictures to demonstrate the level of conversation the model is at.

## After basic training using the ListTrainer class the model was able to answer questions that were exactly like the ones in the database, but failed otherwise


<img src=https://github.com/cchloet/ChatbotV1/blob/main/ChatbotEx1.png>

## After training on the corpus included in the chatterbot library, the chatbot is able to talk about a wider range of topics and its responses are more varied, but the conversation is still unfocused


<img src=https://github.com/cchloet/ChatbotV1/blob/main/ChatbotEx2.png>



More details can be found in the below resources regaurding the Chatterbot library
- Github Repository: https://github.com/gunthercox/ChatterBot/blob/master/chatterbot/logic/unit_conversion.py
- Documentation: https://chatterbot.readthedocs.io/en/stable/comparisons.html#statement-comparison
