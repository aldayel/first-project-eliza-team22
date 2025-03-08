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
            "let's do it", "fine", "alright", "I'd love to"],
               
               
               
               
               
         ## now for middle chat
         


         "shift_from_greetings": [
    # General coffee discussion
    "coffee", "caffeine",  "beans", "roast", "espresso", "latte", "cappuccino",
    "americano", "macchiato", "mocha", "cold brew", "drip coffee", "french press",
    "aeropress", "moka pot", "turkish coffee", "v60", "pour-over", "chemex", "coffee filter",
    "grind size", "brew time", "coffee strength", "flavor", "coffee culture",

    # Questions about coffee preparation
    "how to make", "best way to make", "what,s the best", "how to prepare",
    "why does my coffee taste", "how hot should water be", "how much caffeine ","type"

    # Coffee types and comparisons
    "difference between", "arabica vs robusta", "best coffee beans", "light vs dark roast",
    "single-origin vs blend", "best espresso beans", "best coffee for french press",
    "best coffee for cold brew", "most popular coffee", "is decaf really caffeine-free",

    # Coffee opinions and experiences
    "i love coffee", "coffee is too bitter", "best coffee shop", "favorite coffee",
    "strongest coffee", "most flavorful coffee", "coffee preferences", "how do you like your coffee",
    "best milk for coffee", "best sugar for coffee", "adding syrup to coffee",


         ],


    'coffee_beans_keywords' : [
    # General coffee bean terms
    "coffee beans", "types of coffee beans", "best coffee beans", "different coffee beans",
    "coffee bean varieties", "coffee bean types", "coffee origins", "where do coffee beans come from",
    "coffee bean quality", "popular coffee beans", "coffee bean guide", "best coffee in the world",
    
    #  Most famous coffee beans
    "yemeni beans", "arabic beans", 
     "brazilian coffee beans", "colombian beans", 
    "ethiopian beans", "ethiopian coffee", "strong coffee beans",
    "arabica beans", "arabica coffee", 
    
]





    
      
               
               
               
                  }

    

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
            
                    [
                        "Ah, straight to the point! What aspect of coffee are you interested in? ☕",
                        "I love your enthusiasm! Are we talking brewing techniques, coffee beans, or something else?",
                        "No hesitation, I like that! What's on your mind—espresso, cold brew, or a new coffee recipe?",
                        "Diving right in, I respect it! What coffee-related question do you have?",
                        "Nice! Are we discussing coffee flavors, brewing methods, or coffee history today?",
                        "Straight to business! Are you looking for tips, recommendations, or coffee science?",
                        "You're ready to go, I see! Do you want to learn about coffee types, the best grind size, or the perfect cup?",
                    ],


                    
    "cappuccino": [
        "1️⃣ Brew a **double shot of espresso** (about 60ml).",
        "2️⃣ Steam about **150ml of milk** until it's velvety with microfoam.",
        "3️⃣ Pour the steamed milk over the espresso, holding back the foam.",
        "4️⃣ Add the remaining foam on top for a creamy finish. Enjoy your **Cappuccino!** ☕"
    ],
    
    "v60": [
        "1️⃣ Heat water to **92-96°C (195-205°F)**.",
        "2️⃣ Place a **V60 paper filter** in the dripper and rinse it with hot water.",
        "3️⃣ Add **15-18g of medium-fine ground coffee** into the filter.",
        "4️⃣ Start pouring **30-40ml of water** in a circular motion for blooming (30 seconds).",
        "5️⃣ Continue pouring in slow, steady spirals until you reach **250-300ml of total water**.",
        "6️⃣ Let it drip completely, then enjoy your perfectly brewed **V60 coffee!** ☕"
    ],
    
    "latte": [
        "1️⃣ Brew a **single or double shot of espresso** (30-60ml).",
        "2️⃣ Steam **200-250ml of milk** until it's silky with light foam.",
        "3️⃣ Pour the steamed milk over the espresso in a **tall glass**.",
        "4️⃣ If you like, top with a bit of foam or **latte art**. Enjoy your **Latte!** ☕"
    ],

    "drip coffee": [
        "1️⃣ Use a **standard coffee machine** or a pour-over dripper.",
        "2️⃣ Add **15-20g of medium-coarse ground coffee** per **250ml of water**.",
        "3️⃣ If using a machine, add water and start brewing. If using a dripper, pour in slow spirals.",
        "4️⃣ Let the coffee drip completely and enjoy your **Drip Coffee!** ☕"
    ],

    'unknown_coffee_responses' : [
    "Hmm, I don't have the recipe for that one! But I can help you with Cappuccino, V60, Latte, or Drip Coffee. ☕",
    "That's an interesting coffee! I don't have the recipe for it, but I can guide you through making some popular types like Cappuccino or V60. Would you like that?",
    "I haven't learned that one yet! Maybe you'd like to try a Latte or Drip Coffee instead? ☕",
    "Oops! That coffee type isn't in my list. But I can still help! Do you want to learn how to make Espresso-based drinks or Pour-over coffee?",
    "I'm not sure about that coffee, but I can tell you how to make a great Cappuccino, Latte, or V60! Which one interests you?",
    "That sounds delicious, but I don't have the exact steps for it yet! Would you like to hear about another coffee method instead?",
    "I love discovering new coffee types! Unfortunately, I don't have the instructions for that one. But I can guide you on making some of the best classics like Latte or V60!"
],




'popular_coffee_beans': {
    "yemeni": {
        "description": "Yemeni  beans are one of the world's most ancient and prized coffee varieties. Grown in the arid, mountainous regions of Yemen, these beans are naturally sun-dried and often irregular in size due to traditional, non-industrialized farming methods. Their flavor profile is deep and complex, with a distinct chocolatey richness, earthy undertones, and hints of dried fruit. Some variations carry spicy notes of cardamom and cinnamon, making them stand out among other beans. Due to their unique processing, Yemeni Mocha beans tend to have a heavy body and a wine-like acidity, making them a favorite for those who appreciate bold and exotic coffee."
    },
    "brazil": {
        "description": "Brazil beans are known for their smooth, mild profile with a natural sweetness. Grown in Brazil's vast coffee plantations, these beans are larger and more uniform in shape than many other varieties. Their flavor leans towards nutty and chocolatey tones, often accompanied by hints of caramel and toasted almond. Because of their low acidity and creamy body, Santos beans are widely used in espresso blends and milk-based drinks. They are usually processed using either the natural or washed method, which enhances their balanced and mellow taste, making them an excellent choice for those who prefer a well-rounded, easy-drinking coffee."
    },
    "colombian": {
        "description": "Colombian  beans are highly regarded for their balanced and refined taste. These beans are grown in the high-altitude regions of Colombia, where rich volcanic soil and an ideal climate create perfect growing conditions. Sweet, chocolatey flavors are very prominent in most Colombian Supremo beans, with some fruity notes that touch on caramel, apple, and red fruits like berries. The beans are washed-processed, which gives them a clean and crisp flavor with bright acidity and a silky body. This combination makes them one of the most versatile coffee beans, ideal for both black coffee and milk-based drinks like lattes and cappuccinos."
    },
    "ethiopian": {
        "description": "Ethiopian  beans are among the most floral and aromatic coffee beans in the world. Grown in high-altitude regions of Ethiopia, the birthplace of coffee, these beans develop a uniquely complex and delicate profile. They are well-known for their bright acidity and tea-like body, with flavor notes that often include jasmine, citrus, and ripe berries. Many Yirgacheffe beans are washed-processed, which enhances their clean and vibrant taste. Their light and fruity characteristics make them a favorite for pour-over brewing methods, allowing their floral and fruity essence to shine through."
    }
} ,


##after this we will add  Hmm, you sound like a true coffee enthusiast!
'general_chatbot_responses' : [
        
        "The smell of coffee alone can help reduce stress and wake up your brain! Amazing, right?",
    

    
        "That's interesting! Are you a coffee lover, or just here to chat? ☕",
        "I love good conversations! Are we talking about coffee, or just having a casual chat?",
        "Great question! But before we continue, do you want to talk about coffee or something else?",
        "I can chat about almost anything, but coffee is my specialty! Want to learn about espresso, cold brew, or something else?",
   

   
        "Are you more into **strong, bold espresso**, or do you prefer a **smooth, creamy latte**?",
        "Light roast or dark roast? **Light roasts keep more of the original bean's flavors**, while **dark roasts bring out deep, smoky notes**. Which do you prefer?",
        "If you could only drink one coffee forever—**espresso, cappuccino, or cold brew**—which one would it be? ☕",
        "Do you take your coffee **black**, or do you like it with milk and sugar? Some say black coffee is for purists, others say ‘give me all the sugar’! 😆",
        "Some people love the bitterness of coffee, others prefer it smooth and sweet. What's your coffee style?",
  


        "If you could only drink one coffee forever, would it be **espresso, cappuccino, or cold brew**? ☕",
        "What's the most **unusual** coffee drink you’ve ever tried?",
        "If coffee had flavors based on emotions, what would **Monday morning coffee** taste like? 😂",
        "Have you ever tried making coffee with a **Moka pot or AeroPress**? They give such a unique flavor!",
        
    ],


}
