import requests as requests

while True:
    request = input()
    requesttype = request.split()[0]
    try:
        requestarg1 = request.split()[1]
        requestarg2 = request.split()[2]
        requestarg3 = request.split()[3]
        requestargnull = request.split(78378473874)
    except:
        print()
        
        # friends
    if requesttype == 'get-friends':
        print(requests.get('http://api.roblox.com/users/' + requestarg1 + '/friends').text)
    elif requesttype == 'get-friends-count':
        print(requests.get('http://api.roblox.com/user/get-friendship-count?userId=' + requestarg1).text)
    elif requesttype == 'following-exists':
        print(requests.get('http://api.roblox.com/user/following-exists?userId=' + requestarg1 + '?followerUserId=' + requestarg2).text)
    elif requesttype == 'help': # forgot this
        print('friends')
        print('get-friends <userId>')
        print('get-friends-count <userId>')
        print('following-exist <followeeUserId> <followerUserId>')
        print(' ')
        print('groups')
        print('groups-in <userId>')
        print('group-info <groupId>')
        print('group-allies <groupId>')
        print('group-enemies <groupId>')
        print('')
        print('marketplace')
        print('product-info <assetId>')
        print('gamepass-info <gamepassId>')
        print('has-asset <userId> <assetId>')
        print('')
        print('users')
        print('user-info <userId>')
        print('get-by-username <username>')
        print('can-manage <userId> <assetId>')
        print('')
    # groups
    elif requesttype == 'groups-in':
        print(requests.get('http://api.roblox.com/users/' + requestarg1 + '/groups').text)
    elif requesttype == 'group-info':
        print(requests.get('http://api.roblox.com/groups/' + requestarg1).text)
    elif requesttype == 'group-allies':
        print(requests.get('http://api.roblox.com/groups/' + requestarg1 + '/allies').text)
    elif requesttype == 'group-enemies':
        print(requests.get('http://api.roblox.com/groups/' + requestarg1 + '/enemies').text)
    # marketplace
    elif requesttype == 'product-info':
        print(requests.get('http://api.roblox.com/marketplace/productinfo?assetId=' + requestarg1).text)
    elif requesttype == 'gamepass-info':
        print(requests.get('http://api.roblox.com/marketplace/game-pass-product-info?gamePassId=' + requestarg1).text)
    elif requesttype == 'has-asset':
        print(requests.get('http://api.roblox.com/ownership/hasasset?userId=' + requestarg1 + '?assetId=' + requestarg2).text)
        # users
    elif requesttype == 'user-info':
        print(requests.get('http://api.roblox.com/users/' + requestarg1).text)
    elif requesttype == 'get-by-username':
        print(requests.get('http://api.roblox.com/users/get-by-username?username=' + requestarg1).text)
    elif requesttype == 'can-manage':
        print(requests.get('http://api.roblox.com/users/' + requestarg1 + '/canmanage/' + requestarg2))
    print('')
    