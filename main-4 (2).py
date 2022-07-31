# import the wikipedia module so we can use wikipedia.
import wikipedia

# import the python modules to use for text summarization
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# import text-to-speech
from text_to_speech import speak

# import chatterbot
from chatterbot import ChatBot

# Name the chatbot
chatbot = ChatBot("Chatty")

# Add trainer packages
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Define the main function
def main():
    # Add personality
    personality_dog = [
        "Rollover",
        "I love rolling over for you, human",
        "Stay",
        "I will never leave your side, human",
        "Speak",
        "Bark!",
        "Shake",
        "I don't like my paws to be touched, human",
    ]

    # set up trainer
    trainer_personality_dog = ListTrainer(chatbot)

    # add additional personalities from the chatterbot corpus
    trainer_corpus = ChatterBotCorpusTrainer(chatbot)

    # train the personalities
    trainer_corpus.train("chatterbot.corpus.english")
    trainer_personality_dog.train(personality_dog)

    # Introduction
    print()
    print("Get ready to meet your personal dog!")
    print("While most dogs will eat your homework, this one will do it for you!")
    print("You can tell it to do anything that you want!")
    print("Just remember, it is a dog, so it's respnses will be what you would normally get from a dog.")
    print()
    # Ask user to input dog's name
    dogName = input("What would you like your dog's name to be?: ")
    print()
    # Instructions
    print("Great! Now we just need to tell our dog what to do! Try to use single word dog command responses for this, or else he may act strange...")
    print("Some examples of what you can tell him are 'Shake', 'Rollover', and my favorite 'Homework!")
    print("Just say bye whenever you're done.")
    print()

    # Loop for speaking with dog
    is_exit = False
    while is_exit == False:
        # Get command for dog from user
        userInput = input("What do you want your dog to do?: ")
        print()
        # end loop if "bye" is found in userInput
        if (userInput.lower().find("bye")) != -1:
            is_exit = True
            # print then speak
            print("I love being your dog, goodnight, human.")
            speak("I love being your dog, goodnight, human.")
        # Ask user for the homework they need help with
        elif (userInput.lower() == "homework"):
            moreTopics = "y"
            # Open File for appending and reading
            File_object = open("research.txt","a+")
            # Loop for adding more than one topic
            while moreTopics == "y":
                # print then speak
                print("What homework do you have? I mean... bark?")
                speak("What homework do you have? I mean... bark?")
                print()
                # Get topic from user
                homeworkTopic = input("Enter a topic: ")
                print()
                # Get information on topic from wikipedia
                researchResult = wikipedia.summary(homeworkTopic)
                File_object.write(researchResult)
                File_object.write("\n\n")
                # Ask user if they want to add more topics
                print("Do you need information on anything else? (y/n)")
                speak("Do you need information on anything else?")
                moreTopics = input()
            # Close file
            File_object.close()
            # reopen file so that it can start reading from the beginning of the file
            File_object = open("research.txt", "r")
            # store file into variable
            researchText = File_object.read()
            # close file again
            File_object.close()
            # Run summarizer function
            summarizer(researchText)
            print()
            # Ask the user if they'd like the summary to be read to them.
            print("Okay, I am all done, I've given you a file with my full research along with a summary of it. Would you like me to read the summary to you? (y/n)")
            speak("Okay, I am all done, I've given you a file with my full research along with a summary of it. Would you like me to read the summary to you?")
            readSummary = input()
            if (readSummary == "y"):
                # Read File by reopening it so that the handle is at the beginning of the file
                File_object = open("summary.txt", "r")
                summaryText = File_object.read()
                print(summaryText)
                speak(summaryText)
                File_object.close()
        # print and read dog's response if user input is not "bye" or "homework"
        else:    
            bot_response = chatbot.get_response(userInput)
            print(dogName + ": ", bot_response)
            speak(str(bot_response))
            print()

# summarizer function
def summarizer(text):
    # create a parser to hold our data
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    # Use the lex rank summarizer
    summarizer = LexRankSummarizer()
    # Set the number of sentences to return that make up our summary.
    number_of_sentences = 10
    # Summarize the text, this is the heart of the program
    summary = summarizer(parser.document, number_of_sentences)

    # Open summary.txt for appending and reading
    File_object = open("summary.txt","a+")
    # write summary to file
    for sentence in summary:
        strSentence = str(sentence)
        File_object.write(strSentence)
        File_object.write(" ")
    # Close the file
    File_object.close()
    
# Look for a main function, when found, go to it
if __name__ == '__main__':
    main()