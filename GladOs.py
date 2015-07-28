#!/usr/bin/env python2
# -*- coding: utf8 -*-

import irclib
import ircbot

class BotModeration(ircbot.SingleServerIRCBot):
    def __init__(self):
        """
        Constructeur qui pourrait prendre des paramètres dans un "vrai" programme.
        """
        ircbot.SingleServerIRCBot.__init__(self, [("irc.gg.st", 6667)],
                                           "GladOs", "The cake is a lie")
        self.insultes = ["con", "pute", "cake"] # Liste à agrandir pour un "vrai" programme.

    def on_welcome(self, serv, ev):
        """
        Méthode appelée une fois connecté et identifié.
        Notez qu'on ne peut rejoindre les canaux auparavant.
        """
        serv.join("#anime-story")
        #serv.join("#test-bot-as")
        
    def on_join(self, serv, ev):
        auteur = irclib.nm_to_n(ev.source())
        canal = ev.target()
        
        if auteur == "GladOs":
            serv.privmsg(canal, "It's been a long time. How have you been?")
        else:
            serv.privmsg(canal, "Oh... It's you " + auteur + ". Continue testing !")

    def on_pubmsg(self, serv, ev):
        """
        Méthode appelée à la réception d'un message, qui exclut son expéditeur s'il
        écrit une insulte.
        """
        
        # Il n'est pas indispensable de passer par des variables
        # Ici elles permettent de clarifier le tout.
        auteur = irclib.nm_to_n(ev.source())
        masque_auteur = ev.source()
        canal = ev.target()
        message = ev.arguments()[0].lower() # Les insultes sont écrites en minuscules.
        
        if message == "!quit" and irclib.mask_matches(masque_auteur, "*!*@GG-B3C3AEFC.w80-15.abo.wanadoo.fr"):
            #serv.privmsg(canal, "You murder me !")
            serv.part(canal, "You murder me !")
            self.die()
        
        for insulte in self.insultes:
            if insulte in message:
                serv.privmsg(canal, "3...")
                serv.execute_delayed(1, serv.privmsg, (canal, "2..."))
                serv.execute_delayed(2, serv.privmsg, (canal, "1..."))
                serv.execute_delayed(3, serv.kick, (auteur, "Continue testing !"))
                break

if __name__ == "__main__":
    BotModeration().start()
