import digitalocean
manager = digitalocean.Manager(token="5cf83622dbd42fd84fb769425df63237687e19ce4af54b9901b0f6d20e768220")
my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    print(droplet)