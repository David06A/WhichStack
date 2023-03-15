import os

import openai

openai.api_key = os.getenv("OPENAI_KEY")

class Response():
    def test(self, prompt):   
        res = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {
                    "role": "system",
                    "content": f'''
                        You're going to passed through a prompt from a user.
                        Here is the prompt: {prompt}
                        The context is that the user is asking you for help to decide what tech stack and frameworks they should use.
                        If the user prompt doesn't do this, reply saying you dont understand the prompt.

                        Here is the purpose of their project: 
                        Only reply with the stack/framework information in a human readable way.
                        Always give them information about where they can learn about the stack and some links to documentation.
                        Structure the doc references like 'framework - url\n'.
                        Tell them why the frameworks/stacks you chose are good for their prompt
                        Also tell them how they work well together at the end.
                        And keep the docs at the bottom, telling them check them out.
                        '''
                }
            ]
        )

        if res["choices"][0]["finish_reason"] == "stop":
            return res
    '''
    def request(self, ctx: dict):   
        res = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {
                    "role": "system",
                    "content": f
                        You'll be given a prompt.
                        The context is that a user has answered some questions.
                        You need to use the answers to those questions to pick them a tech stack for their project.
                        The purpose of the project is: {"".join(f"{item}\n" for item in ctx["purpose"].values())}
                        The user's experience in programming is: {"".join(f"{item}\n" for item in ctx["experience"].values())}
                        The user's budget: {"".join(f"{item}\n" for item in ctx["budget"].values())}
                        Their predicted timeframe for the project: {"".join(f"{item}\n" for item in ctx["timeline"].values())}
                        The stacks they currently know: {"".join(f"{item}\n" for item in ctx["stacks"].values())}
                        The programming languages they know: {"".join(f"{item}\n" for item in ctx["languages"].values())}
                        Database hosts they are familar with: {"".join(f"{item}\n" for item in ctx["database"].values())}
                        Hosting providers they are familiar with: {"".join(f"{item}\n" for item in ctx["providers"].values())}

                        Use their current knowledge to format your stack of choice.

                        Also tell them how the frameworks and languages you chose work well together. 

                        Tell them why you think the chosen tech stack is good based on what the user gave.

                        Structure the doc references like 'framework - url\n'.
                        And keep the docs at the bottom, telling them check them out.
                        
                }
            ]
        )

        if res["choices"][0]["finish_reason"] == "stop":
            return res
    '''


    def requesttest(self):   
        res = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
                {
                    "role": "system",
                    "content": f'''
                        You'll be given a prompt.
                        The context is that a user has answered some questions.
                        You need to use the answers to those questions to pick them a tech stack for their project.
                        Make it human readable and friendly.
                        Make it look like you're telling the user and like it's you who's giving the suggestions
                        Don't title the paragraphs like "frontend:", use the titles within the paragraphs

                        Use their current knowledge to format your stack of choice
                        The stack must be a combination of the user's choices and must make sense to use in a real project.
                        There isn't a need to take into account every user input

                        Also tell them how the frameworks and languages you chose work well together. 

                        Tell them why you think the chosen tech stack is good based on what the user gave.

                        Structure the doc references like 'framework - url\n'.
                        And keep the docs at the bottom, telling them check them out.
                        Use normal bullet points and not numbered bullet points

                        The purpose of the project is: I want to build a website
                        The user's experience in programming is: I am an advanced
                        The user's budget: I have a small budget
                        Their predicted timeframe for the project: I have a long timeframe
                        The stacks they would prefer to use: I want to use React\nI want to use Node\nI want to use Vue\nI want to use angular
                        The programming languages they would prefer to use: I want to use Java\nI want to use GO
                        Database hosts they would prefer: I want to use MongoDB\nI want to PostgreSQL
                        Hosting providers they would prefer: I want to use GCP\nI want to use Heroku


                        '''
                }
            ]
        )

        if res["choices"][0]["finish_reason"] == "stop":
            return res

print(Response().requesttest())