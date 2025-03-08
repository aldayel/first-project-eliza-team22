class Dictionary():
   
        
    

    def regex_dic(self):
        return {
            
            "greetings": [
                "Hello", "Hi", "Hey", "Greetings", "Good morning", "Good afternoon", "Good evening",
                "How are you?", "Hey there!", "What's up?", "Yo!", "Welcome", "Nice to see you", 
                "Hi there!", "Hey!", "Hello there!", "Hi friend!", "Nice to meet you!", "How's it going?", 
                "Hope you're having a great day!", "It's a pleasure to meet you.", "How do you do?", 
                "Hello friend!", "Nice to see you!", "Hey there, how's everything?", "How's your day going?", 
                "Hope you're doing great!", "Hey hey!",  "Yo yo!", "Look who's here!", 
                "How's life?", "How's everything?", "What's new?", "What's happening?"],

            "user_condition_keywords": [
            "i'm good",  "doing great", "i'm fine", 
            "i'm okay",  "not bad", "pretty good", "i'm well",
            "feeling great", "i'm doing fine", "all good", "i'm alright", "i feel good",
            "not too bad", "i'm well, thanks", "everything's good", "can't complain",
            "doing well", "i'm happy", "feeling awesome", "i'm doing okay",
            "life's good", "i'm chilling", "i'm fantastic", "i feel amazing","Thanks for asking!","I appreciate you asking!","thanks for ask"],



        'user_answers_keywords' : [
            "yes", "of course", "sure", "definitely", "why not", "okay", 
            "sounds good", "yep", "yeah", "absolutely", "go ahead", 
            "let's do it", "fine", "alright", "I'd love to"]      }

    

    def regex_answr(self):
        return   {
                ## if user ask about bot condition ,and must likley  end of the sentence it  contian a (?)question mark
            "for_question_greetings":
                    
                        ["I'm good, thanks for asking! How about you?", 
                        "I'm doing great! What about you?", 
                        "Feeling fantastic! How are you?", 
                        "Pretty good! Enjoying some coffee!"],



            # if the user ask ask as general greetings like hi , hello , hey there
            "general_greetings": [
                "Hey there! How's your day going?", 
                "Hello! Hope you're having a great day! How are you?", 
                "Hi there! What's new with you?", 
                "Hey! Glad to see you! How's it going?"
            ],


            ##here if bot recive from the user his condition like im good  or thanks for ask -------> regexDic keys -->user_condition_keywords
            ## force the user for our topic 
            "user_condition": ["That's great to hear! Do you have anything to ask about coffee?", 
                        "Glad to hear that! Are you in the mood for some coffee talk?", 
                        "Awesome! Speaking of good things, do you have any intrest in coffee?", 
                        "Nice! By the way, do you have any coffee-related questions?"],


            ##if the bot has unexpected input in the greetings converstion this will handle it to force the user in our topic
            "first_time_unexpected": 
                        ["Sorry, I didn't quite get that. Just to clarify, I'm here to help you with coffee-related topics!",
                        "Hmm, I specialize in all things coffee ☕. Want to learn how to make a great espresso?",
                        "I'm here to talk about coffee! For example, I can teach you how to make the perfect drip coffee. What do you think?",
                        "My expertise is in coffee! If you're interested, I can tell you about different  methods like how to make V60."],




            "going_fast_to_middle_of_conversation": 
            
                    ["Whoa! Jumping straight in, I like it! But let;s make sure—are we here to talk about coffee? ☕ ", 
                    "No warm-up? I respect that! Just to confirm, are we diving into coffee discussions?", 
                    "Straight to business, I love it! But before we go further—do you want to explore the world of coffee? ☕ ", 
                    "No small talk? Fine by me! But before we move ahead, can you confirm—are we talking about coffee? ", 
                    "I like your direct approach! But before we continue, do you want to discuss coffee-related topics?", 
                    "Straight to the point! Just to be sure, are you here for coffee tips, recipes, or brewing guides? ", 
                    "No chit-chat? I can handle that! But tell me—are you ready to dive into the world of coffee? ☕ "],
            }

   

