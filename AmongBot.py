import discord
import time
import os
from discord.ext import commands

class Bot(discord.Client):

    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print('')
        print(' ｡.｡:+* ﾟ ゜ﾟ *+:｡.｡:+* ﾟ ゜ﾟ *')
        print('      Connecté en tant que : ')
        print('          ' + self.user.name)
        print('｡.｡:+* ﾟ ゜ﾟ *+:｡.｡:+* ﾟ ゜ﾟ * \n')

    def create_embed(self, title, description, color, img=""):
        embed = discord.Embed()
        embed.title = title
        embed.description = description 
        if(img != ""):
            embed.set_image(url=img)
        return embed

    def canceritude():
        global x
        x = False
        
    async def on_message(self, message):

        if (message.content.startswith('/help')):
            description = "Salut, Les différentes commandes du bot sont :\n \n -Pour envoyer un code de jeu sur Among us, il suffit de faire la commande **\"/a + le code\"** \n \n -Pour demander qui veux jouer : **\"/jeu\"** \n \n -Pour faire plaisir à <@392402627746463754> et qu'il évite de chanter Shrek dans les code de jeu **\"/say + contenu\"**\n (__edit:__ t'es baisé mec <@392402627746463754>, tu peux plus le faire ca maintenant lol) \n \n -Un module de vote vient d'être ajouter, pour cela il suffit de faire un **\"/vote\"**\n \n -Toutes les couleurs sont dispo en émoji, pour cela, il faut faire **\"/+couleur\"** en **anglais**, par exemple pour avoir l'emoji <:3657_amongusvote_red:765142025217507329>, il suffit de faire **\"/red\"** \n \n -Afin de savoir qui est \"suspicieux\", la commande **\"/sus + username\"** vient d'être ajouté \n \n Un module de map vient d'être ajouter, pour cela, il suffit de faire soit **\"/mira\"**, **\"/skeld\"** ou **\"/polus\"** \n \n Voilà \n \n Bisous, Kénan"
            title = "Aide du AmongBot, par Kénan"
            embed = self.create_embed(title, description, self.user.avatar_url)  
            await message.channel.send(embed=embed)

        # if (message.content.startswith('/help')):
        #     await message.channel.send("Salut, Les différentes commandes du bot sont :\n \n -Pour envoyer un code de jeu sur Among us, il suffit de faire la commande **\"/a + le code\"** \n \n -Pour demander qui veux jouer : **\"/jeu\"** \n \n -Pour faire plaisir à <@392402627746463754> et qu'il évite de chanter Shrek dans les code de jeu **\"/say + contenu\"**\n (__edit:__ t'es baisé mec <@392402627746463754>, tu peux plus le faire ca maintenant lol) \n \n -Un module de vote vient d'être ajouter, pour cela il suffit de faire un **\"/vote\"**\n \n -Toutes les couleurs sont dispo en émoji, pour cela, il faut faire **\"/+couleur\"** en **anglais**, par exemple pour avoir l'emoji <:3657_amongusvote_red:765142025217507329>, il suffit de faire **\"/red\"** \n \n -Afin de savoir qui est \"suspicieux\", la commande **\"/sus + username\"** vient d'être ajouté \n \n Un module de map vient d'être ajouter, pour cela, il suffit de faire soit **\"/mira\"**, **\"/skeld\"** ou **\"/polus\"** \n \n Voilà \n \n Bisous, Kénan")
        

        if (message.content.startswith('/gp')):
            await message.delete()

        if (message.content.startswith('/stop')):
            print("Commande /stop appellé...")
            print("Redemmarage du " + self.user.name)
            time.sleep(1)
            os.system("python3 AmongBot.py")
            exit()
            

        callWord = '/spam '
        if (message.content.startswith(callWord)):
            realcontent = message.content[len(callWord)::]
            await message.delete()
            x = True
            while (x is True) :
                msg = await message.channel.send(realcontent)
                await msg.delete()

        callWord = '/ttsspam '
        if (message.content.startswith(callWord)):
            realcontent = message.content[len(callWord)::]
            x = True
            while (x is True) :
                msg = await message.channel.send(realcontent, tts=True)
                time.sleep(2)
                await msg.delete()
                


        if (message.content.startswith('/jeu')):
            await message.delete()
            msg = await message.channel.send("🎮 Qui pour faire une partie de Among Us?🎮")
            await msg.add_reaction("✅")
            await msg.add_reaction("❌")
            await message.channel.send("https://tenor.com/bpvuu.gif")
            ghost_ping = await message.channel.send("<@&763411334980435988>")
            await ghost_ping.delete()


        if (message.content.startswith('/skeld')):
            await message.channel.send("Map de The Skeld : " + "https://bit.ly/3iZdWXL")

        if (message.content.startswith('/polus')):
            await message.channel.send("Map de Polus : " + "https://bit.ly/3jSocC6")

        if (message.content.startswith('/mira')):
            await message.channel.send("Map de Mira HQ : " + "https://bit.ly/33PYQ2f")

        if (message.content.startswith('/all')):
            await message.channel.send("<:9750_amongusvote_yellow:765142025782820904>"+"<:7040_amongusvote_pink:765142025691201556>"+"<:6956_amongusvote_cyan:765142025725018142>"+"<:6752_amongusvote_brown:765142025648734228>"+"<:6470_amongusvote_green:765142025615966208>"+"<:5618_amongusvote_black:765142025569173514>"+"<:4652_amongusvote_darkgreen:765142025560784906>"+"<:3771_amongusvote_purple:765142025569304586>"+"<:3657_amongusvote_red:765142025217507329>"+"<:3505_amongusvote_orange:765142025535225866>"+"<:2321_amongusvote_white:765142025506390026>"+"<:2165_amongusvote_blue:765142025481748510>")

        if (message.content.startswith('/vote')):
            vote = await message.channel.send("Quel sera la sentence?")
            await vote.add_reaction("<:9750_amongusvote_yellow:765142025782820904>")
            await vote.add_reaction("<:7040_amongusvote_pink:765142025691201556>")
            await vote.add_reaction("<:6956_amongusvote_cyan:765142025725018142>")
            await vote.add_reaction("<:6752_amongusvote_brown:765142025648734228>")
            await vote.add_reaction("<:6470_amongusvote_green:765142025615966208>")
            await vote.add_reaction("<:5618_amongusvote_black:765142025569173514>")
            await vote.add_reaction("<:4652_amongusvote_darkgreen:765142025560784906>")
            await vote.add_reaction("<:3771_amongusvote_purple:765142025569304586>")
            await vote.add_reaction("<:3657_amongusvote_red:765142025217507329>")
            await vote.add_reaction("<:3505_amongusvote_orange:765142025535225866>")
            await vote.add_reaction("<:2321_amongusvote_white:765142025506390026>")
            await vote.add_reaction("<:2165_amongusvote_blue:765142025481748510>")
            await vote.add_reaction("⏩")
            
        if (message.content.startswith('/yellow')):
            await message.channel.send("<:9750_amongusvote_yellow:765142025782820904>")
            await message.delete()

        if (message.content.startswith('/pink')):
            await message.channel.send("<:7040_amongusvote_pink:765142025691201556>")
            await message.delete()

        if (message.content.startswith('/cyan')):
            await message.channel.send("<:6956_amongusvote_cyan:765142025725018142>")
            await message.delete()

        if (message.content.startswith('/brown')):
            await message.channel.send("<:6752_amongusvote_brown:765142025648734228>")
            await message.delete()   

        if (message.content.startswith('/green')):
            await message.channel.send("<:6470_amongusvote_green:765142025615966208>")
            await message.delete()    

        if (message.content.startswith('/black')):
            await message.channel.send("<:5618_amongusvote_black:765142025569173514>")
            await message.delete()  

        if (message.content.startswith('/darkgreen')):
            await message.channel.send("<:4652_amongusvote_darkgreen:765142025560784906>")
            await message.delete()  

        if (message.content.startswith('/purple')):
            await message.channel.send("<:3771_amongusvote_purple:765142025569304586>")
            await message.delete() 

        if (message.content.startswith('/red')):
            await message.channel.send("<:3657_amongusvote_red:765142025217507329>")
            await message.delete() 

        if (message.content.startswith('/orange')):
            await message.channel.send("<:3505_amongusvote_orange:765142025535225866>")
            await message.delete() 

        if (message.content.startswith('/white')):
            await message.channel.send("<:2321_amongusvote_white:765142025506390026>")
            await message.delete()

        if (message.content.startswith('/blue')):
            await message.channel.send("<:2165_amongusvote_blue:765142025481748510>")
            await message.delete()   

        callWord = '/pat '
        if (message.content.startswith(callWord)):
            realcontent = message.content[len(callWord)::]
            await message.channel.send("<a:1054_among_us_pat:765142025423028235>" + realcontent + " get patted by " + "@" + str(message.author) + "<a:1054_among_us_pat:765142025423028235>")
            await message.delete()

        callWord = '/sus '
        if (message.content.startswith(callWord)):
            realcontent = message.content[len(callWord)::]
            await message.channel.send(realcontent + " is <:6340_amongus_sus:765150297009815563>")
        
        callWord = '/say '
        if (message.content.startswith(callWord)):
            realcontent = message.content[len(callWord)::]
            await message.channel.send(realcontent)
            await message.delete()

        callWord = '/a '
        if (message.content.startswith(callWord)):
            realcontent = message.content[len(callWord)::]
            if (len(realcontent) != 6):
                await message.channel.send("Arrete de troll mmdrr, il y a 6 caractères dans un code de partie Among Us, t'as cru j'étais complètement con ou quoi?")
            else:
                description = "Code de partie : __**" + realcontent + "**__"
                title = "Une petite partie Among Us?"
                embed = self.create_embed(title, description, self.user.avatar_url)  
                await message.channel.send(embed=embed)
                ghost_ping = await message.channel.send("<@&763411334980435988>")
                await message.delete()
                await ghost_ping.delete()

token = "NzYzNDI1MD[...]hNgJyaPFk"

if __name__ == "__main__":
    bot = Bot()
    bot.run(token)

