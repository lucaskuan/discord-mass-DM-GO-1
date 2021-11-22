 # Keep in mind that there's no actual api endpoint for users to get guild members.
# So, to get guild members, we have to request for and read the member list.
# This is all handled with the bot.gateway.fetchMembers(...) function :) . This function can either be run while the gateway is connected or before the gateway connects.
# Note, you'll need to connect to the gateway to get the member list.
# An example usage is below. The Guild and Channel ids used are from the fortnite server (652k members, around 150k of those are actually fetchable).
# The number of fetchable members changes from time to time.
# https://github.com/Merubokkusu/Discord-S.C.U.M/blob/master/docs/using/Gateway_Actions.md#gatewayfetchmembers

import discum
bot = discum.Client(token='OTA5MjE2MTEyMTc5MzE0NzU5.YZBD1g.c4sh-oDQ-Lns3y5ddDTMhx4d7Zo')

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members) #this line is optional
        print(str(lenmembersfetched)+' members fetched') #this line is optional
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) #get all user attributes, wait 1 second between requests
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession() #saves 10 seconds when gateway is run again
    return bot.gateway.session.guild(guild_id).members

# members = get_members('900001678202400768', '901162262256037888') # monacoplanet
# members = get_members('902984558104965120', '903024570603286588') # lucky elephant club 30k
# members = get_members('882493441056051210', '895914227544506408') # zombie ape 10k
# members = get_members('572097817422856192', '765265456365699113') # cryptovoxels
# members = get_members('902166453397118976', '903237112210554880') # citizen pink
# members = get_members('894337851762802718', '900099299646533682') # mutant cats
# members = get_members('900445693171351552', '900445693171351554') # crazy camel
# members = get_members('888055672623759410', '888056628136509470') # bricktopians
members = get_members('889565085981364224', '889565086530814024') 
 
memberslist = []

for memberID in members:
    memberslist.append(memberID)

f = open('users.txt', "a")
for element in memberslist:
    f.write(element + '\n')
f.close()